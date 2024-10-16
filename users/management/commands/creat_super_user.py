from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="grey-matter88@mail.ru",
            first_name="Yura",
            last_name="Sarvas",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("bgfEnU7vuV")
        user.save()


