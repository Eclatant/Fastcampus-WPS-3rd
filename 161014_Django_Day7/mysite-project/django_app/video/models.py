from django.db import models


class Channel(models.Model):
    youtube_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)


class Video(models.Model):
    youtube_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    published_date = models.DateTimeField()
