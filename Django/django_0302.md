# Django 01

## Web Framework

### Static web page(정적 웹 페이지)

미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

서버가 클라이언트로부터 웹 페이지에 대한 요청을 받았을 경우 추가적인 처리없이 클라이언트에게 응답을 보냄! 

모든 상황에서 모든 사용자에게 동일한 정보를 표시 -> 이게 정적 웹페이지의 특징!

html, css, javascript가 사용됨

flat page라고도 함



클라이언트 서버 요청 응답

클라이언트: 응용 프로그램 -> 웹 브라우저(크롬)

서버 이 서버를 구축하는게 django 

www.naver.com 이 url을 통해 네이버 서버에게 요청을 보냄 "네이버의 메인 페이지를 줘!"

네이버의 메인 페이지 (html)를 클라이언트에게 넘겨서 브라우저가 이를 해석해서 우리가 네이버의 메인 페이지를 볼 수 있음



### Dynamic web page(동적 웹 페이지)

웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄

방문자와 상호작용해서 페이지 내용은 그때그때 다름

서버 사이드 프로그래밍  언어(python, java, c,  c++)가 사용됨

파일 처리, 데이터베이스와의 상호작용이 이루어져 수정, 삭제 등이 일어남



### Framework

웹 서비스를 만드는데 필요한 도구들의 모임!!

웹 페이지를 개발하는 여러 라이브러리, 모듈이 들어가있음

서버를 개발하는데 있어서 많은 기능이 필요한데 온전히 개발에 집중하기 위해서 모든걸 제로부터 작성하지 않아도 됨 framework가 일종의 환경, 툴을 지원하니까! 

HTML, CSS, JS, DB, 서버, 보안 등등의 기능들을 우리가 배운 파이썬으로 구현할 수 있음

-> 클래스, 라이브러리, 재사용할 수 있는 수많은 코드

django는 이걸 다 제공 해준대!!!



### Web framework

웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는것이 목적

웹 페이지, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어짐



### Django를 사용해야 하는 이유

검증된 python 언어 기반 web framework

대규모 서비스에 안정적, 세계적인 기업들에 의해 사용됨

ex. Spotify, Instagram, Dropbox, Delibery Hero



### Framework Architecture

MVC Design Pattern(model-view-controller)

소프트웨어 공학에서 사용되는 디자인 패턴 중 하나

사용자 인터페이스로부터 프로그램 로직을 분리해 어플리케이션의 시각적인 부분과 뒷쪽에서 실행되는 부분을 서로 영향 없이 개발할 수 있음

Django는 MTV Pattern이라고 함



### MTV Pattern

- Model = DB(데이터 관련)

데이터베이스를 다룸(추가, 수정, 삭제)

- Template = HTML  (눈에보이는거, 웹페이지)

파일의 구조, 레이아웃을 정의

실제 내용을 보여주는데 사용

- View(Controller) = 조작, 가공  @가장 중요한 역할! 컨트롤 타워의 역할

HTTP요청을 수신하고 응답을 반환

Model과의 소통 진행 -> model을 통해 요청을 충족시키는데 필요한 데이터에 접근?

template에게 응답의 서식 설정을 맡김

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-18%20133524.jpg" alt="MTV Pattern1" style="zoom: 67%;" />



MTV Pattern의 흐름 알기!!

모델을 먼저 정의하고 이 모델을 view에서 가져와서 조작하고 이걸 처리해서 template에 넣어주세요 라는 흐름으로 전개됨

![MTV Pattern2](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-18%20133548.jpg)





## Django Intro

1.가상환경 생성 및 활성화

2.django 설치

3.프로젝트 생성

4.서버 켜서 로켓 확인

5.앱 생성

6.앱 등록



### 프로젝트 구조

\__init__.py  python에게 하나의 패키지로 인식하도록 하는 것(수정ㄴㄴ)

asig.py (애스기) 비동기식 웹사이트를 배포할 때 사용하는 파일(수정ㄴㄴ)

settings.py 애플리케이션의 모든 설정을 포함함

urls.py 사이트의 url과 적절한 views의 연결을 지정

wsgi.py (위스기) 웹 서버를 배포할 때 도움을줌(수정ㄴㄴ)

manage.py 커맨드라인 유틸리티(수정ㄴㄴ)



application 생성

application명은 복수형으로 하는것을 권장함



### 어플리케이션 구조

admin.py 관리자용 페이지를 설정 하는 곳

apps.py 앱의 정보가 작성된 곳(수정ㄴㄴ)

models.py 앱에서 사용하는 model을 정의하는 곳

tests.py 프로젝트의 테스트 코드를 작성하는 곳(수정ㄴㄴ)

views.py view 함수들이 정의 되는 곳 

 

### Project / Application

- Project

project는 application의 집합

하나의 프로젝트가 여러개의 app을 갖는 구조

포르젝트에는 여러 앱이 포함될 수 있음

앱은 여러 프로젝트에 있을 수 있지만 여기까지 커지지는 않음

- application

기능을 분리해서 만들고 싶을때 생성하면 됨

멀티앱을 만들 필요가 있는가에 대한 의견은 분분함  -> 일단은 싱글앱으로 개발하고 서비스가 커지면 그때 가서 분리해도 괜찮음

실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당

일반적으로 앱은 하나의 역할 및 기능 단위로 작성함

articles : 게시판을 만드니까 이름을 articles로 했음



settings.py의 INSTALLED_APPS 리스트에 앱을 적어줘야함

장고 프로젝트는 아직 이 앱이 생성된 것을 모르기 때문에 프로젝트에 등록하는 과정이 필요함!

*앱 생성시 주의 사항

반드시 생성 후 등록해야함!! 생성 후 등록!!! 생성 후 등록!!!!!!!!!!!!!!!!!!!!

INSTALLED_APPS에 먼저 등록하고 생성하려면 앱이 생성되지 않음

*앱 등록시 주의 사항

맨 위에 작성하는 이유는? 

순서를 지키지 않아도 문제는 없지만 추후 advanced한 내용을 대비하기 위해 지키는 것을 권장

Local apps -> Third party apps -> Django apps

![installed_apps](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-18%20144830.jpg)





## 요청과 응답

### URLs

HTTP 요청(request)을 알맞은 view로 전달

urlpatterns안의 path('admin/',~) 은 url 주소의 일부분을 뜻함

8000/admin 하면 로그인 페이지 즉, 관리자 페이지에 들어가짐

장고는 admin 페이지가 기본적으로 만들어져 있음

장고 서버의 urls.py가 클라이언트로부터 ~/admin/ 주소를 받아서 이 문자열 admin과 매칭되는 path 함수를 호출해줌 호출이 되면 admin.site.urls 두번째 인자가 페이지가 되거나 역할을 함 

우리가 주소창에 url을 치는 행위는 서버에게 요청을 보내는 행위! 



이어서  path 함수를 만들어 줌

index/ 여기서 '/'가 붙음 -> 장고에서는 이걸 앤드 슬래시라고 하고 꼭 써줘야 함

아까 우리가 admin 페이지에 들어갈 때 뒤에 /를 붙이지 않아도 들어가졌음 접속할 때는 앤드 슬래시를 쓰지 않아도 접속이 가능함 하지만 urls.py에 쓸때는 반드시 써줘야해!(실제로 빼먹어서 에러가 많이 났다..ㅎ)

두번째 인자는  index 페이지에 관한 요청이 왔을 때 메인 페이지로 index 페이지를 보여줘야함 

메인 페이지 = Template  template를 불러올 수 있는 친구는 view!  

url에서 해당되는 view 함수를 연결해줘야함 view 함수는 프로젝트가 아닌 앱에 있음 views.py 는 일종의 모듈 얘를  import 해와야 함

from articles import views

views.함수이름(아직은 함수가 없음)



클라이언트는 서버에게 /index/ 주소로 요청을 보냄

urls.py는 어!  index 주소로 요청이 왔다! 메인 페이지 보여줄 수 있는 view 함수 호출 되어야해!

views.py에는 메인 페이지를 보여주는 어떠한 함수가 있음 이 함수는 template을 준비해서 응답을 줌



cf. urlpatterns의 리스트 안에 요소가 하나밖에 없는데도 콤마가 있음 왜?

Django에서는 trailing comma를 작성하도록 권장함 -> 생산성을 높이기 위해서(이후에 엔터치고 바로 작성할 수 있도록!) settings.py에도 trailing comma가 있음

python에서는 요소 하나만 썼음!



views.py로 이동

index로 요청이 왔으니까 함수 이름을 맞춰줌 

view 함수가 무조건 받아야하는 인자! request

def index(reauest):    -> HTTP request 객체 아까 요청 받은 객체가 함수로 넘어옴 이 요청 객체(request) 안에 클라이언트가 보낸 모든 정보들이 다 들어있음 이 안의 정보들을 view함수가 사용함 

request 안쓰면 에러남! 첫번째 필수 인자야!!!

함수니까 return을 해 무엇을? 메인페이지를! 

위에 보면 기본적으로 랜더링 되어있음  import render라고 적혀있음 -> 함수가 랜더링 되어있는것

return render(request, 'index.html') 

render 함수도 첫번째 인자로 request가 들어감 아까 request함수를 받은 것 그냥 이건 약속이야!

두번째 인자로 템플릿 경로가 들어감

이 함수는 urls.py가 호출했을 때 템플릿을 랜더링하는 역할을 함

랜더링은 무언가를 만들어서 준다는 의미 템플릿을 랜더링해서 리턴함



urls.py로 가서 함수이름을 마저 적어줌



template은 장고가 자동으로 만들어 주지 않음 

앱 안에 templates라는디렉토리를 만들어 주고  html 파일을 만들어 줌(이것도 약속!)

웹엑스 시간에는 index(app)/templates/index/index.html 과 같은 샌드위치 구조로 만들어 줬음!





Language Code

django를 사용하는 사용자에게 제공하는 언어를 설정함 번역을 해줌

기본값이 영어로 되어있어서 한글로도 바꿀 수 있음

대문자로 써도 인식은 하지만 소분자로 쓰는게 좋음

TIME_ZONE

서버 시간을 바꿀 수 있음

USE_I18N

internationalization을 줄인 것 i와n의 사이에 18개의 글자가 있음

국제화, 번역 시스템을 활성화할 것 인가

USE_L10N

localization을 줄인 것 l과 n 사이에 10개의 글자가 있음

지역화,  데이터의 지역화된 형식을 지정을 하는 것(우리가 별도로 수정하지는 않음)

USE_TZ

timezone, 기본적으로 우리가 쓰는 이 시간대를 인식할 것 인가

얘네가 True로 되어 이기 때문에 languate code와 time zone을 사용할 수 있음





## Template

### Django Template

데이터 표현을 제어하는 도구, 표현에 관련된 로직

즉, 무언가를 표현하는 것, 보여주는 것!

built-in system

Django template language가 존재함(프로그래밍 언어는 아니고 별도의 문법)

-> DTL



### DTL 

Django template에서 사용하는 built-in template system

조건, 반복, 변수, 치환, 필터 등의 기능을 제공

python이 HTML에 포함 된 것 아님

python처럼 if, for가 있는데 이름만 맞춘것 뿐!

프로그래밍적 로직이 아니라 프레젠테이션(화면)을 표현하기 위한 것!!!



### DTL Syntax

 1.Variable

양쪽에 중괄호 2개 그안에 변수를 쓰고 render() 함수를 통해 views.py에서 정의한변수를 template에 보냄

변수명은 영어, 숫자, 밑줄의 조합으로 구성될 수 있음, 밑줄로 시작 못함, 공백, 구두점 문자도 사용 못함

dot(.) 을 사용해서 변수 속성에 접근할 수 있음 

render의 세번째 인자로 {'key': value}와 같은 딕셔너리 형태로 넘겨줌

key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨  

->  딕셔너리는 key로 접근해서 value(값)을 사용하니까!

2.Filters

변수 뒤쪽에 사용, 변수를 수정할 때 사용

lower 문자열을 소문자로 바꿔줌 

length 길이를 재줌

join:', '  콜론 뒤에 작성해줌 

chained, 변수 뒤에 필터 쓰고 또 필터 쓰는 등 필터끼리 연결이 가능하고  join 처럼 일부 필터는 인자를 받기도 함

3.Tags @이게 젤 중요함!

중괄호와 %로 되어있음

반복 또는 논리 연산을 수행 함

변수보다 복잡한 일들으 수행 함

일부 태그는 시작 태그와 종료 태그가 필요함 마치 html 처럼!

4.Comments

주석

한 줄짜리 주석은 중괄호, #

여러줄 주석은 컨트롤+슬래쉬하면 comment태그가 등장함 닫는 태그 end comment가 있음



다시 실습으로 돌아와서 새로운 페이지를 만들어보자!

project의 urls.py에서 새로운 페이지를 요청을 받을 수 있는 url을 새로 만들어줌

path('greetings/')

첫번째 인자 주소이름, 앤드 슬래쉬 빼먹지 말고! 

두번째 인자 클라이언트가 greeting이라는 주소로 요청을 보냈을 때 어떤 view함수를 호출 할 것인지

view로 넘어와서 greeting 함수 정의해줌 트래일링 콤마 잊지말기! views.greeting() 괄호 쓰지 말기! 

인자 request는 고정!

return render

랜더링을 할거야  첫번째 인자는 request 두번째 인자 어떤 template을 랜더링 할 것인지

greeting.html template를 만들어줌

python manage.py runserver로 서버를 켜고 들어가면 page not found가 뜸

-> 왜냐면 지금 이 주소는 없으니까!

 "나는 지금 이 url을 찾을 수 없는데 나한테 작성된 url conference가 이 세개가 있어!" 라고 알려줌

urlpatterns와 일치함

변수화 하고싶어!

greeting 함수의 세번째 인자에 딕셔너리 형태의 변수 값을 넘겨줌

{name: 'Alice', } 여기서도 트레일링 콤마 잊지말기!

Alice라는 값을 쓰려면 key인 name으로 접근해야함

template에 돌아와서 {{ name }}  중괄호 열고닫고 사이에 공백 한칸씩 넣어주기



지금은 변수가 하나라서 상관없지만 변수가 늘어나면 세번째 인자에 다 적어주면 불편해..

그래서 위쪽으로 별도로 빼서 context라는 딕셔너리를 만들어주고 변수를 이동시켜줌

세번째 인자에는 context만 쓰면됨

리스트랑 딕셔너리를 추가로 만들면 이것또한 context에 딕셔너리 형태로 넣어주면 됨

장고에서는 일반적으로 key, value의 이름을 맞춰줌 왼쪽의 key값으로 접근해야 함!(잊지말자,,)

template에 돌아와서 변수를 바꿔줌

dot(.)를 사용해줌 info 딕셔너리(변수)의 name key값 그럼 Alice가 출력됨

{{ foods }} 는 리스트가 그대로 출력됨 첫번째만 출력하고 싶다면 인덱스로 접근해주면 됨



또 새로운 페이지 만들기!

urls.py에 dinner path 작성해주기

views.py에서 함수 정의해주기

리스트를 만들어주고 랜덤 모듈을 사용해줘야 하니까 위에서 import random 불러옴

choice를 랜덤으로 하나 뽑음

요청을 보낼 때마다 view함수가  새로 실행되면서 random이 새로운 것을 choice 함

 ul 태그로 안에서 리스트를 반복해주고 for 태그를 만들어 줌

for 태그는 파이썬에서의 for i in range 형태와 비슷하고 반드시 end for가 있어야 함

for 태그 안에 li 를 반복해줌

변수 태그도 쓰고 template 태그도 써주는데.. 

여기서 주의할건 변수 태그는 중괄호,%로 열고 닫히고 template 태그는 중괄호 두개!

 

DTL에서는 괄호가 없음!

for 태그

forloop.counter idx1부터 

forloop.counter0 idx0부터

 리스트가 비었다면 이걸 출력해!

if 태그

for태그도 if 태그도 둘다 닫는 태그가 존재함!

forloop.first 첫바퀴일때만 이걸 출력하고 나머지는 이걸 출력해

length 필터

부등호도 쓸 수 있음

lorem ipsum

3 w 세 단어가 나옴

4 w random 네 단어가 나오는데 랜덤으로 나옴

2 p 2개의 paragraph가 나옴

연산자

DTL에서는  연산자 add만 있음

now 태그

날짜,시간을 출력

지금 여기서 한국어와 한국시간이 나오는건 아까 settings.py에서 language code랑 utc를 설정해줬기 때문에!



### 템플릿 상속

템플릿 상속을 사용하면 사이트의 공통 요소를 포함하고 하위 템플릿에서 재정의(override)할 수 있음

-> 부모 템플릿 base.html을 만들어주고 여기에 bootstrap cdn을 적용시켜줌

base.html은 상위이기 때문에 app의 templates가 아닌 다른곳에 만들어 주고 싶음 그래서 최상단에 templates를 만들어 주고 여기 안에 base.html을 넣어줌  이 위치는 앱과 프로젝트와 동등한 위치에 있고 이 위치는 장고는 아직 모르기 때문에 장고한테 추가 템플릿 경로를 등록해야함! 

-> settings.py의  TEMPLATES의 빈 리스트 DIRS에 추가 경로를 등록해줌

base.html 파일의 body 안에 block을 넣어주고 block의 이름을 설정해줌! 이 block은 content로!

nav태그들이 길기도 하고 만들다보면 base.html파일의 내용도 커질 수 있음

좀 더 간편하게 nav를 수정하기 위해서 app의 templates 디렉토리에  nav.html을  만들어서 옮겨올 수 있음

base에서 include 태그를 사용해서 nav를 로드하면 됨 -> 코드가 깔끔해지고 네비게이션을 수정할 때도 간단함!



{% extends '부모 템플릿 이름'  %} 

자식 템플릿이 부모 템플릿을 확장한다는 것

최상단에 작성 되어야 함

{% block content %} {% end block %}

닫는 태그가 있음

하위 템플릿에서 재지정할 수 있는 블록을 정의

부모들이 만들어 놓은 블록을 자식들이 가져와 재정의함

{% include '' %}

템플릿을 로드하고 현재 페이지로 렌더링함

템플릿 내에 다른 템플릿을 포함(including)하는 방법



### Django 설계 철학

1.표현과 로직을 분리함

표현은 template 로직은 view 

템플릿은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐! 그냥 잘 보여주기만 하면 돼!

ex. 템플릿에서는 연산 불가능함

즉, 이런 기본 목표를 넘어서는 기능을 지원하지 말아야 함

2.중복을 배제함 -> 상속

대다수의 동적 웹사이트는 공통의 header, footer, navbar 같은 공통 디자인을 가지는데 django 템플릿 시스템은 이러한  요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 하고 상속을 함!



코드의 작성 순서

URL  -> View -> Template



트레일링슬레쉬

모든 views는 함수형태로 적음



ip는 컴퓨터의 주소

port는 이 컴퓨터랑 프로그램이 소통하는 창구

나는 1270.0.0.1이랑은 컴퓨터랑 8000번이라는 창구에서 소통할거야!

장고는 port번호를 따로 명시하지 않으면 그냥 8000번을 사용함



include 다른 html 코드를 가져와서 여기에 쓰겠다!



## HTML Form

### HTML form element

서버에 데이터를 제출하기 위한 요소

사용자 정보를 입력하는 여러 방식을 제공

핵심 속성(attribute)

- action: 입력 데이터가 전송될 URL 지정
- method: 입력 데이터 전달 방식 지정

get 어떤 데이터를 그냥 달라고할 때

post 내가 글을 작성하거나 회원가입을 하거나 뭔가 데이터를 저장, 쓸 때 (semantic tag같음 의미론적임)



### HTML input element

사용자로부터 데이터를 입력 받기 위한 요소

type에 따라서 어떻게 입력받을지 달라짐

핵심 속성(attribute)

- name: 데이터를 서버에 전송할 때 어떤 데이터인지 명시해주는것 

서버에 전달하는 파라미터는 딕셔너리형태인데 key에는 name이 value에는 사용자가 입력한 값이 들어감

서버가 데이터에 접근할 때 name으로 접근함 -> 이름 주세요 주소 주세요!

GET 방식은 url로 데이터를 넘겨줌(Post와의 차이점!)

![method_get](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20153914.jpg)



### HTML label element

input에 대한 설명을 나타냄, input값의 이름표

label을 input 요소와 연결

-> input에 id 속성 부여, label에 input의 id와 동일한 값의 for 속성 부여

-> 화면 리더기에서 label을 읽어 사용자가 입력해야하는 텍스트가 무엇인지 이해할 수 있도록 도움, label을 클릭해서 input에 초점을 맞추거나 활성화 시킬 수 있음 id의 텍스트를 누르면 옆에 있는 text field에 커서가 위치됨!



### HTML for attribute

button, input(not hideen type), select, textarea...



### HTML id attribute

must be unique해야 하는 식별자 정의

linking, scripting, styling 시 요소를 식별



### HTTP

Hyper Text Transfer Protocol

hyper text를 주고받는 하나의 약속 -> 어떻게 문서에 대한 데이터 교환을 할 것인가에 대한 약속

이 protocol로 주고 받을거야!  www야 이 웹사이트를 줄래?

HTTP request method의 종류

GET, POST, PUT, DELETE ... 

put 서버로부터 어떤 정보를 수정하는구나

delete 서버로부터 어떤 정보를 삭제하는구나



### HTTP request method - GET

서버로부터 정보를 조회하는데 사용, 데이터를 가져올 때만 사용해야 함

데이터를 서버로 전송할 때 body가 아닌 query string parameters를 통해 전송

url에다 ?key value 형태

반면, POST는 url에 담지않고 body라는 영역에 데이터를 한겹 숨겨서 전송



## URL

### Variable Routing

URL 주소를 변수로 사용하는 것

URL 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

-> 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20170406.jpg" alt="variable routing" style="zoom: 80%;" />



### URL Path converters

- str

  '/' 를 제외한 모든 문자열과 매치

  작성하지 않으면 기본 값

  

- int

  0 or 양의 정수와 매치

  

- slug

  ASCII 문자 or 숫자, 하이픈 및 밎줄 문자로 구성된 모든 슬러그 문자열과 매치

  ex. building-your-1st-djanog-site

  

![variable routing2](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20170652.jpg)



view 함수에 인자로 넘겨줘야함!!



### App URL mapping

app의 view 함수가 많아지면 path()도 많아져서 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 있어 비효율적

-> 각 app에 urls.py를 작성!

1. app안에 urls.py 만들기
2. 프로젝트 urls.py에서 각 앱의 urls.py 파일로URL 매핑 위탁
3. 현재 디렉토리 안에서 view 함수를 import 하기

4. app_name 설정

5. project의 urls.py의 urlpattern에 앱 이름으로 바꿔주고  views 함수 대신 앱 이름.urls를 include해주기
6. import에 include 추가



include()

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 함

- 함수 include()를 만나면 URL의 그 시점까지 일치하는 부분을 잘라내고 남은 문자열 부분을 후속 처리하기 위해 include된 URLconf로 전달 (뭔소리여)

  



### Naming URL patterns

지금까지는 a태그에 url을 직접 작성하는 것이 아니라 path()함수의 name 인자를 정의해서 사용

Django template Tag url 태그를 사용 path() 함수에 작성한 name 을 사용할 수 있음

url template tag는  주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환(뭔소리여)

템플릿에 url을 하드 코딩하지 않아도 된다는 장점이 있음

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20173205.jpg" alt="naming url patterns" style="zoom: 67%;" />

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20173501.jpg" alt="namig url patterns2" style="zoom:67%;" />



현재 디렉토리에 있는 views를 import 함(같은 앱 안의 views.py에 있으니까!)

앱의 url에 오기전에 project의 urls.py를 먼저 만남 그래서 pages앱의 url을 연결시켜주는 path를 만들어 줘야 함

url pages로 요청이 들어오면 그 이후로는 pages앱의 urls.py로 이어서 보게 될 것이다!

include함수에 pages.urls를 인자값으로 넣어줌



## Namespace

articles app 과 pages app에 index라는 같은 이름의 url, template이 존재하면 에러가 발생함!

-> 왜? url namespace, template namespace 문제 때문

1.서로 다른 app의 같은 이름을 가진 url name은 이름공간을 설정해서 구분

2.template, static 등 django는 정해진 경로 하나로 모아서 보기 때문에 중간에 폴더를 임의로 만들어 줌으로써 이름 공간을 설정



### URL namespace

url namespace를 사용하면 서로 다른 앱에서도 동일한 url 이름을 사용하는 경우에도 이름이 지정된 url을 사용할 수 있음

어떤 app의 url인지 적어줘야함! ->app의 urls.py에 "app_name"에 attribute 값 작성

그래서 template의 url 태그에 : 을 넣어줘야함

두번째 앱도 마찬가지로!

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20184542.jpg" alt="url namespace"  />



### Template Namespace

django는 app_name/templates 경로에 있는 templates 파일들만 찾을 수 있고  INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함 그래서 앱이름과 같은  폴더를 똑같이 만들어 임의로 이름 공간을 생성해 줌 

이게 template namespace역할을 함!

app_name/templates/index.html

-> app_name/templates/app_name/index.html   

![template namespace1](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20185307.jpg)

폴더 구조를 변경 했기 때문에 views.py의 함수에서도 두번째 인자인 템플릿 경로에 '앱 이름/~' 로 경로를 바꿔줌

![template namespace2](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20185115.jpg)



# Static files

응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일(이미지, js, css) 

django는 staticfiles 앱을 통해 정적 파일과 관련 된 기능을 제공함

INSTALLED_APPS에 기본적으로 등록되어 있어서 별도로 추가할 필요 없음



 ### Static file 구성

1. django. contriv.staticfiles가 INSTALLED_APPS에 포함되어 있는지 확인

2. settings.py에서 STATIC_URL 정의(이미 되어있음)

3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드

   static 태그 뒤에 이미지의 경로를 써줌!

   static 태그는 빌트인 태그가 아니기 때문에 load를 써줘야 함!!!(STATIC_ROOT에 저장된 정적 파일에 연결)

   <img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20211324.jpg" alt="static file" style="zoom:150%;" />

4. 앱의 static 디렉토리에 정적 파일을 저장 -> my_app/static/my_app/example.jpg(template위치랑 유사!)

![static file2](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20211748.jpg)

*주의! load는 extends 아래에 써줘야 함! 

extends는 다른 어떤 태그들 보다 최상단에 있어야 하기 때문에!!(무.조.건)



### STATIC_URL

이미지를 개발자 도구로 찍어보면 host/static/이미지 경로 라는 url이 나타남

STATIC_URL이 중간 url을 만들어 주는 역할을 한 것!

*주의 /static/ 앤드슬래시 있어야 함!!

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20212829.jpg" alt="static url" style="zoom:150%;" />

이 이미지 url이 있어야 이미지가 출력이 됨

-> 사용자의 요청에 의해서 이미지가 보여짐  왜냐하면 요청은 url로 오기 때문에 이미지를 보여주기 위해서는 url이 있어야 하기 때문에! 



### STATIC_DIRS

정적 파일 추가 경로 만들어 주는 경우

1. 최상단(base.html과 같은 위치)에 static 폴더를 만들어 줌

2. settings.py에 정적 파일 위치 및 추가 경로 작성
3. template에 load로 static tag를 불러와서 이미지의 경로를 참조 해줌

![static dirs](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20215505.jpg)

<img src="django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20215736.jpg" alt="static dirs2" style="zoom:150%;" />

개발자 도구로 확인해보면?

![static url3](django_0302.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20215935.jpg)



### STATIC_ROOT

collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로

django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로

개발 단계에서 debug 값은 디버그를 위해 True로 되어있음 얘를 False로 바꾸면 배포 단계가 되어버림

실 서비스 환경에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

 