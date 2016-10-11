# Django girls

튜토리얼 진행해주세요

-

# 로그인/로그아웃 구현

[Using the Django authentication system - Auth web requests](https://docs.djangoproject.com/en/1.10/topics/auth/default/#auth-web-requests)  

**authenticate**  
username, password를 받아 인증에 성공할 경우 User객체를 리턴 (실패시 None리턴)

**login**  
request, user를 받아 해당 user를 전달받은 request환경에서 로그인이 유지되도록 함

-

### View 작성

```python

```
`member/urls.py`

```
from django.conf.urls import url
from .views import login

urlpatterns = [
    url(r'^login/$', login, name='login'),
]
```

