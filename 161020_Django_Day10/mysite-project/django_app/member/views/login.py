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
        from django.conf import settings
        import requests
        import json
        APP_ID = settings.FACEBOOK_APP_ID
        SECRET_CODE = settings.FACEBOOK_SECRET_CODE
        REDIRECT_URL = 'http://127.0.0.1:8000/member/login/facebook/'

        code = request.GET.get('code')
        print('code : %s' % code)
        # return HttpResponse

        url_request_access_token = 'https://graph.facebook.com/v2.8/oauth/access_token?' \
                                   'client_id={client_id}&' \
                                   'redirect_uri={redirect_uri}&' \
                                   'client_secret={client_secret}&' \
                                   'code={code}'.format(
                                        client_id=APP_ID,
                                        redirect_uri=REDIRECT_URL,
                                        client_secret=SECRET_CODE,
                                        code=code
                                    )
        r = requests.get(url_request_access_token)
        dict_access_token = r.json()
        print(json.dumps(dict_access_token, indent=2))
