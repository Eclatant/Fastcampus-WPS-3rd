from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class YoutubeUserManager(UserManager):
    pass


class YoutubeUser(AbstractUser):
    pass

