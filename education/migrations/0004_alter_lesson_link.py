# Generated by Django 4.2.5 on 2023-09-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_rename_course_lesson_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='ссылка на видео'),
        ),
    ]
