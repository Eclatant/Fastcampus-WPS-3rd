###### Web Programming School  **[16.08.19]**

## Pre-Course (Day1)

### Pre-Course 목표
블로그 만들기


-

### 전체 목차
1. Cloud9 환경설정
2. 인터넷과 서버
3. 웹 프레임워크
5. Django의 MTV구조
6. Django Model
7. Django 관리자
7. Django View
8. Django Template
9. Django urls
10. Django ORM
11. View에서의 동적 데이터 전달
12. Django template tags
13. CSS, Bootstrap
14. Template extending
15. Template links
16. Django Form

-

### Cloud9 환경설정
+ c9.io 접속
+ Create a new workspace 선택

![NewWorkspace](Assets/c9_new_workspace.png)

-

+ 새 Workspace 생성

![CreateWorkspace](Assets/c9_django.png)

-

+ 세팅 완료

![SettingComplete](Assets/c9_setting_complete.png)

-

### 인터넷과 서버

인터넷으로 볼 수 있는 naver.com이나 google.co.kr과 같은 웹 사이트는 컴퓨터에 저장된 파일입니다

서버는 (일반적으로) 여러사람이 접속해도 무리없이 버텨낼 수 있는 컴퓨터를 뜻합니다

#### 웹 사이트는 아래와 같이 동작합니다

+ 웹 사이트가 동작할 기계 (물리적 서버)가 존재하며,
+ 해당 서버에서는 접속한 사용자들의 요청을 받습니다
+ 서버는 받은 요청에 대해서 적절한 응답을 돌려줍니다


-

### 웹 프레임워크

Django는 파이썬으로 만들어진 웹 애플리케이션 프레임워크(Web application framework)입니다

쉽고 빠르게 웹사이트를 개발할 수 있도록 도와주는 프레임워크이죠


#### 프레임워크는 왜 필요한가?

웹 사이트를 만들때에는 비슷한 유형의 요소들이 항상 필요합니다. 회원관리, 로그인 등의 사용자 기능이나 관리자 기능, 파일 업로드/다운로드 기능 등등...

같은 기능을 여러 개발자들이 똑같이 만드는 시간소모를 덜기 위해 웹 사이트 제작에 필요한 요소들을 미리 만들어서 모아놓은것이 프레임워크입니다


-


### Django의 MTV구조


Django는 개발자들의 편의와 유지보수의 용이성을 위해 Model-Template-View라는 패턴을 제공합니다

**Model**은 데이터베이스의 구조를 설정하는 컴포넌트이며,

**Template**은 사용자들에게 보이는 디자인 영역. 즉, HTML구조만을 모아놓은 컴포넌트입니다.

마지막으로 **View**는 **Model**의 데이터를 **Template**에 보여주는 역할을 합니다

-

### Django Model

블로그에 데이터를 저장할 모델을 생성해보겠습니다

그 전에, ```객체(Object)```에 관해 잠깐 설명하겠습니다

-

#### 객체

프로그래밍 개발 방법중 ```객체 지향 프로그래밍``` 이라 부르는 개념이 있습니다.

이 방법은 프로그램이 작동하는데에 특정 모델을 만들어 해당 모델이 어떤 역할과 성질을 가지는지 미리 정의하는 방식이라고 생각하시면 됩니다.

객체는 여기서 ```속성(properties)```과 ```행동(methods)```을 모아놓은 것입니다.


예를 들어, ```자동차(Cart)```라는 객체를 모델링 한다면, 아래와 같이 나타낼 수 있습니다

	자동차
	------------
	[속성(properties)]
	종류 (승용차, SUV, 스포츠카...)
	가격
	색상 (빨강, 노랑, 파랑, 검정...)
	
	[행동(methods)]
	시동걸기
	앞으로 가기
	멈추기
	클락션 울리기
	
	
객체지향이라는 개념은 현실에 존재하는 것을 속성과 행위로 분류해서 나타내는 것입니다

우리는 블로그를 만들 것이므로, 블로그에 등록되는 글(Post)를 객체로 나타내봅시다


	Post
	----------
	[properties]
	title
	content
	author
	created_date
	is_published
	
	[method]
	publish
	

is_published는 출판여부 (다른 사용자들이 읽을 수 있도록 출판된 상태인지)를 나타내며,

publish 메서드는 글을 출판상태로 만드는 행동입니다.

-

#### 애플리케이션 생성

fastcampus 프로젝트에 blog 애플리케이션을 추가해봅시다

	cd /home/ubuntu/workspace
	./manage.py startapp blog



![CreateApp](Assets/django_create_app.png)
왼쪽의 폴더목록에 ```blog```폴더가 생성됩니다	

-

#### settings.py에 해당 애플리케이션 사용 설정

```fastcampus/fastcampus/settings.py```의 ```INSTALLED_APPS```에 ```'blog'```를 추가해줍니다

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    )
    
-

#### 모델 작성

```blog/models.py```에 아래 내용을 추가합니다

	from __future__ import unicode_literals
	from django.db import models
	
	class Post(models.Model):
	    author = models.ForeignKey('auth.User')
	    title = models.CharField(max_length=200)
	    text = models.TextField()
	    created_date = models.DateTimeField(auto_now_add=True)
	    is_published = models.BooleanField(default=False)
	
	    def publish(self):
	        self.is_published = True
	        self.save()
	
	    def __unicode__(self):
	        return self.title
	        

-

#### 코드설명

+ ```class Post(models.Model)```은 모델을 정의하는 코드입니다

+ ```class```는 객체를 정의한다는 키워드입니다

+ ```Post```는 모델의 이름입니다. 클래스의 첫 글자는 대문자를 사용합니다

##### 속성을 정의할 때는, 각 속성이 어떤 성질을 가지고 있는지 구분합니다.

+ ```models.CharField```는 제한된 글자수의 텍스트를 정의할 때 사용합니다.

+ ```models.TextField```는 제한없는 글자수의 긴 텍스트를 정의합니다.

+ ```models.DateTimeField```는 날짜/시간을 위한 속성입니다.

+ ```models.ForeignKey```는 다른 모델에 대한 링크를 위한 속성입니다.

+ ```models.BooleanField```는 참/거짓 (True/False)를 정의하는 속성입니다.

##### 메서드

```def publish(self)```는 ```publish```라는 행동(메서드:method)입니다.

-

#### 데이터베이스 생성

명령어 입력

	./manage.py makemigrations
	./manage.py migrate
	
아래와 같은 메세지가 출력됩니다

	azelf:~/workspace $ ./manage.py makemigrations
	Migrations for 'blog':
	  0001_initial.py:
	    - Create model Post
	azelf:~/workspace $ ./manage.py migrate
	Operations to perform:
	  Apply all migrations: admin, blog, contenttypes, auth, sessions
	Running migrations:
	  Rendering model states... DONE
	  Applying contenttypes.0001_initial... OK
	  Applying auth.0001_initial... OK
	  Applying admin.0001_initial... OK
	  Applying admin.0002_logentry_remove_auto_add... OK
	  Applying contenttypes.0002_remove_content_type_name... OK
	  Applying auth.0002_alter_permission_name_max_length... OK
	  Applying auth.0003_alter_user_email_max_length... OK
	  Applying auth.0004_alter_user_username_opts... OK
	  Applying auth.0005_alter_user_last_login_null... OK
	  Applying auth.0006_require_contenttypes_0002... OK
	  Applying auth.0007_alter_validators_add_error_messages... OK
	  Applying blog.0001_initial... OK
	  Applying sessions.0001_initial... OK	

-

### Django 관리자

