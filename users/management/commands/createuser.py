from django.core.management import BaseCommand

from users.models import User, UserRoles


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='t@t.com',
            first_name='Alesha',
            last_name='lol',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        user.set_password('Aa111111')
        user.save()