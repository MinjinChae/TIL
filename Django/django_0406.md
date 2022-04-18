# Django 03

## Review

### Model

데이터베이스의 구조를 만들 때, 그 구조를 장고의 모델 클래스를 통해 진행함 모델을 통해 데이터베이스에 접속하고 관리함

중요한건! 모델 클래스 하나가 데이터베이스의 테이블 하나에 매핑이 된다는 것!

### Database

데이터베이스 != 모델

모델을 통해 레이아웃을 짜고 그 레이아웃을 기반으로 데이터베이스를 생성함

-> 체계화된 데이터의 모임

쿼리

데이터베이스와 소통하기 위한 명령어

### Database의 기본구조

스키마

데이터베이스에서의 전반적인 구조, 표현방법, 관계 등을 정의한 구조

테이블

클래스 하나로 테이블 하나가 만들어짐

클래스에는 열(필드), 행(레코드)이 있음

### Model 정리

웹 애플리케이션에서 데이터를 구조화하고 조작하기 위한 도구!!

### ORM

객제 지향 프로그래밍 언어(파이썬)를 사용하여 호환되지 않는 유형의 시스템(데이터베이스는 파이썬이라는 언어를 이해할 수 없음)간에 데이터를 변환하는 프로그래밍 기술

![orm](django_0406.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-04-19%20234237.jpg)

파이썬을 쓰고 ORM이 SQL로 해석을 하고 돌아오는 SQL의 명령문을 다시 파이썬의 형태로 바꿔줌

Queryset API 문법에 근거하여 파이썬 객체 지향적 표현으로 요청을 보냄

데이터베이스가 우리에게 응답을 줄 때, object 또는 queryset 형태로 데이터 목록을 주면서 응답을 해줌

-> 왜 쓰는거야? 생산성때문에!

### models.py 작성

![models.py](django_0406.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-04-19%20234631.jpg)

상속을 받음 서브클래스로 표현

models 모듈에서 Model이라는 클래스(모델에 대한 역할을 할 수 있는 모든 기능이 작성이 되어있는 부모 클래스의 역할)

우리는 각 필드에 대해 정의만 해주면 됨 -> 필드의 이름, 필드의 타입, 속성값

나머지 다른 모델로써의 역할은 저 Model이라는 부모 클래스를 상속 받아서 쓰겠다는 것!

게시판이니까 title과  content라는 컬럼을 준비함, 2개의 필드

models안에 Field들이 존재함 

-> CharField는 길이에 제한이 있는 문자열을 받을 때 TextField는 길이에 제한이 없는 문자열을 받을 때

각 필드는 클래스의 변수(속성)로써 작성됨, 각 변수(속성)은 각 데이터베이스의 열에 매핑

id는 장고가 알아서 해주기 떄문에 작성 안해줘도 괜찮아

### Migrations

장고가 모델에 생긴 변화를 반영하는 방법!

makemigrations (필수) 모델을 변경했다면 반드시 설계도도 만들어야함!

migrate (필수) 설계도를 만들었다면 DB에 반영을 해야지 -> 모델과 DB가 동기화됨(둘이 같아졌구나!)

sqlmigrate SQL문으로 어떻게 해석이 되는지 미리보기 

showmigrations 프로젝트 전체에서 설계도들의 상태를 확인

### DB API

DB를 조작하기 위한 도구

ORM을 제공함에 따라 DB를 편하게 조작할 수 있도록 도움

매니저(objects)를 통해서 데이터베이스와 소통할 수 있는 QuerySetAPI를 사용할 수 있음

 ### 실습(redirect)

![redirect](django_0406.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-04-20%20004525.jpg)

게시글을 작성하니 log가 두 줄이 추가됨 우리는 제출을 누를 때 POST로 create주소로 요청을 보냄 (초록색)

요청을 보낸 다음에 요청이 하나 더 옴(두번째 줄) 이 주소는 articles/1 -> 이건 detail 페이지의 주소야

장고한테 요청이 두개가 온 것!! -> 왜? 두번째 요청은 redirect가 보낸 거! 우리는 detail 페이지로 가야하고 그럼 이 페이지를 받아야 함

이 페이지를 받으려면 요청이 가야함 요청이 가야 응답이 오니까! 

무슨 요청?  "나 detail 페이지로 가고싶어!" 그래서 글을 쓰고 요청이 하나 또 감 -> detail view 함수가 실행됨

글을 쓰고 또 요청을 넣을 수가 없으니까 그 과정을 redirect가 해주는 거!!



## Django Form

지금까지 HTML form, input을 통해서 사용자로부터 데이터를 받았지만 이렇게 사용자의 데이터를 받게되면 입력된 데이터의 유효성을 검증하고 검증 결과(ex.에러)와 함께 다시 표시해야함 

-> 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있기 때문에! 항상 생각해야함

개발자: 여기에 숫자쓰세요~  / 사용자: 싫엉 숫자 안 쓸거야

 사용자들은 개발자가 요구한 형식 그대로를 보내지 않을 수도 있음(그게 의도이든 실수이든 )

사용자가 입력한 데이터 검증 -> 유효성 검증 

유효성 검증을 쉽게 만들어주는 툴을 제공하는게 바로 Django Form



### Django's forms

유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

Form과 관련한 유효성 검사를 단순화, 자동화 할 수 있는 기능 제공

개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함

(개발자야 고생하지말고 내가 제공하는거 잘 써봐~)

1. 랜더링을 위한 데이터 준비 및 재구성

2. 데이터에 대한 HTML  forms 생성

3. 클라이언트로부터 받은 데이터 수신 및 처리

-> 데이터를 준비해주고  데이터에 대한 HTML form을 생성해주고 이 form에서 작성한 데이터를 수신, 처리 해줌 (기존의 form과 input에서 해주던걸  싹 다 해주는 아주 좋은 친구!) 



### Django 'Form Class'

Model Class를 작성했듯이 Form Class를 작성해야함

얘도 Model Class처럼 서브클래스로써 사용할거야!

Model class를 작성할 때, Model class라는 built-in class가 있었고 얘를 부모 클래스로써 사용했었음

마찬가지로 Form도 장고의 built-in class중에 Form Class가 존재하고 이걸 상속을 받아 서브클래스로 사용할거야 

Form내 field, field배치 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관한 에러메세지를 어떻게 작성할 것인지 결정

장고는 사용자의 데이터를 받을 때 해야 할 과중한 작업

데이터 유효성 검증, 데이터 검증 결과 재출력,  유효한 데이터에 대해 요구되는 동작 수행(유효한 데이터라면 거기에 요구되는 추가적인 동작들이 있을 것..!))과 반복 코드를 줄여 줌



### 실습

1. 가상환경 실행, 가상환경 활성화

앗 서버 켜기전에 migrate!!

python manage.py  runserver 



2. forms.py 생성

   articles앱에 forms.py? 없는데..? 기본적으로 만들어지지도 않았고 만든적도 없어

   urls.py를 만들어줬던 것처럼 forms.py도 만들어주자 

3. forms.py 작성

   django 내장 built-in에서 forms 모듈을 import해

   ArticleForm class를 만들어주고import했던 forms 모듈에 Form 클래스를 부모클래스로 상속받기

   필드 작성해주기(model 필드와 유사해..!) 이름은 model 필드에서 했던 것과 똑같음(title과 content)

   근데 content는 TextField가 아니야 text를 누르면 자동완성에서 TextField가 뜨지않음 

   models.py의 CharField는 models모듈에 있고 forms.py의 CharField는 forms모듈에 있음

   즉, 이름은 같지만 같은 필드는 아니라는거..! 

   models.py의 CharField에서 max_length는 필수인자, forms.py의  CharField에서는 max_length 안쓰네..?(필수가 아니구나..)

   

<기존의 form과 input태그 대체하기 -> new, edit >

4. views.py의 new 함수 수정

   forms.py에서 FormClass import 해오기 .(현재 디렉토리의) forms모듈에서 ArticleForm import 하기

   ArticleForm이라는 클래스로 form이라는 인스턴스 생성

   이 인스턴스를 context에 넣음 -> 템플릿으로 보내겠다!

   

5. new.html 수정

   장고의 form은 사용자의 입력을 받는 부분에 관여함(label부터 textarea까지)

   변수 form(context에서 넘긴 form) 그리고 서버를 켜고 개발자 도구를 보면 lablel과 input이 만들어져있음! 

   forms.py에서 만들어진 인스턴스가 출력되고 있음

   title 필드에서 max_length=10를 넣었기 때문에 Title에서 10자 이상 써지지 않음

   (하지만 10자인지 아닌지 유효성 검사는 아직 안했음! 우선 사용자의 입력 자체를 막는거)

   근데 여기서 문제점!

   첫번째, 아까전에는 context가 text아래에 있었는데 지금은 옆에 있음 -> 속성값 설정

   as_p() -> \<p> 태그로 감싸져서 렌더링 됨

   두번째, content가 textarea가 아님 -> widget 이용(django widget 검색해서 참고)

   widget값도 forms에 있음 -> 태그가 textarea로 바뀜 

   우리는 label태그와 input태그를 직접 작성하고 있지 않기 때문에 class의 속성값으로 input을 컨트롤함





From rendering options

as_p() 각 필드가 단락(\<p>태그)로 감싸져서 렌더링 됨

as_ul() 각 필드가 항목(\<ul>태그)로 감싸져서 렌더링 됨, \<ul>태그는 직접 작성해야 함

as_table() 각 필드가 테이블(\<tr>태그)행으로 감싸져서 렌더링 됨, \<table>태그는 직접 작성해야 함



Django의 HTML input 요소 표현 방법 2가지

Form fields

input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용 됨

하지만, form fields가 모든걸 제공해주지는 않음..! textarea 태그도 없어

이런 부분을 채워주는게 widgets!

widgets

웹 페이지의 HTML input 요소 렌더링

GET/POST  딕셔너리에서 데이터 추출

단독 사용 불가능! widgets은 반드시 Form fields에 할당 됨

주의사항

form fields와 혼동되어서는 안됨

form fields는 input 유효성 검사를 처리 widgets는 유효성 검사와 관련 없음

단순히 input element의 단순 raw한 렌더링 처리

form field 및 widget 응용

drop down형태의 select 태그 -> FormField 와 widgets으로 대체

region이라는 변수를 만들고 무언가를 선택을 하는 필드니까 ChoiceField 그 안에 widget은 select 

ChoiceField에서 select는 default이기 때문에 굳이 적지않아도 괜찮음

ppt처럼 호출로 안 해도 상관없음

변수 생성 -> 옵션 태그 직접 입력하는 것처럼 선택 요소 만들기

하나의 리스트로 묶기 

첫번째 튜플값: 변수값,value값  두번째 튜플값: 사용자에게 출력되는 형태

사용자가 서울을 클릭하면 sl이 우리에게 넘어옴

두번째 인자 choices에 키워드 인자가 들어감 













장고에서 forms 함수 불러오기

forms모델에서 Forms class를 상속을 받고

model이랑 구조가 비슷함

근데 content는 textfield가 아님 textfield제공안함

이름은 같지만 같은  field가 아님

model에서 charfield는 maxlength가 필수였는데 form에서는 안쓰네..?

form과 input태그를 대체해주기 -> new, edit

views.py

일단 form을 import해오기

인스턴스 생성

context에 form을 넣어주고 rendeer의 세번째 인자에 context 넣어주기

context에 넣어준다는건 템플릿에 보내겠다는것!

new.html

사용장에게 입력을 받는부분에 관여함

변수 form을 출력 {{ form }}

개발자 도구로 확인해보니 label, input이 생겨져있음

forms.py에서 생성한 인스턴스로인해 title과 content가 출력됨

input에 max_lenght가 생성되서 10자이상 입력안됨

근데 아직 10자인지 아닌지 유효성 검사는 안했고 기본적으로 사용자로부터 입력을 막음

input태그가 인라인태그라 title content가 한줄에 있음 얘네를 어떻게하지..?

-> rendring options 사용



widget = forms.Textarea를 입력하면 textarea태그로 바뀜

widget은 반복적으로 사용못함 field를 먼저 사용하고 field에서 사용할 수 없는것을  widget에서 사용

input을 표현하는 두가지 방법은 field랑 widget



widgets 

input element 표현

form fields와 혼동되어서는 안됨

form fields는 input 유효성 검사를 처리 widgets는 유효성 검사와 관련 없음

단순히 input element의 단순 raw한 렌더링 처리



choice태그의 select 인자값들은 어떻게해..?

ChoiceField

default widget이 select

다 써주고 

하나의 리스트를 만들고 그안에 튜플 형태로 넣어줌

두번째가 실제 출력값 위에 sl이 우리한테 보내지는 value값

choices=REGIONS_CHOICES

왜 굳이 불편하게 나눠서 써야해? 장고에서 권장하는 스타일 가이드가 그러래..

django coding style 검색해서 들어가



ModelForm

title과 content는 이미 Model 필드에서 썼기 때문에 Form에서  Model 필드를 재정의하는 행위가 중복 될 수 있음 그래서 model을 통해 form을 만들 수 있는 helper가 있음

ModelForm Class

일반 Form Class와 완전히 같은 방식으로  view에서 사용 가능

class안에 class를 작성..? 뭐래



forms 라이브러리의 ModelForm 클래스를 상속받음

Metal 클래스 선언 어떠 ㄴ모델을 기반으로 Form을 작성할 것인지에 대해 Meta 클래스에 지정



Inner Class

가독성 및 프로그램 유지 관리를 지원

외부에서 내부 클래스에 접근할 수 없어 외부에서 보여지지 않는 정보를 여기에 작성?

코드의 복잡성을 줄일 수 있음

Meta 데이터

데이터에 대한 데이터

ex) 사진 - 컴퓨터의 입장에서는 사진 데이터

사진에도 데이터가 있음(날짜, 위치 등등) 이런걸 메타 데이터라고 함



그래서 너 무슨 model을 기반으로 만들건데? 

model  가져오기 

어떤 필드를 출력할거야?

두개면 두개 적으면 되는데 많으면 다 적어줘야해? 아니 전체 필드를 출력하려면 \__ all__ 

-> 새로고침 해보면 똑같이 나옴 field를 작성해주지도 않고 model만 지정해줬는데  widget으로 바꿔주지도 않았는데.. 왜냐면 모델에서 textfield라고 되어있으니까 그대로 가져왔음

created_at updated_at은 사용자로부터 받는게 아니네? 그럼 출력대상에서 빠져~



modelForm  Form 

뭐가 더 좋고 뭐가 더 나쁜건 없음 역할이 다를 뿐

모델폼이라면 아이디랑 비밀번호를 DB에 저장하라? 저장하라는건 로그인이 아니라 회원가입임 

이런 경우는 모델폼

하지만 로그인은 외부적으로 인증 절차를 밟고 끝 DB랑 연관없음 이런경우는 form

modelform이 짱이네 이런건 아님 

사용자로부터 받는 데이터가 ~~

우리는 제목과 내용을 저장해야하니까 modelform을 사용함



10개의 필드중에 9개의 필드만 출력한다면 하나를 제외하는게 빠름

그때 exclude를 사용 만약 title을 빼겠다! 

주의사항!! fields와 exclude를 동시에 사용못함

어떤 field들은 기본값이 들어오기 때문에 출력을할 필요가 없다면 exclude를 사용함



Form으로 받아서 DB에 저장

model의 구조를 그대로 받아서 쓸 수 있다면 modelForm 사용

form은~



create함수

request.Post 딕셔너리 데이터를 한번에 넣어줌

받는 갯수가 상관없어짐 한번에 통째로 받으니까!

유효성 검증의 별도의 복잡한 코드를 작성할 필요가 없다

데이터를 각각 받아왔던걸 인자로 넣어서 한줄로 바꿔줌

유효성 검사 진행

is_valid 

이게 valid 하냐?

함수가 is로 시작하면 boolean 유효한지 아닌지 True False 가 나옴

통과를 하게되면 

통과된 form에 save method호출 하고 저장

통과하지못하면 -> 제목이 10자 초과되었을때

어디론가 return을 해서 응답을 해줌

통과 했으면 detail페이지로 보내 

왜 노란불이 들어와..? 아까 저기서는 aritcle 인스턴스가 있었는데 지금은 없어

근데 save의  return값은 article  이렇게 적어주면 괜찮아

통과 못했으면 다시 new페이지로 가자



model form의 save method

객체를 만들고(반환) 저장함

하위 클래스는 기존 모델 인스턴스를 키워드 인자 인스턴스로 받아 들일 수 있음

유효성 검사를 통과하지 못하면  form.errors를 확인하여 에러 확인 가능함



인스턴스값이 있다 수정

없다 새로운 글 작성이구나









error messages는 attrs가 아님 widget가 동일한 선상에 있음



