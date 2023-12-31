# Generated by Django 4.2.5 on 2023-09-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0014_remove_payments_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='оплачено'),
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_intent_id',
            field=models.CharField(default='NULL', max_length=100, verbose_name='id_платежа'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(choices=[('Безналичный', 'Безналичный'), ('Наличные', 'Наличные')], default='Наличные', max_length=20, verbose_name='Способ оплаты'),
        ),
    ]
