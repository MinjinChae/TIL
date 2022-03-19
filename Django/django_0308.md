# Django 02

## Django Model

### Model

웹 애플리케이션의 데이터를 구조화 하고 조작하기 위한 도구

단일한 데이터에 대한 정보를 가짐

저장된 데이터베이스의 구조(layout) -> django에서 쓸 데이터 구조를 잡는것

데이터 각각의 필드가 있음 필드가 여러개 모여서 하나의 구조를 이룸

@@@ django는 model을 통해 데이터에 접속하고 관리!!!!!

일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨



ORM SQL을 쓰지 않고 파이썬을 이용해서 데이터베이스를 다룰 수 있는 것

Migragions Model의 히스토리

git은 코드 변경 사항의  히스토리를 쌓는것 

CRUD 

create 생성 

read 읽기

update 수정

delete 삭제



### Database

- 데이터베이스(DB)

체계화된 데이터의 모임

- 쿼리(Query)

데이터를 조회, 조건에 맞는 데이터를 가져오거나 수정,삭제 등 조작하기 위한 명령어

쿼리를 날린다 -> 데이터베이스를 조작한다! CRUD

데이터를 가져오기 위한 명령어 -> SQL로 날림



### Database의 기본 구조

- 스키마(Schema)

데이터 베이스가 어떤 구조로 작성되어있는가 필드가 어떤 구조로 구성되어있는가 등의 설계도

스키마를 보면 데이터베이스가 어떻게 생겼는지 알 수 잇음

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20224810.jpg" alt="schema" style="zoom: 67%;" />

- 테이블

모델 클래스를 만듬으로써 테이블을 지정해줌

열(column):  필드(field), or 데이터의 속성들

행(row): 레코드(record) or 튜플 

데이터를 추가하면 row가 늘어남 -> 데이터의 한줄 한줄을 의미함

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20231544.jpg" alt="col" style="zoom:50%;" />

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20231600.jpg" alt="row" style="zoom: 67%;" />

- PK primary key

각각의 데이터를 구분할 수 있는 고유값 ex. 주민번호

데이터안에서 pk가 다르다면 무조건 다른 데이터고 pk를 통해 데이터를 지목, 가져올 수 있음

pk는 중복이 될 수 없음

일반적으로는 id라는 이름을 사용함

django는 우리가 pk를 지정하지 않으면 자동으로 id라는 값으로 저장해줌 -> 우리가 데이터를 추가할때마다 자동으로 1씩 증가하면서 추가됨

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20232102.jpg" alt="pk" style="zoom: 67%;" />

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-19%20232304.jpg" alt="database stru" style="zoom:67%;" />





## ORM 

Object Relational Mapping 객체 관계 매핑

데이터베이스를 모델 객체로 접근하겠다는것

객체 지향 프로그래밍 언어를 사용해서 django와 sql 데이터를 변환하는 기술 (sqld 따라구,,,) 

-> SQL을 쓰지 않고 파이썬을 이용해서 데이터베이스를 다룰 수 있는 것!! 

DB에는 두가지 형식이 있는데

첫번째는 테이블 형식(SQL database) 이게 일반적인거

두번째는 테이블이 없는 데이터베이스(noSQL database) 테이블이 조금 느슨한거

조금 더 자유롭게 사용함 채팅이나 빠르게 변하는 데이터 베이스는 noSQL 데이터 베이스를 사용함



### ORM의 장점과 단점

- 장점

SQL을 잘 알지 못해도 DB조작 가능

객체 지향적 접근으로 인한 높은 생산성

- 단점

ORM만으로 완전한 서비스를 구현하기 어려움

한겹 더 감싸서 파이썬으로 소통해야하니까 효율성이 떨어짐

but 현대 개발 세계에서는 웹 개발의 속도를 높이는 것(생산성)이 중요하기 때문에 ORM 을 사용하고 있음!

그래서 왜 사용하는데..? SQL 모르는데 데이터베이스를 다루고 싶으니까 쓰는거

-> "우리는 DB를 객체(objects)로 조작하기 위해 ORM을 사용한다"



### models.py 작성

![models.py](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-08%20101836.jpg)

각 모델은 django.models.Model 클래스의 서브 클래스로 표현되고 django.db.models 모듈의 Model 클래스를 상속받음

models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의

title과 content는 모델의 field를 나타냄

각 필드는 클래스 속성으로 지정되어 있고 각 속성은 각 데이터베이스의 열에 매핑



### 사용 모델 필드

- TextField( \**options)

글자의 수가 많을  때 사용

max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에는 반영 but 모델과 데이터베이스 수준에는 적용되지 않음

- CharField(max_length=None, \**options)

길이의 제한이 있는 문자열을 넣을 때 사용

-> 핸드폰 번호를 입력하라고 했는데 유저는 이름을 쓸 수도 있어서 유효성 검사를 해줘야함

CharField는 반드시 max_length가 필요함!

- field options

default로 false값이 들어가 있어서 필요할때 지정하면됨

null: null이라는 값이 저장될지 선택

데이터 베이스에 null값이 들어갈지 말지 선택파이썬에서는 none과 똑같은것

필요할 때 null = True라고 지정하면됨

blank: 빈칸으로 두어도 될지 선택하는것



### Migrations

django가 model에 생긴 벼화를 반영하는 방법

1. makemigrations

   moeel을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용

   <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20000940.jpg" alt="makemigrations"  />

2. migrate

   마이그레이션을 DB에 반영하기 위해 사용

​		<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20000958.jpg" alt="migrage"  />

3. sqlmigrate

   마이그레이션에 대한 SQL 구문을 보기 위해 사용

   ![](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20001042.jpg)



4. showmigrations

   프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용

   마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음

   ![showmigrations1](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20001129.jpg)



![showmigrations2](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20001143.jpg)

여기서 model 수정!

![model수정](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20002701.jpg)

이런식으로 Model을 조작(생성,수정,삭제)하면 반드시 마이그레이션을 생성하고 반영(적용)해줘야함!

-> 장고의 흐름! 앱 만들면 settings.py에 등록해주는것처럼



### DateField's options

자동으로 시간  저장

- auto_now_add

  최초 생성 일자

  Django ORM이 insert시에만 현재 날짜와 시간으로  갱신

  맨 처음에 레코드가 생성될때 최초 한번 저장하는것

- auto_now

  최종 수정 일자

  Django ORM이 save할 때마다 현재 날짜와 시간으로 갱신

  데이터가 수정(변경)이 될 때마다 시간이 저장이됨, 갱신해줌



## migrations 정리

기본기능이 생성됨

관리자 인증 컨텐트타입 세션

히스토리처럼 쌓는 마이그레이션을 만들어줄때 python manage.py makemigratios

적용되지 않은 마이그레이션을 적용할때 python manage.py migrate

sql로 어떻게 변환이 되었는가 보는데 python manage.py sqlmigrate appname 0001

각 마이그레이션이 실제로 데이터에 적용이 된건지 확인하기 위해서는 python manage.py showmigrations



## Database API

DB를 조작하기 위한 도구

![making queries](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012306.jpg)



### 실습

라이브러리 등록 및 실행

1. 라이브러리 설치

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012532.jpg" alt="라이브러리 설치" style="zoom:50%;" />



2. 앱 등록 후 shell_plus 실행

   <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012543.jpg" alt="라이브러리 등록 및 실행" style="zoom:50%;" />

shell_plus 실행하면 이 화면이 나타남

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012555.jpg" alt="shell_plus실행" style="zoom:50%;" />

데이터를 저장하는 방법은 3가지가 있음



## CRUD

### [실습] READ

전체 article 객체 조회

class이름.매니저objects.all()

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012649.jpg" alt="read_all"  />

아직 아무것도 create하지 않은 상태니까 QuerySet의 리스트가 비어있음

### [실습] CREATE

1.  인스턴스를 만들고 save하는 방법

article = Article()

article.title = '~~'

article.save()

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012645.jpg" alt="create 1" style="zoom:150%;" />

2. 인스턴스 생성과 동시에 keyword인자를 넘기는 방식

article = Article(title='~~', content='text')

article.save()

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012705.jpg" alt="create 2"  />

3. QuerySet API - create() 사용

Article.objects.create(title='~~', context='text')

![create 3](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012716.jpg)



### [실습] 테이블 확인

![table check](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012735.jpg)



### str method

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20015828.jpg" alt="str method" style="zoom:50%;" />



### [실습] READ

- all()

   모든 데이터 조회, 현재 QuerySet의 복사본 반환

![read_all_2](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012833.jpg)

- get()

get 1개의 데이터 조회

pk(id)랑 같이 써줌

models에 pk는 없지만 내부적으로 자동으로 id와 같은 값으로 인식하게 해줘서 사용 가능함!

![get](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012844.jpg)

pk=100은 존재하지 않아서 에러가 떴음

get은 한가지의 데이터만 가져오기  때문에 둘 이상의 객체를 찾아서 'MultipleObjectsReturned'에러가 떴음

- filter()

주어진 lookup 매개변수오 일치하는 객체를 포함하는 새 QuerySet을 반환

조건과 일치하는 모든 데이터를 가져와줌!

-> "content가 django인 데이터를 가져와줘!"

​	"tilte이 first인 데이터를 가져와줘!"

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012857.jpg" alt="filter" style="zoom: 67%;" />



### [실습]UPDATE

1. 수정할 데이터를 불러오기
2. 인스턴스 객체의 인스턴수 변숭의 값 변경 -> article.title = '어쩌구로 수정' 라고 고쳐주기
3. 저장하기 article.save()
4. Article.objects.all()로 전체 또는 article.title로 데이터를 확인하면 바뀌어져있음

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012911.jpg" alt="update" style="zoom: 67%;" />



### [실습]DELETE

delete()

1.삭제할 데이터 불러오기

2.delete()로 데이터 삭제하기

![delete](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012923.jpg)

-> 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환함



### Field lookups

get과 filter에는 조건이 들어가는데 이걸 field lookups이라고함

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

contains ~를 포함하고 있는

숫자

gt

gte

in

isstartswith ~로 시작하는

등등이 있음

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20023508.jpg" alt="field lookups" style="zoom: 67%;" />



Queryset DB의 객체의 목록이구나 

리스트처럼 인데스, 슬라이싱이 가능함



## Admin Site

### admin 생성

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20012943.jpg" alt="admin create" style="zoom: 67%;" />

관리자 계정 생성 후 서버를 실행하고 '/admin' 로 가서 관리자 페이지 로그인

내가 만든  model을 볼 수 있음

### admin 등록

admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것

models.py 에 정의한  \__str__의 형태로 객체가 표현됨(뭔소리여)

-> ".models 나와 같은 위치에 있는 models에서 Article(클래스 이름)을 import해와!"

​	 "admin site에 register(등록)해!"

<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20024833.jpg" alt="admin register" style="zoom: 80%;" />



## CRUD with views

### CRUD 실습

1. 프로젝트 생성 django-admin startproject crud .

2. 앱 생성 python manage.py startapp articles

3. 앱 등록 settings.py INSTALLED_APPS의 제일 위에 등록해주기 트레일링 콤마도 잊지말자!

4.  base 템플릿 작성하고 settings.py에 추가 템플릿 경로 등록 여기서도 트레일링 콤마 잊지말자!

   ![crud_4](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20143612.jpg)



5. articles 앱의 urls.py 작성

   현재 디렉토리에서 views를 import 해줘!

   'index'라는 주소가 요청이 들어오면 views.index 함수를 호출하고 이 주소의 이름은 index야 (트레일링 콤마 잊지말자!)

   <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20144529.jpg" alt="crud_5" style="zoom: 80%;" />

   

6. articles 앱의 views.py 작성

   index 함수를 정의

   첫번째 인자는 무조건 request 이건 약속이야

   return 해줄거야 무엇을? render  첫번째 인자는 무조건 request 두번째 인자는 템플릿의 경로

   <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20144542.jpg" alt="crud_6" style="zoom:80%;" />

   

7. index의 템플릿 만들어주기

   샌드위치 구조로 만들어주자 (articles/templates/articles/index.html)

   base.html을 상속받으니까 extends 태그를 최상단에 적어주고 block 태그를 적어 준 후 오버라이딩 해주자

   <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20144552.jpg" alt="crud_7" style="zoom: 50%;" />

8. READ - 전체 게시글 조회

   views.py

   같은 디렉토리에 있는 models에서 Article을 import 해와

   모델을 이용해서 모든 데이터를 가져와 -> article = Article.objects.all()

   가져온 데이터를 템플릿으로 넘겨 -> context는 딕셔너리 형태로 작성해주기

   템플릿에서 데이터를 보여줘 -> 세번째 인자로 context 넣어주기

​		<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20145511.jpg" alt="crud_8" style="zoom: 67%;" />



​		index.html

​		화면에 보여 줄 내용 변수로 표현해주기

​		변수는 중괄호 두개! {{ ~~ }} .(dot)이용해서  뽑아낼 수 있음!

​		<img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20145539.jpg" alt="crud_8_2" style="zoom: 80%;" />



9. CREATE-New views

   urls.py에서 지금까지와 동일한 방법으로 path 작성해주기

   views.py에서도 마찬가지

   new.html 만들어서 내용 작성해주기

   여기서 짚고 넘어 갈 부분은....!

   내용 입력하는 부분은 textarea태그, cols와 rows로 크기 늘려주기

   <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20150317.jpg" alt="crud_9"  />



10. CREATE - Crreate views

    create는 new 페이지에서 입력한 데이터를 받는 페이지!

    urls.py 동일한 방법으로 path 작성해주기

    views.py

    create 함수 정의 첫번째 인자는 무조건  request 이건 약속이야

    title을 request GET 방식으로 get해 ('title')  멀라

    ????????????????????

    DB 데이터 저장하기

    분홍색은 모델에 있는 필드명!, 초록색은 입력한 데이터명!

    ![crud_10](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-08%20162658%20(2).jpg)

    ![crud_10_2](django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20153456.jpg)

    create.html 작성(근데 이건 나중에 필요없어서 지울거야)

    

11. views.py에 돌아가서 inex함수 수정

    게시글 정렬 순서를 최신순으로 변경하기

    첫번재 방법은 DB로 부터 받은 퀴리셋을 이후에 파이썬이 변경(파이썬이 조작)

    ->슬라이싱 이용하기!

    두번째 방법은 내림차순 쿼리셋으로 받음(DB가 조작)

    -> order_by('-pk')

    <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20154009.jpg" alt="crud_11" style="zoom: 50%;" />



12. new 로직 수정

    new.html

    서버를 전송하는 방식 즉, method를 post로 수정해주고 그 밑에 csrf_token 태그 추가해주기

    <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20154802.jpg" alt="crud_12" style="zoom: 67%;" />

    views.py

    POST로 바꿔주고 redirect 함수 적용해서 index페이지 가도록 바꿔주기

    redirect도 import해줘

    render가 아니라 redirect를 return해

    <img src="django_0308.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-20%20155358.jpg" alt="crud_12_2" style="zoom: 50%;" />

    

13. DETAIL

    개별 게시글 상세 페이지 구현하기!

    글의 번호(pk)를 활용해서 가각의 페이지를 따로 구현해야 함

    urls.py

    Variable Routing 활용하기 -> paht에  '\<int:pk>/' 넣어주기

GET은 form의 GET method

get은 데이터 가져온다는 뜻!



분홍색은 모델에 있는 필드명!

초록색은 입력한 데이터명!



GET url 쿼리스트링에 보여짐

기본값 서버 리소스를 요청할때

POST body에 한번 숨겨서

그외 전부 리소스를 생성 수정 삭제할 때



CSRF Token

공격자가 나인척 하면서 글을 쓸 수 있음

이걸 방어하기 위해서..!

데이터를 보내는 쪽과 데이터를 받는 쪽이 암호를 주고 받음  -> CSRF Token

form에서  method로 post를 보내려면 csrf token을 써줘야함

settings.py

MIDDLEWARE 요청이 들어오면 여기를 거쳐서 지나감

csrftoken에 대한 middleware가 들어가 있음

자동으로 검증해줌



render라는 함수는 템플릿을 렌더해서 결과로 돌려주는 함수 

index.html에서 context를 넘겨주지 않아서 나오지않음

그러니까 템플릿을 렌더링하는게 아니라 특정한  url로 가게해주면됨

redirect import해줌

특정 url로 사용자를 보내버리는 역할을함





db 데이터를 저장해둬야 밑에서 활용가능



이 url이 들어오면 views이 delete로 보내!



빨간색 디테일 노란색 삭제 초록색 인덱스



post 일때도 삭제가 되겠지만 이 view 로 들어오면 삭제됨

데이터베이스에는 항상 utc 기준으로 저장

어떻게 보여줄지 지정해주는게  timezone 속성



폴더이름 0308로 제출