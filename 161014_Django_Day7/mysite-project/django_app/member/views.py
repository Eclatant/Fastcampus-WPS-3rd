from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import \
    authenticate as auth_authenticate, \
    login as auth_login, \
    logout as auth_logout

# https://docs.djangoproject.com/en/1.10/
# topics/auth/default/#auth-web-requests


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


def logout(request):
    auth_logout(request)
    messages.info(request, '로그아웃 되었습니다')
    return redirect('blog:post_list')


def signup(request):
    """
    회원가입을 만들어주세요
    가입후에 message에 info tag로 '%s님 %s아이디로 회원가입 되었습니다'

    0. base.html에 signup링크 연결되는 a태그 구현 (로그인 안 되어있을 때만)
    1. views.py에 위 함수 추가 (빈 내용)
    2. urls.py에 연결 (signup/)
    3. 사용할 템플릿 구성 (form)
    4. form요소에 회원가입에 필요한 필드 구현 (email, password, nickname, last_name, first_name)
    5. views.py에서 POST요청을 받아 확인
        5-1.
    6. views.py에서 받은 값들을 사용해 MyUser모델 생성
    7. 생성 완료 후 해당 User로 로그인
    8. message.info(request, '메세지내용')으로 request에 메세지 전달
    9. 모든 과정 완료 후 'blog:post_list'로 redirect

    # Extra
    - Signup으로 오기 이전 URL로 redirect
    - login을 통해서 signup으로 온 경우에도 login이전에 있던 페이지로 redirect
    - MyUserManager의 create_user메서드를 사용
    - ModelForm을 사용, 또는 Form을 사용
    - form에 Bootstrap 클래스를 적용 (form-group, form-control)
    """

    if request.method == 'POST':
        # 전달받은 POST데이터를 가지고 회원가입을 진행
        pass
    else:
        # member/signup.html 파일을 render
        pass

    return redirect('blog:post_list')


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
