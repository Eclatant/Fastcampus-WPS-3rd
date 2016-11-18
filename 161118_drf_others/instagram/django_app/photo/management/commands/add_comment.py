from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from photo.models import Photo, PhotoComment
from django.contrib.auth import get_user_model
User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        photo = Photo.objects.order_by('-created_date').first()
        content = 'Comment %s' % timezone.now()
        PhotoComment.objects.create(
            photo=photo,
            author=User.objects.first(),
            content=
        )