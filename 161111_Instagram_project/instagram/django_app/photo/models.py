from django.db import models
from django.conf import settings


class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
