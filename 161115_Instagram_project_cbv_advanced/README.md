# 인스타그램 서비스 설계

## 새로운 로그인 뷰

**FBV**  
def login_fbv(request) 로 작성해주세요

- views.py에 View작성
	- pass처리 후 form - urls - view를 미리 연결 한 후 나중에 로직을 작성하세요
	- request.method == 'GET'일 경우, context에 form을 포함하여 render
	- request.method == 'POST'일 경우, form의 validation후 Login처리
- forms.py에 LoginForm(forms.Form) 작성
	- username, password필드 가짐
- urls모듈 생성, views모듈을 하위요소로 둠
	- urls/views.py
- View와 urls연결
- Template작성
	- member/login.html에 작성