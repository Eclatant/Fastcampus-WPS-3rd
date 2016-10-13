from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=24, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

