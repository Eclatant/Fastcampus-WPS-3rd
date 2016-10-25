from django.db import models
from django.conf import settings
from member.models import MyUser as User
"""
Album
    title : CharField
    owner : ForeignKey
    description : CharField

Photo
    Album : ForeignKey
    owner : ForeignKey
    title : CharField
    description : CharField
    img : ImageField

Photo좋아요를 구현하고싶으면 어떻게해야될까요?
좋아요에는 해당 Photo, User, 좋아요누른시간이 기록됩니다
"""


class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=80, blank=True)


class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True)
    img = models.ImageField(upload_to='photo')
