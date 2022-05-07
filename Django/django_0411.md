## The Django Authentication System

Django의 인증 시스템은 django.contrib.auth에 Django contrib module로 제공

필수 구성은 seetings.py에 이미 포함되어 있으며 INSATLLED_APPS 설정에 나열된 아래 두 항목으로 구성됨

1. django.contrib.auth
2. django.contrib.contenttypes

별도로 추가를 하는 작업이 필요없음!

이미 내장앱이 작성이 되어있음 -> 이 두가지가 장고의 인증 시스템에 반영을 할 것

django.contrib.auth 인증 프레임워크의 핵심 기본 모델 포함 

django.contrib.contenttypes 사용자가 생성한 모델과 권한을 연결할 수 있음 권한에 관련된 것!



Django 인증 시스템은 인증(Authentication)과 권한(Authorization)부여를 함께 제공하고 이러한 기능이 어느 정도 결합되어 인증시스템이라고 함



### Authentication & Authorization

- Authentication(인증)

  신원 확인

  사용자가 자신이 누기인지 확인하는 것

- Authorization(권한, 허가)

  권한 부여 

  인증된 사용자가 수행할 수 있는 작업을 결정 -> 로그인을 했다고해서 다들 같은 권한을 가지고 있는게 아님 ex. 회원에도 등급이 있음, 관리자와 일반 사용자에 대해서 서로가 할 수 있는 일이 다름



두번째 앱 생성

app 이름이 반드시 acoutns 일 필요는 없음

auth와 관련해 django 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 accounts로 지정하는것을 권장!!



accounts 앱 생성했으면 앱 등록  생성 후 등록!!

url에 가서 해줌 이 문자열, 이 주소로 url이 들어온다면~ 여기서 자르고 이어서 연결된 urls.py를 include해줌

어차피 articles랑 구조는 똑같음

accounts 앱의 urls.py 만들어줌



쿠키와 세션

HTTP 

Protocol 규칙 규약

비연결지향 서버는 요청에 대한 응답을 보낸 후 클라이언트랑 연결을 끊음

네이버에 들어갔어 우리랑 네이버가 연결이 되어있구나!하고 생각을 할 수 있어

연결이 되어있으니까 이 페이지를 볼 수 있구나~ 사실 이건 불가능해

즉 우리가 네이버의 메인 페이지를 줘ㅓ하고 요청을 보내면 네이버의 메인 페이지를 보내는 응답을 하고 끊어지는거 서로 손을 잡고 있는게 아니야

무상태 연결을 끊는 순간 서로의 통신이 끝나기 때문에 이 상태가 유지되지 않음

서로 완전히 독립적임

근데 로그인 상태는 유지 됨

  클라이언트와 서버의 지속적인 관계를 유지하기 위해 쿠키와 세션이 필요함!



쿠키

서버가 주는 작은 데이터 조각 

우리가 웹사이트를 방문할 때 웹 브라우저가 우리에게 주는 것

사용자의 컴퓨터에 설치되는 작은 기록 정보 파일

KEY-VALUE 데이터 형식으로 저장

동일한 서버에 재 요청시 저장된 쿠키를 함께 전송함



로그인 요청이 담긴 쿠키와 응답을 같이 보내주고 클라이언트의 컴퓨터에 쿠키가 저장이 되고 같은걸 재요청할 때 요청과 쿠키를 같이 보냄

나 지금 로그인 되었어 하고 매요청마다 말해줌 나 로그인 되어있는 사람이야~ 그래서 마치 상태가 계속해서 유지되어 있는 것 처럼 보임 서버는 매 요청을 받을때마다 어? 얘 연결되어 있는 사람이네 하고 인식



쿠키 사용 목적

세션관리

상태를 유지시켜주는 세션 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니

개인화

트래킹 시크릿모드 모든 요청에 대해 데이터를 저장하지 않고 일회용으로 사용하는! 



개발자 도구 - 네트워크 - 헤더

set-cookie 

cookies

request cookies 요청할 때 보내는 쿠키

response cookies 응답을 받는 쿠키



장바구니에서 상품 삭제 버튼은 내가 도마를 가지고 있다는 쿠키를 삭제하는거

cookies clear 누르면 도마가 사라짐



세션 

무상태를 상태가 있는 것처럼 유지시키는 것

클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 발급 받은 session id를 쿠키에 저장 쿠키는 요청 때마다 서버에 함께 전송되고 서버에서 session id를 확인해 알맞은 로직을 처리

쿠키에는 ID만 저장함 key만 저장하는거! 값은 서버가 저장하고 있음



응? 유효기간이 작성되어 있지 않은 세션들은?

쿠키는 수명주기에 따라 두가지로 정의됨

Session cookies 브라우저가 현재 세션이 종료되는 시기를 정의

현재 세션이 종료되면 같이 삭제됨

ex.swea 

Persistent cookies

지정된 기간이 지나면 삭제



장고는 짱이야..



## 로그인

로그인은 CRUD에서 session을 create하는 로직과 같음

로그인은 유저를 만드는게 아니라 로그인 상태를 유지할 수 있는 session, cookie를 create하는것과 같음

Django는 우리가 session의 메커니즘에 생각하지 않게끔 인증에 관한 built-in forms를 제공해줌



### Authentication Form

사용자 로그인을 위한 form

request를 첫번재 인자로 취함

urls.py

login에 대한 url 작성 

views.py

로그인을 하기 위해서는 원래대로라면 view 함수가  2개 -> 로그인 페이지, 로그인 진행

로그인 페이지 GET ,로그인 진행 POST

-> 같은 view 함수에서 request method로 분기처리됨

if else문 이용해서  만약에 요청받은 method가 POST일 때, 아닐 때

POST가 아닐 때는 로그인폼 페이지를 return해줘야함

우리는 지금까지 ModelForm을 만들었는데 이제 built-in forms을 사용할거야 

-> django authentication system 검색해서 공식문서 참고하면 AuthenticationForm 내용이 나옴

djano.contrib.auth.forms 에서 AuthenticationForm import해옴

form = AuthenticationForm()을 form 만들어주고 context에 form 담아주기

return 첫번째 인자는 request,  두번째 인자는 accounts/login.html, 세번째 인자는 context

(article이랑 구조 똑같음 form만 바뀜)

templates/accounts/login.html

create 템플릿이랑 거의 같음

action값만 다르게 해주고 h1태그를 로그인으로 바꿔줌

migrate하고 서버 켜주기! 

개발자 도구를 찍어보면 사용자이름의 name은 username 비밀번호는 password라고 나옴

usermodel이 어떻게 생겼는지는 모르겠지만 username과 password라는 필드가 있다는것을 예측할 수 있음

POST일때는, form = AuthenticationForm()의 첫번째 인자로 request가 들어가고 두번째 인자로 데이터가 들어감 

login과 create의 input이 다름 

->왜? ArticleForm ModelForm을 상속받음 키워드 인자의 구조는 결국 부모를 따라감

input의 구조가 다른것을 통해 login의 AuthenticationForm은  ModelForm을 상속받는게 아니구라..라고 추정이 가능함 Form의 상속을 받음

로그인을 할 때 받는 필드 username과 password DB에 저장 되는게 아님 그렇기때문 ModelForm을 쓸 필요가 없음 이 두개를 받아서 세션을 만드는것

username과 password가 DB에 저장되는건 로그인이 아니라 회원가입!!(헷갈리지말자)

회원가입은 ModelForm 작성한 유저의 정보가 그대로 필드에 맞춰서 저장이 됨

근데 로그인은 내 아이디와 비밀번호가 저장이 되는게 아니라 인증이 되는 데이터의 수단일뿐! 그렇기 때문에 ModelForm이 아니라 Form의 상속을 받음

그러므로 인자의 구조가 달라짐!!

인자를 넣은후에는 유효성 검사 진행

유효성 검사를 통과했다면 

AuthenticationForm이 실제 로그인을 진행해주지는 않음 로그인 진행을 위한 사전 인증 절차를 제공해주는거지 실제 session을 만들어 주지는 않음  

실제 session을 만들어주는건 login 함수야

로그인 함수의 첫번째 인자는 request, 두번째 인자는 user, 그리고 선택인자가 들어감

현재 세션에 연결하려는 인증 된 사용자가 있는 경우(AuthenticationForm을 통과했을때) login()함수가 필요함

사용자를 로그인하면 view 함수에서 사용 됨

HttpRequest 객체와 User 객체가 필요함

Django의 session framework를 사용하여 세션에 user의 ID를 저장(==로그인)

공식문서 How to log a user in 참고

django.contrib.auth에서 login을 import 해옴

유효성 검사를 통과하면 login함수 실행함

첫번째 인자 request, 두번째 인자로 user가 들어가는데 우리는 아직 user를 써본적이 없음 우선 ??로 해두고

articles:index(메인페이지)로 redirect해줌

근데 이상태에서는 로그인이 실행되지 않음 -> 1.user가 없고 2. view함수의 이름과 import한 login 함수의 이름이 같음

이걸 해결하기 위해서는 둘중 하나 바꿔줘야함! import한걸 바꿔줌  form~import~ as auth_login

view함수에서도 auth_login으로 바꿔줌

form을 통해 user data를 받았으니까 인증 된 사용자는 form객체에 있음 

form.get_user() method를 호출하면 AuthenticationForm을 통해서 인증 된 사용자(인증 된 유저 객체)가 return이 됨

세션은 장고의 db에서 만들어짐 django_session table 

컬럼이 3개 session_key, session_data, expire_date(유효기간)

여기서 브라우저한테는 session_key만 제공함 data는 서버만 가지고 있음

다음 요청에서 클라이언트가 key를 요청하면 이 key 대조를 통해 session_data를 통해 로그인을 시켜줌

로그인 해보고 개발자도구>Application을 보면 value 값과 db의 session_key값이 같음

클라이언트에는 key값만 저장됨  이 두개를 매칭해서 비교함

우리는 매요청마다 key값을 장고 서버에 보냄(로그아웃하기전까지) 그래야지 로그인 상태가 유지됨

이게 바로 쿠키를 이용해 상태를 유지하는거!

실제 session에 대한 내용, data는 장고가 가지고 있음  일반적인 쿠키 key,value는 브라우저가 가지고있음 

매번 개발자도구를 켜놓을 수 없음

인증데이터를 템플릿에서는 어떻게 출력할 수 있을까?

base.html

Hello, {{ user }}

로그인 링크

우리는 context에서 아무런값도 넘겨주지 않았지만 출력이 가능함

-> 왜? django의 settings.py에 context processors가 있는데 우리가 별도로 render 함수로 넘겨주지 않아도 장고가 템플릿이 렌더링 될 때 자동으로 호출 가능한 목록들을 넘겨줌

이중에서 auth라는 부분이 장고의 인증시스템에 관여하는 부분이고 얘때문에 user를 그냥 쓸 수 있음

Users

템플릿 RequestConteext를 렌더링할 때 현재 로그인한 사용자를 나타내는 auth.User 인스턴스는 템플릿 변수 {{ user }}에 저장됨 비로그인된 사용자는 AnonymousUser 인스턴스를 리턴함

비로그인 사용자는 userModel을 사용하지 않고 다른 userModel을 사용하고 있음

django.contrib.auth User model 객체가 있고

django.contrib.auth.models.AnonymousUser에 Anonymous class가 따로 있음

익명의 사용자를 표현하기 위한 별도의 클래스!

중요한건 템플릿에서 user를 바로 쓸 수 있는 이유는 context_processors에 이미 미리 랜더링 등록이 되어있기때문에!



### 로그아웃

session 을 Deletd하는 로직과 같음

logout 함수가 따로 있음

인자를 request 하나만 받고 반한 값도 없음

사용자가 로그인하지 않은 경우 로그아웃을 호출해도 오류를 발생시키지 않음

session data를 DB에서 완전히 삭제, 쿠키에서도 sessionid 삭제

서버에서도 지우고! 클라이언트에서도 지우고! 

클라이언트에서 왜 지워? 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고 이저 ㄴ사용자의 세션 데이터에 엑세스하는 것을 방지히가 위해서

사실 서버에서만 지워도 상관없는데 클라이언트에 남아있으면 누군가 엑세스할 수 있으니까 이걸 방지하기 위해서 

urls.py 작성

views.py

logout도 session을 삭제하는것이기 때문에 POST요청만 받음

logout 함수를 불려오기 위해서 django.contrib.auth 에서 logout을 import해옴 근데 login때와 같이 함수 이름이 겹치니까 as auth_logout 으로 바꿔줌

base.html

logout 버튼을 만들어줌

logout은 POST니까 form 만들어주고(method도 잊지말고 넣어주기) 그 안에 csrf_token, input 작성



로그인과 로그아웃에 decorator 달아주기

django.views.decorators.http 에서 require_http_methods, require_POST import 해오기

login view 함수는 GET 과 POST 둘다 받아야함

logout view 함수는 POST만 받음



근데 지금 비로그인 상태인데 로그인과 로그아웃이 둘다 보임 비로그인 상태에서는 로그인만 보이면됨, 로그아웃은 로그 되었을 때 등장하면 됨

로그인 한 사람이냐 안 한 사람이냐

1. is_authenticated attribute(속성값)

2. login_required decorator(데코레이터)

   

is_authenticated 속성

User model의 속성중 하나

모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성

AnonymousUser에 대해서는 항상 False

사용자가 인증 되었는지 여부를 알 수 있는 방법

구너환과는 관련이 없으며 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않음 단순히 로그인된 유저냐 아니냐만 ture false로 확인함

base.html

만약에 request.user.is_authenticated가 true면 로그아웃을 하고 아니면 로그인을해!

여기서 request라는 변수는 어디서 나온거야?

context_processor에 request가 있음  request는 모든 템플릿에서 다 쓸 수 있음

request에는 user가 있음

-> 요청을 하는 유저가 인증되었는지 확인하는거

먄약에 요청객체의 유저 속성값이 true면 로그인 되었다는것 아니라면 anonymous user이기 때문에 로그인을 해야함

또 로그인이 되었다면 로그인페이지로 갈 수 없어야함

login view 함수 수정

method GET과 POST를 진행하기 전에

만약에 유저가 로그인한 사람이라면  articles:index 페이지로 redirect  

로그아웃은 로그인된 사람만 쓸 수 있어야함

logout view 함수 수정

인증된 사용자라면 로그아웃을 진행

인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리하기 위해서 articles/index.html에도 똑같이 if else문에 request.user.is_authenticated를 사용함

하지만  view함수는 그대로라서 url을 타고 들어가면 쓸 수 있음

view함수 수정해야함

login_required decorator

사용자가 로그인되어 있지 않으면 settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect함

LOGIN_URL의 기본 값은 '/accounts/login/'

인증 성공 시 사용자가 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨

articles/views.py

일단 django.contrib.auth.decorators에서 login_requried를 imprt 해옴

로그인을 해야만 하는건 CRUD중 CUD!!

조회는 열어두고 create, update, delete는 @login_required를 해줌

로그인이 되어있어야만 두번째 decorator로 넘어옴

막는것 뿐만 아니라 로그인 되어있지 않으면 로그인 페이지로 redirect해줌

/?next/articles/create/ 장고가 기억해줌 너 전에 가려고 했던거 여기였잖아 그러면 너 지금 로그인하면 파라미터로 저장해둘테니까 그 다음에 보내줄게!(GET방식)

여기서 로그인이 진행되면 next 파라미터값이 같이 login view함수로 같이 요청이 감

그래서 저 값을  처리를 해줘야 저 주소를 쓸 수 있음

login.html의 action값을 없애고(중요한건 여기서 action값을 비워줘야 한다는거!!)

next 파라미터 값이 있는 경우 request.GET.get('next') 만약 이게 없다면(or) articles:indext로 redirect해줌



next 파라미터의 경우 redirect요청은 POST 방식이 불가능하기 때문에 GET방식으로 요청이 되어서 @login_requred와 @require_POST의 데코레이터 궁합이 맞지않아 405 error 발생함

그래서 둘중에 하나를 아래로 내려야함 @login_required를 if request.user.is_authenticated else~속성값으로 바꿔줌



## Authentication System 2

### UserCreationForm

주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

3개의 필드를 가짐

1. username
2. password1
3. password2

비밀번호랑 비밀번호 확인이라서 password1,2가 있음



ulrs.py

signup 작성

view.py

회원가입을 위한 페이지와 회원가입을 진행하는 페이지 2개가 있음

GET으로 요청 받아서 페이지 렌더링하는 부분, POST로 데이터 받아서 데이터 저장하는 부분

요청 받은 method가 POST라면 일단 pass

요청 받은 method가 GET이라면 일단 pass render해줌 첫번째 인자는 request, 두번째 인자는 accounts/signup.html

templates/accounts/signup

회원가입 페이지 작성 로그인 페이지랑 별반 다를거 없음

다시 views.py로 돌아와서 else 부분의 pass를 채워줌 빈 form 인스턴스를 보여줘야함

회원가입은 UserCreationForm! AuthenticationForm과 같은 위치에 있기 때문에 django.contrib.auth.forms 에서 UserCreationForm을 import 해옴

form = UserCreationForm()

context에 form 넘겨주고 return의 세번째 인자에 context 넣기

if 부분의 pass 채워주기 form = UsercreationForm(request.POST) POST형식으로 요청받은걸 form에 넣어주고 유효성 검사 진행

유효성 검사를 통과했다면 form.save() 저장함

회원가입 끝나고 articles:index 메인페이지로  redirect 해줘

User create / Article create 구조가 사실상 똑같음 사용하는 form만 달라짐

가입하고나서 자동으로 로그인된 상태로 해주려면? login함수 넣어주기

form.save() 저장하고나서 그 이후에 auth_login 함수 넣어주기 첫번째 인자는 request, 두번째 인자는 user 그럼 user는 어떻게 가져와..? user = forrm.save() 이게 바로 가입된 유저 객체

두번째 인자로  user를 넣어줌

그러면 회원가입 되면서 로그인된 상태가 됨

require_http_methods decorator 붙여주기

base.html

비로그인 상태일때 회원가입 할 수 있도록 링크 만들어주기



회원탈퇴

urls.py

delete 작성

views.py

delete 함수 작성

request.user.delete() 지우고 메인페이지로 redirect

delete는 POST 요청만 받기 때문에 require_POST  decorator

로그인한 유저만 회원탈퇴 가능하도록 if request.user.is_authenticated 넣어주기

탈퇴했다고해서 session이 지워지는건 아님(로그아웃을 해야지 지워짐)

탈퇴하면서 session도 지우고 싶다면,  삭제하고나서 auth_logout함수 불러줌 

근데 주의사항이 있다면 이 두개의 순서가 바뀌면 안됨!!

반드시 회원탈퇴 후 로그아웃 함수 호출 이 두개가 바뀌면 회원탈퇴가 안됨!!!

base.html

회원탈퇴는 로그인 되어있을때만 나타나게 해줌

form작성 ,csrf_token, input  넣어주기



회원정보 수정

UserChangeForm사용함

사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

urls.py

update 작성

views.py

update 함수 작성

회원정보수정 페이지랑 진행되는 페이지가 따로 있을것 method에 따라 분기처리됨

요청 받은 method가 POST면 일단 패스 그게 아니라면  일단 패스

페이지를 렌더링할건데 회원 수정 페이지를 return함

templates/accounts/update.html

signup이랑 구조가 같음 필요한 부분만 바꿔줌(action 값)

다시 views.py로 와서

UserChangeForm을 import 해오고 else의 pass 부분을 채워줌

form = UserChangeForm()

수정에 관련된건 기존 데이터를 받아야함 instance=request.user

user 데이터의 객체는 요청 객체에 들어가 있음

form을 context에 담아 return에 넘겨줌

article/update 이랑 accounts/update 구조가 같음 인스턴스 키워드 인자에  article  넣어줬었음

근데 회원정보수정 페이지를 보면 필요없는 부분이 너무 많아 악용될 가능성도 크고..

나머지는 admin한테만 보여야함

UserChangeForm은 출력되는 필드를 custom해줘야함

accounts/forms.py 만들기

class CustomChangeForm() 상속을 뭐 받냐면 UserChangeForm!

그럼 django.contrib.auth.forms에서 UserChangeForm을 import 해오기

그대로 상속받아서 fields만 지정해줌

model ?? fields ???

로그인, 로그아웃, 회원가입, 탈퇴 모두 유저를 이용하는데 이 유저는 도대체 어디에서 온 유저..?





if pass 부분 채워주기



request.user.is~ 

request가 들어오면 middleware를 쭉 통과하고 우리가 적어둔 url view를 통과하고(우리의 함수를 통과) 다시 response로 올라 가면서 함수, middleware를 통과함





쿠키 데이터의 조각

세션 만료 유통기한 상태

쿠키와 세션의 차이

쿠키안쪽에 세션 아이디가 있음

쿠키는 서버의 자원을 사용(우리 컴퓨터에 저장) 엥??

세션은 서버의 자원을 사용하지 않음(서버에 저장) ?잉?

이걸 왜 만든거야? 어떠한 상태를 유지하고 싶어서

HTTP 상태를 저장할 수 없음 쿠키와 세션을 이용

채팅 서비스는 websocket을 이용

쿠키는 항상 내 컴퓨터에 저장되어 있고 key-value 형태



