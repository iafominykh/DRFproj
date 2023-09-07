from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views import CourseViewSet, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    PaymentsListView, \
    PaymentsCreateView, LessonCreateAPIView, LessonListAPIView

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
                  path('payment/create/', PaymentsCreateView.as_view(), name='payment_create'),
              ] + router.urls
