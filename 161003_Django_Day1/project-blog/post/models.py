from django.db import models


# Post 클래스
# 데이터베이스에서 테이블이 됩니다
class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
