from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated



from education.models import Course, Lesson, Payments
from education.paginators import Pagination
from education.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer, \
    PaymentCreateSerializer,  PaymentRetrieveSerializer, PaymentUpdateSerializer
from education.permissions import IsOwner, IsModerator



class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = Pagination
    queryset = Course.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonListAPIView(generics.ListAPIView):
    """Список уроков"""
    serializer_class = LessonSerializer
    pagination_class = Pagination
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class PaymentsListView(generics.ListAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']


class PaymentCreateAPIView(generics.CreateAPIView):
    """
    API endpoint that allows users to create payments.
    """
    serializer_class = PaymentCreateSerializer

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """
    API endpoint that allows users to retrieve payment.
    """
    serializer_class = PaymentRetrieveSerializer
    queryset = Payments.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint that allows users to update payment.
    """
    serializer_class = PaymentUpdateSerializer
    queryset = Payments.objects.all()

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()
