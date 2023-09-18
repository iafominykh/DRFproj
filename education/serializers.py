from rest_framework import serializers

from education.models import Course, Lesson, Payments, Subscription
from education.services import retrieve_payment, make_payment, create_payment
from education.validators import VideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        validators = [VideoValidator(field='video')]
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        lesson = Lesson.objects.filter(course=instance)
        if lesson:
            return lesson.count()
        return 0

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lessons', 'lesson_count')


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['payment_intent_id'] = create_payment(int(validated_data.get('payment_amount')))
        payment = Payments.objects.create(**validated_data)
        return payment

    class Meta:
        model = Payments
        fields = "__all__"


class PaymentRetrieveSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField()

    def get_payment_status(self, instance):
        return retrieve_payment(instance.payment_intent_id)

    class Meta:
        model = Payments
        fields = "__all__"


class PaymentUpdateSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        payment = make_payment(instance.payment_intent_id)
        if payment == 'succeeded':
            instance.is_paid = True
            instance.save()
            return instance
        else:
            return instance

    class Meta:
        model = Payments
        fields = "__all__"