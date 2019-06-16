import hashlib
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, User
from django.contrib.auth.hashers import make_password

from store_api.models import Playlist


class Command(BaseCommand):
    help = 'Creating users.'
    algorithm = "pbkdf2_sha256"
    iterations = 12000
    digest = hashlib.sha256

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        User.objects.create(username='Admin', password=make_password("1234qwer"), is_superuser=True, is_staff=True)
        users = []
        users.append(User.objects.create(username='user1', password=make_password("1234qwer")))
        users.append(User.objects.create(username='user2', password=make_password("1234qwer")))
        users.append(User.objects.create(username='user3', password=make_password("1234qwer")))

        content_type = ContentType.objects.get_for_model(Playlist)
        permissions = list(Permission.objects.filter(
            content_type=content_type
        ).all())
        for user in users:
            user.user_permissions.set(permissions)
