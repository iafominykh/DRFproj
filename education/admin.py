from django.contrib import admin

# Register your models here.
from education.models import Course, Lesson, Payments, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'description', 'author', 'price')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'description', 'link', 'course', 'author')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'lesson', 'payment_amount', 'payment_method')
    list_filter = ('user',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'status')