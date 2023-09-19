from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from education.models import Subscription, Course
from users.models import User


@shared_task
def send_email(course):
    subscribers_list = Subscription.objects.filter(course=course)
    course = Course.objects.get(id=course)
    for subscriber in subscribers_list:
        print('Отправлено сообщение об обновлении курса')
        send_mail(
            subject="Обновление курса!",
            message=f"У курса {course.title} обновление!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscriber.user.email]
        )


@shared_task
def check_user():
    now_date = timezone.now()
    one_month_ago = now_date - timedelta(days=30)
    inactive_user = User.objects.filter(last_login__lt=one_month_ago)
    inactive_user.update(is_active=False)
