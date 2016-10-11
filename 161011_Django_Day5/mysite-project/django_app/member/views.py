from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import \
    authenticate as auth_authenticate, \
    login as auth_login
# https://docs.djangoproject.com/en/1.10/
# topics/auth/default/#auth-web-requests


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth_authenticate(
        username=username,
        password=password
    )

    if user is not None:
        auth_login(request, user)
        return HttpResponse('로그인 되었습니다')
    else:
        return HttpResponse('로그인에 실패하였습니다')