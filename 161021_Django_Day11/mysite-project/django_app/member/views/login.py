from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login

__all__ = [
    'login',
    'login_facebook',
]


def login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('username 또는 password는 필수항목입니다')
        user = auth_authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인에 성공하였습니다')
            return redirect(next)
        else:
            messages.error(request, '로그인에 실패하였습니다')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})


def login_facebook(request):
    if request.GET.get('error'):
        messages.error(request, '사용자가 페이스북 로그인을 취소했습니다')
        return redirect('member:login')

    if request.GET.get('code'):
        REDIRECT_URL = 'http://127.0.0.1:8000/member/login/facebook/'
        # authenticate backends에 FacebookBackend추가해서 dict_user_info객체로 로그인 가능
        user = auth_authenticate(user_info=dict_user_info)
        if user is not None:
            auth_login(request, user)
            messages.success(request, '페이스북 유저로 로그인 되었습니다')
            return redirect('blog:post_list')
        else:
            messages.error(request, '페이스북 로그인에 실패하였습니다')
            return redirect('member:login')

