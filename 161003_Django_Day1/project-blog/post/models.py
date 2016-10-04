from django.db import models


# Post 클래스
# 데이터베이스에서 테이블이 됩니다

# 추후 추가 필드
#   해당 글을 본 유저 목록
class Post(models.Model):
    # 글 제목
    title = models.CharField(max_length=40)

    # 간단설명
    description = models.CharField(max_length=100, blank=True)

    # 본문내용
    content = models.TextField(blank=True)

    # 좋아요 수
    like_count = models.IntegerField(default=0)

    # 작성자의 IP주소
    ip_address = models.IPAddressField(blank=True)

    # 생성일자
    created = models.DateTimeField(auto_now_add=True)

    # 객체를 문자열로 표시
    def __str__(self):
        return self.title
