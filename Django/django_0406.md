# Django 03

두번째는 redirect가 보낸거 요청을 보냄 "나 detial 페이지가 보고싶어" -> 응답

글 쓰고나서 요청이 또 왔으니까 detail view함수가 실행이 되고 두줄이 늘어남



## Django Form

지금까지 HTML form, input을 통새서 사용자로부터 데이터를 받았지만 입력된 데이터의 유효성을 검증하고 검증 결과와 함께 다시 표시해야함 

-> 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있기 때문에

숫자쓰세요~ 싫엉

사용자가 입력한 데이터 검증 -> 유효성 검증

유효성 검증을 쉽게 만들어주는 툴을 제공하는게 바로 Django Form



Django's forms

유효성 검사 도구 중 하나

중요한 방어 수단

유효성 검사를 단순화, 자동화 할 수 있는 기능 제고

직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함

1.랜더링을 위한 데이터 준비 및 재구성

2.데이터에 대한 HTML  forms 생성

3.클라이언트로부터 받은 데이터 수신 및 처리



Model Class를 작성했듯이 Form Class를 작성해야함

Form내 field, field배치 디스플레이 widget label 초기값

유효하지 않은 field에 관한 에러메세지를 어떻게 작성할 것인지 결정



가상환경 실행

앗 서버 켜기전에 migrate!!

런서버



articles앱에 forms.py? 없는데..?

기본적으로 만들어지지도 않았고 만든적도 없어

forms.py 만들어주기

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



