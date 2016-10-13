from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import \
    authenticate as auth_authenticate, \
    login as auth_login
# https://docs.djangoproject.com/en/1.10/
# topics/auth/default/#auth-web-requests


@csrf_exempt
def login(request):
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
            return HttpResponse('로그인 되었습니다')
        else:
            return HttpResponse('로그인에 실패하였습니다')
    else:
        pass






# def signUp(request):
#     # from IPython import embed; embed()
#     if not request.method == 'POST':
#         return render(request, 'dgirls/signup.html')
#     else :
#         userid = request.POST['userid']
#         passwd = request.POST['passwd']
#         email = request.POST['email']
#
#         if User.objects.get(userid=userid).exsits():
#             return redirect("dgirls:signup", {'msg': '존재하는 ID'})
#         else :
#             s = sha512()
#             s.update(SALT)
#             s.update(passwd.encode("ascii"))
#             user = User.objects.create(userid=userid, passwd=passwd, email=email)
#
#             auth_login(reqeust, user)
#
#             return render(request, 'dgirls/index.html')
