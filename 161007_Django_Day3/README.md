# 파이썬 셸 관련 설정

## 셸에서 방향키 누르면 특수문자 나오며 인식되지 않을 때

### 맥

기존에 있던 파이썬 버전 삭제

```
pyenv uninstall 3.4.3
```

관련 유틸리티 설치 (readline, xz)

```
brew install readline xz
```

파이썬 재설치

```
pyenv install 3.4.3
```

3.4.3 하위로 존재하던 가상환경 재설치

```
pyenv virtualenv 3.4.3 <가상환경이름>
```

## 기본 셸 변경

### zsh<http://theyearlyprophet.com/love-your-terminal.html>  
bash와 비슷하게 동작하는 셸로, 사용성이 좋습니다.

#### 리눅스

```
sudo apt-get install zsh
curl -L http://install.ohmyz.sh | sh
chsh -s `which zsh`
```

#### 맥

```
brew install zsh zsh-completions
curl -L http://install.ohmyz.sh | sh
```

> **확인법**  
> echo $SHELL

## 리눅스 기본 터미널 변경

**Terminator**

```
sudo add-apt-repository ppa:gnome-terminator
sudo apt-get update
sudo apt-get install terminator
```

-

# 관계형 데이터베이스

> 데이터를 엑셀의 시트 형태로 저장합니다.  
> 서로 다른 분류의 데이터는 시트간의 관계로 연결할 수 있습니다.

데이터베이스의 테이블 = 엑셀 시트

-

### 간단한 관계형 데이터베이스 모델

**소속사 테이블**

ID | 소속사명
--- | ---
1 | 로엔 엔터테인먼트
2 | 피데스 스타티윰
3 | JYP 엔터테인먼트
4 | 드림티엔터테인먼트

**그룹정보 테이블**

ID | 그룹명
--- | ---
2 | 걸스데이
3 | missA


**연예인 목록 테이블**

ID | 소속사ID | 그룹ID | 이름 | 출생연도
--- | --- | --- | --- | ---
1 | 2 | NULL | 박보영 | 1990
2 | 3 | 2 | 민아 | 1993
3 | 1 | NULL | 아이유 | 1993
4 | 4 | 3 | 수지 | 1994
5 | 3 | 2 | 혜리 | 1994
