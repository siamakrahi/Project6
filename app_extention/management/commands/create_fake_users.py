from django.core.management.base import BaseCommand
#from django.utils.crypto import get_random_string
from faker import Faker
from app_accounting.models import User

class Command(BaseCommand):
    help = 'Create 10 fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                password='asdf@1234',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                avatar=fake.image_url(),
                about=fake.text(),
                is_active=True,
                is_staff=False,
                is_superuser=False,
            )
            user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake users'))
