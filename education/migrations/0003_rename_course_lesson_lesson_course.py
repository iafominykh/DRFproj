# Generated by Django 4.2.5 on 2023-09-06 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_payments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='course_lesson',
            new_name='course',
        ),
    ]
