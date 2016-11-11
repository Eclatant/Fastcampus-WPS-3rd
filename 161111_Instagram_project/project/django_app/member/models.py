from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    img_profile = models.ImageField(
        upload_to='user',
        blank=True
    )
    following_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Following',
        related_name='follower_users'
    )
    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_set_block'
    )

    def __str__(self):
        return self.get_full_name()

    def follow(self, user):
        instance, created = Following.objects.get_or_create(
            follower=self,
            followee=user
        )
        return instance

    def unfollow(self, user):
        Following.objects.filter(follower=self, followee=user).delete()


class Following(models.Model):
    follower = models.ForeignKey(MyUser, related_name='follower')
    followee = models.ForeignKey(MyUser, related_name='followee')
    created_date = models.DateTimeField(auto_now_add=True)