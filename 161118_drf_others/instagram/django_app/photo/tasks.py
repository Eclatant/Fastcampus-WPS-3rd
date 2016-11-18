from celery import shared_task
from .models import Photo, PhotoComment
from django.contrib.auth import get_user_model
User = get_user_model()


@shared_task
def photo_add_after(photo):
    print('photo_add_after start')
    PhotoComment.objects.create(
        photo=photo,
        author=User.objects.first(),
        content='등록되었습니다',
    )
    print('photo_add_after end')