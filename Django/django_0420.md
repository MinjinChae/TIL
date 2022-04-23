웹엑스 설명

서버에는 두개가 있는데

Web server Request가 왔을 때 web page를 Response의 Body 담아서 응답을 주는 서버

서버가 html css js를 response의 body에 담아서 보내주면 웹 브라우저가 화면을 해석해서 보여주고 있는 것



API server Request가 왔을 때 요청한 것에 대한 처리를 하고 그 결과를  Response의 Body 담아서 응답을 주는 서버

장바구니에 담는건 web page를 주세요가 아님

유저의 장바구니에 노트북 A를 담아줘

서버는 view-model을 통해 처리를 하고 response를 줌(응답을 함) 이때 response를 어떻게 주냐?

메세지는 msg로 많이 씀

그럼 클라이언트는 아 success구나 msg는 이거구나 잘 담겼네 하고 알아차리고 

화면에서 아이콘이 바뀌거나 함

쟤는 화면을 그리는데 필요한 결과가 아니야 단지 요청한 것에 대한 과정을 처리하고 그 결과를 response의 body에 담아서 그냥 돌려주는거 이러한 역할을 하는 서버를 api server라고 함

key: value 의 json 형식으로 많이 사용함

지금까지 우리는 장고를 웹서버로 써왔고 이제 api서버로 써보자는거~

​            

HTTP

한마디로 말을 하면,  클라이언트와 서버가 서로 어떤 형식으로 데이터를 보내줄건지를 약속한 것(규약)

Hyper Text를 서로 주고받을건데 Hyper Text가 있는 웹에서 클라이언트와 서버가 어떠한 형식으로 데이터를 보내주고 받을건지 약속한 것!

HTTP말고도 다른 프로토콜

FTP, SSH, SMTP, HTTP, HTTPS

HTTS에서 S는 secure 조금 더 안전한 HTTP 프로토콜!

뭐가 더 안전해진건데? 네트워크 공부해~~

클라이언트와 서버가 서로 데이터를 주고 받으려면 '프로토콜'이 필요함

웹 개발에서는  HTTP, HTTPS가 중요함



HTTP의 기본 특성

서술형내기좋다구요?ㅠ.ㅠ

비연결성(Connetless)

클라이언트와 서버가 한 번 응답을 주고 받으면 연결을 끊음

왜 이렇게 설계했을까..? 리소스를 아끼기 위해서!

무상태(stateless)

Connetless 발생한 것, 서버가 클라이언트를 기억하지 못함(식별 불가능)

-> 매번 요청할 때마다, 내가 누군지를 서버에게 알려줘야함

---->너~~무 불편해 

그래서 등장한게 쿠키와 세션! 

쿠키 - 맨날 까먹지말고 기억해! 내 정보를 클라이언트 너가 기억해서 나(서버)한테 들고와!

너가 누구인지 너가 기억하라구~

근데 쿠키가 굉장히 쉽게 뺏겨(나의 민감한 정보들,, 내 계좌, 내 나이 등 내 프라이버시들아ㅠ)- > 보안이 취약

세션 - 그 민감한 정보, 서버가 기억해줄게 민감한 정보는 세션에 저장해넣고 쿠키에는 아이디만 저장해!



HTTP 메시지

요청

HTTP Method

클라이언트가 서버에게 Request(요청)을 보내는데 이러한 Request가 어떤 요청인지 쉽게 알려주기 위해서

데이터를 달라는거야 만든다는거야 수정한다는 삭제한다는거야 뭐야! 

R 조회  GET

C 생성 POST

U 수정 PUT

D 삭제 DELETE

서버는 HTTP method를 보고 알게됨 아~ 조회한다는거구나?! 이런식으로?

method는 요청하는거니까 Request에 담겨있어

Request는 Head와 Body 로 나누어져있어

Head 요청에 대한 부가정보, method

Body 실제 데이터를 담아서 보낼 때 Body는 있을 수도 있고 없을 수도 있어 

GET요청은 Body가 필요없어, DELETE도 Body가 필요없어

POST, PUT은 Body 필요해 

Head에는 항상 채워져있는데 Body는 그렇지않음(-> method에 따라 다름!)



Header가 뭐야?

Head에 담겨있는 key:value가 여러개 담겨있기 때문에 Headers라고 함

user-agent 나에게 요청보낸 유저는 windows에 win64비트에 chrome은 이 버전이구나~

개발자들은 user-agent를 수집해서 분석함

운영체제 정보까지 다 담겨있구나 아항~



HTTP Response

Head와 Body로 나눠짐

Head에는 Header가 담겨져있음 상태코드가 Header에 담겨서 전송됨(중요해)

상태코드는 숫자에 불과하는데 그에 대응되는 상태 메세지를 가지고 있음 status message

상태코드 상태메세지

200              ok

404            not found

상태코드는 5개의 코드로 이루어져있음

100번대 서버가 클라이언트한테 정보성 응답 

(이것만 알자) 100 -> continue

클라이언트가 서버에게 저기..서버야 나 계속 요청해도 괜찮겠어? 하고 물어보면 괜찮아 계속해! 하는 것

200번대 일반적인, 정상적인 상황

200  ->  OK 다 처리됐어! 정상이야!

201 ->  Create 클라이언트의 요청대로 리소스가 서버에게 잘 생성되었다

그래서 POST요청은 200, 201 둘다 가능 구성하기 나름

300번대 잠깐만 있어봐 너 그거하려면 뭐  조금 더 해야할거 같은데?

301 ->  Moved Permanently  너가 나한테 요청한 리소스 그 위치에 있는거 아니야! 옮겨졌어!

보통 301을 하고 서버가 redirect를 줌 

너 cat 이미지 달라고 했잖아 근데 없어 대신 우리한테 dog 이미지는 있으니까 dog 페이지를 보여줄게?(redirect)

304 -> Not Modified 수정되지 않았음 이전에 받았던 이미지를 주머니에 잘 넣어두고 또다시 그 페이지에 들어와서 이미지를 달라고 하면 서버가 너 그거 전에 봤거든? 하고 알려주면 브라우저가 어 진짜네 있었네 하고 전에 넣어뒀던 이미지 꺼내서 보는거(리소스 절약)

예 ? 브라우저 캐싱이요...? 

400번대 클라이언트가 잘못했어!!

400 -> Bad Request 클라이언트님 요청은 제대로 했는데 형식이나 내부 문법이 잘못된거같아요! url은 맞습니다요!

401 -> Unauthorized  클라이언트님 그 요청 잘해주셨는데 그거 하려면 인증부터 하고오삼~

403  -> Forbidden 권한이 막힌거 너 인증은 잘했는데 권한이 없어

404 -> Not Found 나한테 없는 리소스를 요청한 것(url)

429 -> Too Many Requests 아 요청이 너무 많아요,,ㅡㅡ

500번대 서버가 잘못했어!! 개발자야 야근해라

500 -> Internal Server Error 클라이언트 요청은 ok야 근데 안에 내부 로직이 뻥! 터졌음

503 -> Service Unavaliable  로아 터졌다



Body 웹페이지에 필요한 정보,  요청한 것에 대한 처리 정보



웹에서의 리소스 식별

리소스? 서버에 존재하는 정보, 자원, 데이터

우리는 리소스를 조회 갱신 추가 삭제 했던 것!

URI

URL 서버에 존재하는 정보가 네트워크상에서 봤을 때 어디에 있는지 나타내는거 L=located

각각의 리소스가 네트워크상에 위치해있는 정보

URN 얘는 안 써

URL구조(중요해!!!)

Scheme header에 들어있음

Host ip주소는 기억하기 어려우니까 도메인을 쓰는거야

Port 어떤 컴퓨터의 문을 열고 들어갈거니

Path 도메인과 포트를 찾았다면 그안에서 어떻게 url이 나눠지고 있는지 -> 리소스의 경로 리소스가 이 컴퓨터의 어디에 접근하면 되는지 명시하는거

Query  쿼리스트링 있을 수도 있고 없을 수도 있고~ 서버로 전송

Fragment  서버로 전송안됨 HTML 특정 부분을 보여주기 위한 방법





응답에는 상태 코드가 있음

리소스에 대한 행의를 정의함 

우리가 요청을 보냈을 때 원하는 동작이 무엇이냐는 것

GET 조회

POST  작성 

PUT 수정

DELETE 삭제 post로도 삭제할 수 있지만 delete로 삭제하는게 더 쉬움

urls.py는 뭘하겠다라는 액션이 없음 단지 자원을 표현하는 단계 

뭘 하기위해서는 method 사용

posts/1/ 이라는 url을 GET이라는 method로 보냄 -> 1번 게시글 조회

posts/1/create 이런건 restful한 api가 아님

상태코드

2,4,5를 잘 알고있어야함

2xx 정상

4xx 클라이언트에서 에러

urls.py에 없는 url을 요청한거

5xx 다 서버 잘못이야~!

1xx는 일반적인 기업에서 사용하지 않음

가장 많이 보이는건 200 ok 하여튼 정상적으로  처리되었음

201 created 새로운 데이터가 생성되었을때 (회사 내부적으로 백앤드 개발자와 클라이언트 개발자가 약속하는거라 200을 쓸 수도 있음)

401 인증되지 않은 유저가 무엇을 하려고 할 때 관리가가 아닌데 관리자 api을 쓰려고 한다거나..?

403 forbidden 권한에 대한 문제 발생

404 not found 리소스를 찾을 수 없다 = 클라이언트가 url로 서버를 요청하는거 

500 Internal Server Error 야근행~~ index out of range 내부 로직을 잘못짜서 터진거..

502 네트워크를 알아야 함 사실 많이 만나지 않는 상태코드야

503 야근행~~



데이터를 클라이언트에게 줄 때 내려준다라고 씀 데이터 내려줄게~~

URI의 구조부터는 꼭 알아야 하는 지식!!!!!!!!!!!!!!!



API -> Web API

프론트엔드에서 어떤 url로 어떤 Request를 보내면 백엔드에서 어떤 처리를 해서 어떤 Response를 내려줄게 라고 약속한 규칙

'약속' -> 약속은 깨라고 있는 거 어떻게 설계해도 기능적으로 문제가 없음

REST API 딱! 있는게 아니라 약속인데 WEB API를 설계할때의 가이드라인

직역하면 표현적인 상태 이전 ? 

웹을 하나의 거대한 프로그램이라고 생각을 해보자

우리가 웹 서핑을 하면서 오는 웹 페이지들 

웹 이라는 프로그램의 매순간순간의 상태를 보는것

그래서 표현적인 우리가 보고있는 매순간의 상태를 이전 한다는 것..? 

REST API를 사요하는 서비스를 RESTful 서비스라고 함

오늘날의 대부분을 서비스는 RESTful 서비스를 따르고 있음



이건 외워야해!!

URL은 리소스를 나타내기 위해서만 사용하고 리소스에 대한 처리는 메서드로 표현함

Document는 단수명사로, Collection은 복수명사로 표현함

이 두가지만 지키면 RESTful하게 API를 짤 수 있음

~/articles/1/edit 이렇게 쓰지마!

Document가 모여서 있는게 Collections

여러개의 article이 모여있는.. ?

article/POST x

articles/POST o



꼭 JSON만 쓰는건 아니지만 오늘날에는 JSON을 많이 사용함





rest에서 중요한건 API

어떤 서비스를 이욯하기 위해서 데이터를 어떻게 요청하고 어떤 데이터를 내려줄지 짜는거!

응답 데이터 타입

HTML -> 이제 거의 보기 힘들어..

우리는 XML, JSON 을 쓸거야 요즘에는  JSON을 많이 써

XML은 오래된 회사가 써

대표적인 서비스 목록

우리가 쓰는 모든 서비스가 API

카카오톡 네이버웹툰 유튜브 디스코드

서버에서 하는 일은 API 를 설계하고 API에 요청이 들어왔을때 어떻게 할 지 설계하는거!



JSON

자바스크립트는 key-value 형태로 쓰면 객체 



REST

rest를 지키지 않으면 취업이 안된다구...? 엉엉엉,...



django_seed django에서 모델을 만들 때 데이터를 하나하나 넣음  

음원 서비스 -> 음원 데이터를 미리 우리의 데이터베이스에 넣어둬야함

artist

album

...

shell_plus로 하나하나 create해서 데이터를 넣는건 무리..

내가 가지고 있는 데이터 파일을 장고 모델에 맞춰서 데이터베이스에 넣어주는게 django_seed

음원 서비스가 아니ㄹ더라도 미리 데이터를 가지고 있어야 하는게 있음 - 도서 조회 서비스랄까

django_seed 검색해보기 

django_seed와 항상 같이 나오는게 faker



1.이제는 템플릿을 랜더링 하지 않아



DRF를 많이 사용함

장고를 백앤드로 쓸 때는 거의 정석처럼 쓰이는거!

최근에는 DRF 말고도 많이 나왔지만 그건 넥스트 스텝이여



Postman 참고 아니구 필수라구...

실제로 요청을 하고 응답을 받는 프로그램이야 



PUT 전체 데이터 수정

PATCH 한두개? 근데 회사마다 다름



django rest frame work 앞글자만 딴게 DRF

api vesion 1 명시

django seed 라이브러리를 사용해서 데이터 생성

model을 django seed가 봄 articles모델을 니가 참조해서 각각의 필드의 데이터 타입에 맞게 20개의 데이터를 생성해서 넣어줘?

어떻게 파이썬 객체로 만들 수 있을지 만드는거?

이 씨리얼 라이저가 어떤 모델을 모델의 어떤 필드를 

many = True 여러 인스턴스를 직렬할 때

시리얼라이즈 모델에서 데이터를 가져와서 jsonresponse로 만들기 위해서 쓰는거

모델에서 가져온 데이터가 여러개 즉 쿼리셋 형태일때 파이썬 형태로 만들어주잖아 

야 이거 한개 아니고 여러개니까 너가 잘 처리해라~



Pagination

article을 조회했는데 1000개의 데이터가 있어 

<<<1,2,3,4...>>>

1번 누르면  100개 보이고

2번 누르면 100개 보이고 하는?











\# *serialize를 사용할 때 여러개의 형태가 들어갈 때* 

  \# *우리가 넘겨주는 데이터가 한개짜리가 아니라 여러개야* 

  \# *너 여러번 처리해 하는 옵션을 넘겨주는거!*



프린트를 찍어보니 

유저로부터 입력한 데이터가 이렇게 나오는구나..!

Response(serializer.data)나 (data=request.data) 에서 우리가 원하는 정보가 .data라는 attribute에 들어있다는건 약간은 암기사항인거죠?

model을 보고 판단을 함  username은 있는데 title content 이런건 없어 null True 안해줬으니까

우리 model에는 username 없어 필요없는거니까

클라이언트는 상태코드를 보고 내가 성공했는지 아니까 

response로 데이터를 넣어서 주면 데이터는 잘옴 이때 status code는 200이 default

dfr를 쓰면 csrf_token체크하지않음 !

이 인스턴스가 이 데이터로 modelform이 수정하도록 했음

 그냥 form data의 key value에 articcle  10넣어줘도 되지만 

이거 하기 싫엉

read_only_fields 읽기 전용 필드

그 곳에 읽을 수 있게 데이터를 넣어줌

content만 보냈음에도 불구하고 정상적으로 데이터가 들어감을 확인할 수 있음

빠지기 때문에 save 할 때 article=article을 넣어줌



피피티 마지막 4장 몰라도됨(count해주는거)

평가에도 안나와



그동안 ModelForm을 통해서 사용자의 요청을 받는 form을 만들었는데 이제는 이 데이터를 serializer해주는 도구=model serial 를 사용할거야! -> serializers.py를 만들고 기존의 ModelForm과 굉장히 유사한 구조의 DRF를 사용하는 ModelSerializer를 만들거야



### Django REST Framesork(DRF)

Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리

DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 동작함

Web API 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

![drf](django_0420.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-04-22%20022346.jpg)



## Single Model

### Postman

Postman 참고 아니구 필수라구...

API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼

설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성할 수 있도록 도움

->  간단히 말해서, 실제로 요청을 하고 응답을 받는 프로그램이야!





## 실습

articles/를 처리하는 view함수는 GET, POST 처리 

articles/1/ variable routing을 처리하는 view함수는 GET, PUT, DELETE 처리

url과 view 함수는 2개씩!



1. 가상환경 설정 및 패키지 설치

   

2. 설치된 app 확인



3. urls.py 작성(작성되어 있음)

   지금까지와 다르게  'api/v1/'으로 되어있음 -> 우리의 api version 1이야! 

   articles 앱의 urls들을 include 함

   articles/urls.py 만들어주기

   

4. models.py작성(작성되어 있음)



5.  Dummy Data 생성

   django-seed 라이브러리 사용해서 모델 구조에 맞는 데이터 생성

   (해당 실습에서는 migrations 파일이 이미 생성되어 있기 때문에 migrate만 진행해주면 됨)

   migrate가 되어야 seed가 됨 테이블이 있어야 데이터가 들어가니까!



6. articles/serializers.py 생성 후, ModelSerializer 작성

   Model의 필드를 어떻게 직렬화 할 지 설정하는 것이 핵심

   Django에서 Model 필드를 설정하는 것과 동일함

   drf에서 serializers를 import 해줌

   Article의 쿼리셋을 직렬화하기 위해서 AriticleListSerializer 클래스 선언

   ModelForm 쓰는 것처럼 ModelSerializer 

   Meta 클래스 작성도 동일함

   

7. GET - Article List

   urls.py 

   app_name, url name 필요없음 -> 템플릿도 없고 장고에서 쓸만한 url도 없으니까!

   views.py 

   현재 디렉토리의 models에서 Article import 해와

   article_list 함수 선언 / 첫번째 인자는 request

   전체 게시글 조회 -> articles = Article.objects.all()

   현재 디렉토리의 serializers에서 ArticleListSerializer import 해와 

   serializer 진행 -> ArticleListSerializer를 통해 serializer 인스턴스 생성하고 쿼리셋 articles이 첫번째 인자, multiple  objects니까 many=True 옵션이 두번째 인자(필수!)

   drf에 있는 response 모듈에서 Response import 해와

   전체 게시글에 대한 응답을 JSON형태로 반환 ->  데이터를 JSON형태(serializer.data)로 추출

   여기까지 하고 사이트를 요청하면 500 Internal Server Error가 발생함

   -> 왜? drf의 view 함수는 필수적으로 api_view decorator가 필요함!!!

   drf에 있는 decorators 모듈에서 api_view를 import 해와(@필수@ 빼먹지마!!)

   이 view 함수는 GET 요청에서만 허용해

   짜잔! 우리의 view 함수 이름을 따서 페이지에 있는 이름이 정해짐

   생성일, 수정일 등 안뜨게 하고싶다면 serializers의 fields를 수정해주면됨

   id랑 contetn만 필요해 -> fields = ('id', 'content', )

   페이지를 제공하는게 아니라 데이터를 제공하는 경우, get_list_or_404 사용할 수 있음

   조회하고자 하는 쿼리셋이 없으면 404 에러를 리턴하기

   django의 shortcuts 모듈에서 get_list_or_404 import 해와

   articles = Article.objects.all() -> articles = get_list_or_404(Article)

   

   

8. GET - Article Detail

   serializers.py

   상세페이지에서는 더 많은 데이터(created_at,  updated_at)를 조회하기 위해서 Article List와 Article Detail을 구분함

   -> 추가로 ArticleSerializer 정의

   (필드를 구분하지 않는다면 그냥 똑같이 써도 상관없지만 이번 실습에서는 구분해서 진행)

   urls.py

   variable routing 필요함 -> 'articles/\<int:article_pk>/' view함수의 이름은 article_detail

   views.py

   article_list 함수 선언 / 첫번째 인자는 request, 두번째 인자는 article_pk

   api_view decorator 사용, 이 view 함수는 GET 요청에서만 허용해(잊지말자)

   단일 게시글 조회 -> article = Article.objects.get(pk=article_pk) 

   이거 대신에 get_object_or_404 사용해주기!  조회하고자 하는 객체가 없으면 404 에러를 리턴하기

   import에서 get_object_or_404 추가해주고 article = get_objecrt_or_404(Article, pk=article_pk)

   serializer 진행하고 serializer된 객체의 데이터 속성 값 반환(위와 동일)

   ArticleSerializer 사용해야 하니까 import 하고 serializer 해주기, multiple object가 아니기 때문에 many=True옵션 필요없음

   

   

9. POST - Create Article 

   article_list 함수로 게시글을 조회하거나 생성하는 행위를 모두 처리 가능

   api_view decorator에 POST 추가해주기 -> 안해주면 405 에러 발생

   article_list 함수에서 method를 분리해줌(if elif문으로)

   요청받은 method가 GET일 때/ 요청받은 method가 POST일 때

   if else가 아닌 if elif로 하는 이유는 DRF가 그냥 그렇게 권해서..(명시적으로 보여주기 위해서)

   요청받은 method가 POST일 때 

   serializer 진행 

   자동완성을 보면 첫번째 인자가 insatance 근데 우리는 사용자 요청의 데이터를 넣어야 함

   -> (data=request.data)

   drf에서 status 모듈 import 해와

   유효성 검사 진행 serializer가 유효해? 통과하면 저장하고 생성된 데이터와 status code를 응답해

   여기서 status code는 201 Created 잘 작성이 되었다!

   유효성 검사를 통과하지 못했으면 에러라는 속성 값과 status code를 응답해 

   여기서 status code는 400 Bad Request 나쁜 요청이었다!

   근데 is_valid 안쪽에 raise_exception=True를 넣어주면 400을 return하는 코드가 필요없어짐

   = 여기서 문제가 발생하면 예외를 발생시켜요 그 예외가 400 Bad Request 발생시킴

   

10. DELETE - Delete Article

    DELETE에 대한 처리는 pk값이 필요하기 때문에 article_detail  함수에서 처리함

    api_view decorator에 DELETE 추가

    if elif elif 문으로 나눠주기 -> 요청받은 method가 DELETE일 때 

    method가 DELETE일 때도 get_object_or_404가 필요하기 때문에 제일 위로 올려줌

    그러면 인스턴스 객체 article을 바로 삭제해주면 끝!

    응답에 메세지를 넣어줄 수 있음

    메세지와 204 status code를 응답해줌

    

11. PUT - Update Article

    api_view decorator에 PUT 추가

    요청받은 method가 PUT일 때 

    serializer 인스턴스를 만들건데 첫번째 인자가 instance

    POST일 때는 instance가 없어서 안넣었지만 여기에는 기존 객체 article을 넣어주고

    두번째 인자에는 요청받은 데이터를 넣어줌

    유효성 검사, raise_exception 속성값 True로 바꿔주기

    저장하고 수정 된 데이터 응답하기 (별다른 status code 없음)

    

12. 데이터 베이스 초기화 후 Comment 모델 작성

    article : comment -> 1: N  -> comment 클래스에 FK 작성함

    모델은 그냥 작성하던대로 작성해

    

13. 마이그레이션 작업 후 data seed 진행

    

14. GET - Comment List

    serializers.py 

    CommentSerializer 작성

    댓글은 굳이 댓글 전체를 조회하는걸 만들 필요가 없기 때문에 그냥 CommentSerializer만 작성

    urls.py

    

    views.py

    comment_list 함수 선언

    현재 디렉토리에서 Comment 클래스 import 해와

    article_list에서 했던 것처럼 똑같은거 반복

    comments 변수 선언하고 get_list_or_404

    CommentSerializer를 import해주고 이 쿼리셋을 serializer 진행하기

    얘는 multiple object니까 many=True 옵션 잊지말고 넣어주기

    serializer의 데이터를 응답해

    api_view decoraor에 GET -> 이 view 함수는 GET 요청에서만 허용해

    (지금까지 해왔던거  반복)

    댓글에는 외래키가 있기때문에 article의 pk가 기본적으로 나옴 -> 이 1번 댓글은 12번 게시물에 달려있는거야

    

    

15.  GET - Comment List 

    urls.py

    단일 댓글 조회니까 comment_pk를 variable routing로 넣어주기

    views.py

    아까 article_detail이랑 구조가 같음

    comment_detail 함수 선언하고 첫번째 인자로 reqeust,  두번째 인자로 comment_pk 넣기

    단일 객체 조회 -> comment = get_object_or_404(Comment, pk=comment_pk)

    serializer 진행 단일 객체니까 many=True 필요없음

    serializer의 데이터를 응답해

    

16. POST - Create Comment

    urls.py

    댓글이 작성되기 위해서는 몇번째 게시글인지도 필요함 article_pk가 필요하기 때문에 또 다른 view함수를 만들어야함

    views.py

    api_view decorator는 POST

    comment_create 함수를 선언하고  reqeust,  두번째 인자로 article_pk 넣기

    CommentSerializer를 통해 serializer 인스턴스를 만들고 인자로 사용자 요청의 데이터(사용자가 입력한 데이터)를 넣음 

    유효성 검사, is_valid에 raise_exception=True 속성값 넣어주기

    유효하다면 저장하고 데이터와 201 status code를 응답해

    이렇게만 작성하면 에러가 발생함 -> 댓글을 작성하기 위해서는 몇 번 게시글에 작성했는지에 대한 정보를 가져와야 하는데 article_pk를 처리해주지 않았기 때문이야..

    => 지금까지라면 save안에 commit=False를 넣었겠지만 여기서는 article에 article 객체를 넣어주면 됨!
    
    그전에 article 객체 조회해주기!! 조회한 article객체를 save에 키워드 인자로 넣어줌
    
    해당하는 컬럼(외래키 지정한 article)에 위에서 조회한 변수 이름을 설정
    
     그래도 400 Bad Request에러 발생 유효성 검사에서 걸린거구나!
    
    유효성 검사를 할 때 CommentSerializer에서 정의된 필드들만 검사를 진행하기 때문에 추가로 넣기전에 이미 유효성 검사에서 빈값이 있음
    
    -> 유효성 검사에서 serializer 유효성 검사를 하지 않도록 빼줘야함 유효성 검사에서 pass 하고 추가로 넣고 save 하도록 -> read only field
    
    serializers.py의 CommentSerializer에서 read_only_fields하고 읽기 전용 필드로 바꾸고자하는 컬럼명을 작성함 이렇게 되면 is_valid에서는 배제되고 응답에는 포함됨
    
    



17. DELETE & PUT - delete, update Comment

    comment_pk를 받는 comment_detail 함수에서 처리

    api_view decorator에 DELETE, PUT 추가

    if elif elif 문 사용해서 요청받는 method가 GET, DELETE, PUT일 때를 나눠지고 지금까지와 동일하고 작성함



 

 

### ModelSerializer

모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut

- 모델 정보에 맞춰 자동으로 필드 생성 -> 이미 모델 정보를 알고 있기 때문에 
- serializer에 대한 유효성 검사기를 자동으로 생성
- .create() & .update()의 간단한 기본 구현이 포함됨

-> ModelForm이랑 비슷해! 모델 필드에 맞춰 응답에 대한 객체를 만들어줌



### Serializer in Shell(shell_plus 이용)

ipython이 있어야 실습하기 편함 shell_plus 실행전에 ipython 설치해주기 `pip install ipython`

#2. 작성했던  ModelSerializer를 imoprt 해줘야 함

articles 앱의 serializers에서 ArticleListSerializer import

#3. ModelSerializer를 통해 instance 생성

#4. serializer 진행

serializer를 하기 위해서는 대상 즉, 객체가 필요함 모델 인스턴스이던, 쿼리셋이던!

단일객체

1번 게시글 하나 조회하기(ORM)

이 모델 serializer의 인자로 객체(article)를 넣어줌

출력해보면 객체가 들어가있음!

serializer객체에 .data를 하면 우리가 원하는 JSON 데이터(속성값)이 나옴

이번에는 쿼리셋일때

전체 게시글 데이터를 JSON으로 줘야한다면?

전체 게시글 조회하기(ORM)

ArticleListSerializer에 인자로 쿼리셋(articles)를 넣어줌

serializer에서 data를 추출하면 에러가 나옴 

-> serializer하는 대사이 단일객체가 아니라 쿼리셋이라면 `many=True` 옵션을 넣어줘야함!!

serializer한 데이터를 만드는 이유는 이 응답을 받는 대상은 파이썬을 쓰는 사람일수도 있고, 자바를 쓰는 사람일수도 있고  다른 언어를 쓰는 사람일수도 있음 결국 JSON 으로 변환해서 써야함 변환하기 위해 준비된 파일이 이거야!



### 'many' argurment

many=True

단일 인스턴스가 아닌 QuerySet처럼 mutiple object등을 serializing하기 위해서 serializer를 인스턴스화 할 때 

many=True를 키워드 인자로 전달해야함



### api_view decorator

view 함수가 응답해야 하는 HTTP method 목록을 리스트의 인자로 받음

@api_view에 인자를 아무것도 넣지 않는다면 기본적으로 GET method만 허용함

다른 method 요청에 대해서는 405 Method Allowed로 응답함

DRF에서는 선택이 아닌 필수적으로 작성해야 해당 view 함수가 정상적으로 동작함



 ### Status Codes in DRF

DRF에는 status code를 보다 명확하고 읽기 쉽게 만드는 데 사용할 수 잇는 정의된 상수 집합을 제공

status 모듈에 HTTP status code 집합이 모두 포함되어 있음

단순히 status=201이라고 숫자로도 표현할 수 있지만 DRF는 권장하지 않음



### 'raise_exception' argument

is_valid()는 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 선택적 raise_exception인자를 사용 할 수 있음

기본적으로 HTTP status code 400을 응답으로 반환함

-> 데이터가 invalid할 때 400을 return 시키는 속성값 





## 1:N Relation

### Read Only Field(읽기 전용 필드)

어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 직렬화하는 과정에서 article 필드가 유효겅 검사(is_vlaid)를 통과하지 못함

우리가 form-data에서 넘겨주는건 content(댓글의 내용)뿐! 외래키는 안보내고 view 함수에서 처리하고 싶음

그래서 읽기 전용 필드(read_only_fields)설정을 통해 직렬화하지는 않고 반환 값, return에는 해당 필드가 포함되도록 설정할 수 있음





### 1:N Serializer

이제부터 커스텀~~

단일 게시글을 조회할 때  게시글의 정보만 뜸 -> 1:N관계에서 1쪽은 외래키가 없으니까!

근데 게시글이랑 이 게시글의 댓글 정보도 추가하고싶어!

역참조..어떻게 수정해야할까?

특정 게시글에 작성된 댓글 목록 출력하기 -> 기존 필드 override or 추가 필드 구성



case1) PrimaryKeyRelatedField

article의 pk를 참조하는 대상을 불러올 수 있음 -> comment

원래 article.comment_set.all() 의 comment_set을 기존 필드로 가져오기

무엇으로 출력할거야? serializers.PrimaryKeyRelatedField

comment는 N으로 multiple objects니까 many=True 속성 필요함 

comment_set 필드는 사용자로부터 입력을 받는것이 아니라 얘도 조회만 받아야함 -> read_only=True 속성 필요함 fields='\__all__'에 포함되어 있지 않으니까 Meta안에서 설정해주는게 아니라 인자에 속성 넣어주기

만약 comment_set 이라는 이름이 싫다면 models.py의 Comment 클래스에서 related_name 설정해주면 됨



case2) Nested relationships

모델 관계상으로 참조된 대상은 참조하는 대상의 표현(응답)에  포함되거나 중첩(nested) 될 수 있음 

