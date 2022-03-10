ORM SQL을 쓰지 않고 파이썬을 이용해서 데이터베이스를 다룰 수 있는 것

Migragions Model의 히스토리

git은 코드 변경 사항의  히스토리를 쌓는것 

CRUD 

create 생성 

read 읽기

update 수정

delete 삭제

Model 

단일한 데이터에 대한 정보를 가짐

데이터 각각의 필드가 있음 필드가 여러개 모여서 하나의 구조를 이룸

model을 통해 데이터에 접속하고 관리!!!!!@@@

데이터에 접속하고 관리하려면 model

Django에서 쓸 데이터 구조를 잡는것



Database

데이터베이스(DB)

체계화된 데이터의 모임

쿼리(Query)

쿼리를 날린다 데이터베이스를 조작한다! CRUD

데이터를 가져오기 위한 명령어 -> SQL로 날림

데이터를 조회, 조건에 맞는 데이터를 가져오거나 수정,삭제 등 조작하기 위한 명령어



기본 구조

스키마 

데이터 베이스가 어떤 구조로 작성되어있는가 필드가 어떤 구조로 구성되어있는가 등의 설계도

스키마를 보면 데이터베이스가 어떻게 생겼는지 알 수 잇음

테이블

모델 클래스를 만듬으로써 테이블을 지정해줌

열 column  데이터의 속성들

행 row 데이터를 추가하면 row가 늘어남 

행(row),레코드 데이터의 한줄 한줄을 의미함

PK primary key 각각의 데이터를 구분할 수 있는 고유값 ex. 주민번호

데이터안에서 pk가 다르다면 무조건 다른 데이터고 pk를 통해 데이터를 지목, 가져올 수 있음

pk는 중복이 될 수 없음

일반적으로는 id라는 이름을 사용함

장고는 우리가 pk를 지정하지 않으면 자동으로 id라는 값으로 저장해줌

우리가 데이터를 추가할때마다 자동으로 1씩 증가하면서 추가됨



ORM 

object relational mapping

객체관계매핑

데이터베이스를 모델 객체로 접근하겠다는것

프로그래밍 언어를 사용해서 django와 sql 데이터를 변환하는 기술

sqld 따라구,,, 

DB 에는 두가지 형식이 있는데

하나는 테이블 형식(SQL database) 

일반적인거

두번째는 테이블이 없는 데이터베이스(noSQL database)\

테이블이 조금 느슨한거

조금 더 자유롭게 사용함 채팅이나 빠르게 변하는 데이터 베이스는 noSQL 데이터 베이스를 사용함

orm 

장점

SQL을 잘 알지 못해도 db조작 가능

객체 지향적 접근으로 인한 높은 생산성

단점

ORM만으로 완전한 서비스를 구현하기 어려움

효율성이 떨어짐 한겹 더 감싸서 파이썬으로 소통해야하니까 효율성이 떨어짐

현대 개발 세계에서는 웹 개발의 속도를 높이는 것(생산성)이 중요하기 때문에 ORM 을 사용하고 있음!

그래서 왜 사용하는데..?

SQL 모르는데 데이터베이스를 다루고 싶으니까 쓰는거



class로 만들어야함  modes.Model로 상속받아야함



CharField 핸드폰 번호를 입력하라고 했는데 유저는 이름을 쓸 수도 있어서 유효성 검사를 해줘야함

CharField는 반드시 max_length가 필요함!

field options

default로 false값이 들어가 있어서 필요할때 지정하면됨

null null이라는 값이 저장될지 선택

데이터 베이스에 null값이 들어갈지 말지 선택

파이썬에서는 none과 똑같은것

필요할 때 null = True라고 지정하면됨



blank 빈칸으로 두어도 될지 선택하는것



이런식으로 Model을 조작(생성,수정,삭제)하면 반드시 마이그레이션을 생성하고 반영(적용)해줘야함!

-> 장고의 흐름! 앱 만들면 settings.py에 등록해주는것처럼



기본기능이 생성됨

관리자 인증 컨텐트타입 세션

히스토리처럼 쌓는 마이그레이션을 만들어줄때 python manage.py makemigratios

적용되지 않은 마이그레이션을 적용할때 python manage.py migrate

sql로 어떻게 변환이 되었는가 보는데 python manage.py sql~

각 마이그레이션이 실제로 데이터에 적용이 된건지 확인하기 위해서는 showmigrations

DateTimeField 자동으로 시간  저장

auto_now_add  맨 처음에 레코드가 생성될때 최초 한번 저장하는것

auto_now 이 데이터가 수정(변경)이 될 때마다 시간이 저장이됨, 갱신해줌



데이터를 저장하는 방법은 3가지가 있음



Queryset DB의 객체의 목록이구나 

리스트처럼 인데스, 슬라이싱이 가능함



\__str__ 이걸 써줘야지 글자가 보임





Read

all 모든 데이터 조회

get 1개의 데이터 조회

get은 한가지의 데이터만 가져오기 때문에 에러가 뜬거

그래서 pk(id)랑 같이 써줌

models에 pk는 없지만 내부적으로 자동으로 id와 같은 값으로 인식하게 해줘서 사용 가능함!

filter

조건과 일치하는 모든 데이터를 가져와줌

get과 filter에는 조건이 들어가는데 이걸 field lookups이라고함

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

contains ~를 포함하고 있는

숫자

gt

gte

in

isstartswith ~로 시작하는

등등이 있음

데이터를 불러와서

article.title = 어쩌구야 라고 고쳐준 후에 저장해줌

Article.objects.all()로 전체 데이터를 확인하면 바뀌어져있음

이미 불러왔으니까 그걸 article.delete()로 지울 수 있음

.models 나와 같은 위치에 있는 models에서 article을 가져와



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