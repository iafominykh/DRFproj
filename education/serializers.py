from rest_framework import serializers

from education.models import Course, Lesson, Payments, Subscription
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