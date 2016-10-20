from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
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

        code = request.GET.get('code')
        print('code : %s' % code)
        ret = 'Code receive success : %s' % code
        return HttpResponse(ret)

        url_request_access_token = 'https://graph.facebook.com/v2.8/oauth/access_token?' \
                                   'client_id={cliend_id}&' \
                                   'redirect_uri={redirect_uri}&' \
                                   'client_secret={client_secret}&' \
                                   'code={code}'.format(
            cliend_id=APP_ID,
            redirect_uri=URL_LOGIN_FACEBOOK,
            client_secret=SECRET_ID,
            code=code
        )
