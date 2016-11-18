from django.core.management.base import BaseCommand, CommandError
from photo.models import Photo, PhotoComment


class Command(BaseCommand):
    def handle(self, *args, **options):
        photo = Photo.objects.order_by('-created_date').first()
