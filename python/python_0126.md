객체

객체는 어떤것, 상태와 동작이 같이 있는 개념

파이썬은 모든 것이 객체(object)

객체 지향 프로그래밍? 컴퓨터 프로그래밍의 패러다임 중 하나 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 



객체

파이선은 모두 객체로 이뤄져 있다.

속성은 value,attribute 동작은 method

객체는 특정 타입의  인스턴스이다. instance 사례

인스턴스는 만들어진 객체 -> 뭘로 만들어진? 클래스 -> 클래스로 만들어진 객체가 인스턴스!

클래스와 인스턴스의 차이는?

클래스는 설계도고 인스턴스는 만들어진거야

클래스는 틀이고 인스턴스는 붕어빵!

123, 900,5는int라는 클래스로 만들어진 인스턴스!  이런식으로 만들어진건 리터털

얘내ㅔ느 특별해 ! 다른 애들은 우리가 직접 클래스를 정의해서 만들어줘야함

a = 123

type(a)

<class 'int'> 

b = 'hello'

type(b)

<class 'str'> -> 우리는 지금까지 str만 봤지만 앞에 class가 있었던것!  

객체의 특징

type: 어떤 클래스로 만들어졌는가

attribute: 어떤 데이터를 가지는가

method: 어떤 함수를 할 수 있는가



객체지향 프로그래밍이란?

이전에 절차지향 프로그래밍이 있었는데 속성과 메서드가 떨어져있어서 유지보수, 코드보기가 불편하고, 협업하기가 불편해서 속성하고 메서드를 객체라는 개념으로 묶자는 의견이 나와서 객체지향 프로그래밍 탄생 

객체를 지향 하겠다는 것, 객체가 중심이 되는 프로그래밍

파이썬에서 class는 class라고 시작

그리고 class의 이름을 써줌 파스칼케이스로!(대문자로 시작하고 단어의 의미가 바뀔때마다 다시 대문자로 쓰는)

그리고 그 안쪽에다가 속성과 메서드를 써주면 설계도가 완성!

데이터의 타입은 결국 클래스!

즉, 클래스를 만든다는건 새로운 데이터 타입을 만든다는것과 같은 것

self.name 얘네가 속성, 인스턴스 변수..

self.gender

dir()이라는 함수는 어떠한 타입(클래스)에 속성과 메서드가 뭐가 있는지 다 보여줌!

dir('abc')

'title','strip',~~~

str.strip() .뒤에 쓰던 메서드가 나옴!

이중에서 __두개가 붙은걸 던더라고 하는데 얘네는 스페셜 리스트

_\_\doc__    독스트링

__ eq __ __ gt __  __ le __ __ lt __

클래스 A로 만들어진  인스턴스 a,b가 있는데

얘네를 if a> b if a=b 로 쓰고 싶어

class안에는 여러개의 속성과 여러개의 메소드가 있는데 이걸 바로 정의해주는게  얘네!

self.name 여기서 .은 dot이라는 연산자 

-> 클래스안에 있는 속성과 연산자를 연결하는 dot연산자... .(dot)하고 꺼내쓰면됨!

그럼 len()은? 얘네는 python이라는 메인 프로그램안에 내장이 되어있는것

123. __ class  __ 너의 클래스는 뭐니?  근데 이렇게하면 오류떠 왜냐면 123.은 float로 인식해서

(123.) __ class  __ 너의 클래스는 뭐니?

<class 'int'>

a = True

a. __ class __ 

<class 'bool>

dir(123)

파이썬은 내부적으로 bool이나 int랑 같음 그래서 연산자나 속성이 같음

리터럴(literal) 그대로!  리터럴은 인스턴스를 만드는 방식 중 하나

'abc'

'abc'

a =123

-> 그냥 이렇게 생성하는 방식이 리터럴이다

리터럴은 별도의 클래스를 호출하지 않고 객체를 만드는 방식 중 하나!



 클래스 어떠한 객체의 타입, 객체를 만드는 설계도, 붕어빵 틀

이 클래스를 가지고 생성을 하게되면 인스턴스, 붕어빵



class 정의하기

class Person:

​	name = 'minjin'   <- 속성

​	def run():     <-메소드

​			print('헥헥')

peson_1 = Person() 클래스의 이름을 쓰고 소괄호 열고닫고 인스턴스 생성!



print(type(person_1))

print(isinstance(person_1, Person)) person_1인스턴스가 Person이라는 클래스로 만들어졌니?

<class~main~ Person>

True



class Person:

​	cnt = 0 # 클래스 변수

​	def __ init __ (self,  name):

​		self.name = name  #인스턴스 변수

peson_1 = Person('minjin') 

peson_2 = Person('haley')

print(person_1.name)

print(person_2.name)



얘네 둘이서 cnt는 공유하고 self.name은 각각! 

클래스 변수는 이 클래스로 만들어진 모든 인스턴스가 이 클래스 변수를 가지고 있음, 공유함!

인스턴스 변수는 만들어진 하나하나의 인스턴스에 종속적인, 독립적인 변수!



__ 가 붙으면 특별한 기능을 하는 메서드

__ init __ 는 생성자!  클래스가 생성될 때 무조건 불리는 함수!!!!

클래스가 생성된다는 것, 즉 인스턴스가 만들어질때

class Person:

​	cnt = 0   <-클래스 변수

​	def \__init__ (self, name):

​		self.name = name

minjin = Person()

minjin.cnt = 3 <- 인스턴스 변수

jun = Person('jun')

print(jun.cnt)

cnt 변수를 1씩 높이고 싶으면 Person.cnt  += 1

인스턴스를 생성하는 순간 인스턴스의 네임스페이스가 생기고 인스턴스의 cnt를 쓰니까 클래스의 cnt를 쓰지못함 이런 코드는 쓰면 안된다..!



class Person:

​	cnt = 0 # 클래스 변수

​	def __ init __ (self,  name):

​		self.name = name  #인스턴스 변수

​		Person.cnt += 1

peson_1 = Person('minjin')

print(person_1.cnt) 

peson_2 = Person('haley')

print(person_2.cnt) 



인스턴스 변수에서 cnt를 만들어졌기 때문에  3 하지만 이건 잘못된 코드!

==  클래스간 비교는 구현 해줘야함 __ eq __(구글링)

is 연산자는 메모리 주소 비교 그래서 False

is  동일한 객체를 가리키는 경우 True

객체 비교하기

1.같은 값을 가졌지만 주소가 다름

2.주소가 같음



객체자체를 상호

[].sort()를 생각해보자

주어가 객체....

객체지향의 장점

간결성,직관적으로 코드를 알 수 있음

클래스와 인스턴스

클래스는 객체들의 분류

인스턴스는 하나하나의 실체, 예

==

is  동일한 객체를 가리키는 경우 True

객체 비교하기

1.같은 값을 가졌지만 주소가 다름

2.주소가 같음

if a in None:

인스턴스

변수를 가질 수 있음

인스턴스 메소드



self

인스턴스를 가르키는것 -> 클래스는 자기가 만든 인스턴스가 뭔지 알지못함, 클래스는 설계도니까

호출시 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

self는 바꿀 수 있음 근데 바꾸지 않는게 좋은 관습적인 표현!



메소드

인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달됨 ->



생성자 메소드

인스턴스를 생성할 때 호출되는 메소드

\_\_\init\__

소멸자 메소드

객체가 사라지기전에 호출되는 메소드

_\_\del__

매직 메소드

클래스

클래스 변수

객체: 속성+메소드

클래스: 변수+메소드

인스턴스: 변수+메소드

호출 시, 첫번째 인자가 호출된다...?                                                                  

인스턴스와 클래스 간의 이름공간

스태틱 메소드

호출 시, 어떠한 인자도 전달되지 않음 

인자로 아무것도 안넘기게 되어있음

모든 리스트에서 썼던 메서드는 인스턴스 메서드...

클래스 값을 조정하고 싶을때는 클래스 메서드

객체를 다루지는 않지만 다른 행위를 하고 싶을때는 스태틱 메서드

  

클래스메서드

@classmethod 를 하면 클래서메소드가 자동으로 생성

class Myclass:

​	def plus(cls): <-첫번째 인자로 클래스가 넘어오고 인스턴스를 만들지 않아도 생성 가능

​		cls.cnt += 1

클래스 매서드는 그 설계도에 있는 변수를 조작하는 역할을 함

@classmethod

데코레이터: 함수를 꾸며서 기능을 부여

함수가 여러개라서 각각의 함수에 반복해야할 작업이 있을 때 사용

매개변수로 함수가 들어오고 꾸며줄 대상함수가 매개변수

하나의 함수를 래핑하고

함수 콜 하기전에 날짜 출력하고

그 안쪽에 우리가 원하는 함수를 넣어주면됨

절취선

return해

def time_display_decorator(origin_func):
    def decorated():
        print(dt.now())
        origin_func()
        print('----')
    return decorated
@time_display_decorator
def test_a():
    print('test_a')
@time_display_decorator
def test_b():
    print('test_b')
test_a() # time_display_decorator(test_a)()  <- time_display_decorator를  불러와서 실행해
        \# time_display_decorator()
test_b()

decorator는 1급객체../

파스칼 케이스로 데코레이터 - 클래스형식으로 데코레이터가 되어있구나!



스태틱 매서드

속성 클래스 변수,인스턴스 변수를 다루지 않고 단지 기능만하는 메서드를 정의할 때

호출 시 어떠한 인자도 넘어오지 않음



객체지향의 핵심 4가지 @@@@셤

추상화 고수준의것의 저수준으로 뽑아서 만드는것..!

상속

A에게 있는 클래스의 모든것들이 B 로 넘어감

class A:

​	pass

class A(): 

class A(object):

세개 다 같은 뜻!

class A(object): object 클래스를 상속받은  A를 정의하겠슴다

하위클래스는 상위클래스의 모든 것들을 상속 받음

부모클래스의 모든것들이 상속되므로 코드의 재사용성이 높아짐

"DRY" 법칙

Don't repeat your self  코드를 반복하지 말라는 것





class 상속

professor에 talk 가 없었지만 person을 상속받아서 가능

isinstance ~은 ~의 instance입니까

issubclass ~은 ~의 subclass입니까



super() 엄마부르는거

부모클래스를 사용하고 싶은 경우

상위 클래스에 있는 걸 직접 접근하고 싶을 때

메서드 오버라이딩  부모 클래스에 있는걸 한번더 덮어써서 정의하는것 

메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함 -> 자식 이기는 부모 없다..



다중상속 여러개를 한번에 받음

먼저 상속 받은걸 사용 baby1.gene XX



다형성

하나의 클래스가 여러  객체를 받고 같은 메서드로 응답 할 수 있음

mro메서드(Method Resolution Order)

모든 클래스는 object를 상속받고 있다는것!! 끝은 object..



캡슐화

1.비슷한 기능을 하는 속성과 메서드를 묶는 작업

2.'은닉성' ->  접근에 대한 권한 

심화

응집도(choesion) 비슷한 기능을 하는 속성과 메서드가 얼마나 뭉쳐져 있는가

결합도(coupling) -> 의존성(dependency) 각각의 속성과 메서드가 얼마나 서로에게 의존되어 있느가 

A와 B가 의존성이 높다는것은  A에 문제가 생기면 B도 안됨

그러니까 모듈간 결합도는 낮을수록 응집도는 높을수록 좋다!

캡슐화를 할 때 이 두가지를 생각해야함! (하지만 이건 심화~.~)

Public Acess Modifiler다 가능

Protected Acess Modifiler  나랑 내 자식(class안에서)만 가능

Private Acess Modifiler 나만 가능

public 

언더바 없이 시작하는 메서드나 속성 일반적으로 작성되는 메서드와 속성의 대다수

protected

언더바 1개로 시작하는 메서드나 속성 

private

언더바 2개로 시작하는 메서드나 속성

name mangling 을 통해서  _{class name}__ 이런 방법으로 막음



우리가 코드를 은닉성을 띄게하고 싶다면  protected 하면 된다!



getter 뭔가를 얻는 것

setter 뭔가를 설정하는 것

getter setter 반복해서 쓰는거 귀찮으니까 



매직 메서드

__ 가 있는 애들을 매직 메서드라고 부름 특수한 동작을 위해 만들어졌기 때문에!

\__str__(self)  

인스턴스를 문자열로 취급하려고 할 때 print(p1)을 쓰면 어떤 문자열로 바꿀지 결정할 수 있음  

\__len__(self)

클래스의 길이라는 개념을 만들어줌

\__repr__(self)

\__lt__(self)   
