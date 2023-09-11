from django.contrib import admin

# Register your models here.
from education.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'description', 'author')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'description', 'link', 'course', 'author')
    