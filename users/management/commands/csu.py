from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='testovnet676@bk.ru',
            first_name='admin',
            last_name='A',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('Qq123123')
        user.save()