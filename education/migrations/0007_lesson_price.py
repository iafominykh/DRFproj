# Generated by Django 4.2.5 on 2023-09-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.IntegerField(default=5000, verbose_name='стоимость курса'),
        ),
    ]