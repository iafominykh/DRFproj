from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views import CourseViewSet, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    PaymentsListView, \
    LessonCreateAPIView, LessonListAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView, \
    PaymentUpdateAPIView, PaymentRetrieveAPIView, PaymentCreateAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('payment/', PaymentsListView.as_view(), name='payment_list'),
                  path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),

                  path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment-get"),
                  path(
                      "payment/update/<int:pk>/",
                      PaymentUpdateAPIView.as_view(),
                      name="payment-update",
                  ),
                  path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
                  path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(),
                       name='subscription_delete'),
              ] + router.urls
