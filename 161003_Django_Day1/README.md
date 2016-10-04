# pyenv

pyenv는 프로젝트별로 파이썬 버전을 따로 관리할 수 있도록 도와주는 라이브러리입니다.  
여러 프로젝트를 동시에 진행하다보면, 어떤 프로젝트에서는 2.7을, 어떤 프로젝트에서는 3.4를 사용하는 식으로 다양한 버전의 사용할 수도 있고, 각각에 설치된 라이브러리간 충돌이 일어날 수도 있습니다.

# virtualenv

virtualenv는 파이썬 개발환경을 프로젝트별로 분리해서 관리할 수 있게 해주는 라이브러리입니다.  
위의 pyenv와 다른점은, pyenv는 **파이썬**의 버전을 관리해주는 것이며, virtualenv는 **파이썬 패키지 설치 환경**을 따로 관리해줍니다.

# pyenv-virtualenv

위의 pyenv제작자가, pyenv를 사용할 경우 쉽게 virtualenv를 사용할 수 있도록 만든 라이브러리입니다.

-

# pyenv install

* 맥  
`brew install pyenv`  
`brew install pyenv-virtualenv`

* 리눅스  
<https://github.com/yyuu/pyenv-installer>  

`curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`

* 설치 후 pyenv관련 설정을 shell설정에 추가  
	* 맥 `vi ~/.bash_profile`
	* 리눅스 	`vi ~/.bashrc`


> 맥
> 
```
export PYENV_ROOT=/usr/local/var/pyenv
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
```

> 리눅스
> 
```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```



#### 파이썬 3.4.3버전 설치  

`pyenv install 3.4.3`


#### 가상환경 생성

`pyenv virtualenv <version> <env name>`

#### 사용할 폴더로 이동
`cd projects/django/blog`

#### local에 가상환경 지정
`pyenv local 3.4.3 fc-blog`



-

#### vi 단축키

`shift + g` : 가장 아래로  
`shift + a` : 현재 줄에서 가장 마지막으로



# Django

### MTV Structure

Django는 소프트웨어 공학에서 사용되는 MVC(Model-View-Controller)패턴과 유사한, Model-Template-View(MTV)패턴을 사용합니다.

-

#### MVC패턴에서 각 요소의 역할

* Model

	* 데이터베이스의 테이블에 대응
	* 전체 데이터의 구조를 결정

* View
	* 클라이언트에 보여지는 부분을 담당
	* HTML/CSS/JavaScript

* Controller
	* 사용자의 요청에 따라 Model에서 데이터를 얻어와서 View에 전달하는 역할

-
 
#### Django의 MTV패턴에 매칭되는 각 MVC요소

* MVC의 Model -> MTV의 Model
* MVC의 View -> MTV의 Template
* MVC의 Controller -> MTV의 View

> MVC의 View와 MTV의 View를 헷갈리지 않도록 주의합니다.  
> MVC의 View는 사용자가 보는 부분이며, MTV에서의 View는 실제로는 Controller의 역할을 합니다.

-

#### Model (models.py)

Model은 데이터베이스의 테이블의 형태를 정의합니다. Django에서는 ORM(Object Relation Mapping)이라는 기법을 사용해서 데이터베이스를 다루며, 이 때 Model에 정의한 클래스 객체의 형태를 사용합니다.

Model의 내용이 변경되거나, 새로운 테이블을 만들 경우 실제 데이터베이스에 변경사항을 반영해야합니다.  
예전에는 south라는 서드파티 라이브러리를 사용했지만, 1.7버전부터는 내장기능으로 편입되어 `manage.py`에서 쉽게 실행할 수 있습니다.

#### View (views.py)

View는 Model과 Template을 연결하는 로직을 담당합니다.  
뷰는 함수형 뷰(Function-based view)와 클래스형 뷰(Class-based view), 두 형태로 사용 가능하며, 어느쪽으로 작성하든 상관없습니다. 다만, 간단하고 일반적인 형태의 뷰는 장고가 제공하는 제네릭 뷰를 사용할 수 있으며, 또한 재활용면에서도 클래스형 뷰가 좀 더 유리합니다.  
처음에는 뷰의 동작을 알기 위해 FBV를 사용해서 시작하고, 이후 뷰에 대해 이해가 쌓이면 CBV로 진행할 예정입니다.

#### Template (templates폴더)

프로젝트 설정파일에 지정하며, 템플릿 파일들을 모아놓는 폴더 역할을 합니다.  
일반적으로는 프로젝트 디렉토리 바로 안쪽에 위치합니다.


#### URLConf (urls.py)

URLConf는 Django로 들어온 URL요청을 View와 매핑해주는 `urls.py`파일을 말합니다. 반드시 하나의 파일에 정의할 필요는 없으며, 여러 파일에 정의하고 프로젝트의 메인 URLConf에 불러와서 사용할 수 있습니다.

-

#### 프로젝트 설정 (settings.py)

기본적인 사항은 장고가 자동으로 생성해주며, 필요한 부분만 등록해서 사용합니다.  
아래는 프로젝트에 맞춰 일반적으로 설정해야하는 항목들입니다.

* Database설정
* Template 디렉토리 설정
* Static 디렉토리 및 URL 설정
* Application(app) 등록
* Timezone, Locale 등록

-

