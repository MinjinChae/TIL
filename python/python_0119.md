# 함수

## 함수 기초

### 함수의 정의

 재사용성과 가독성,생산성을 위해 사용?

함수(Function)

기능을 하는 코드의 조각,묶음 매번 다시 작성하지 않고 필요 시에만 호출하여 간편하게 사용

사용자 함수(Custom Function) 

구현되어 있는 함수가 없는 경우 사용자가 직접 함수를 작성



### 함수를 사용해야 하는 이유

조건반복문으로 표현 할 수 있지만 내장함수를 활용할 수 있고 그 내장함수를 내가 다시 묶어서 표현 할 수 있음

내장함수를 활용하여 코드의 길이를 줄일 수 있음

함수,모듈,클래스 밑에 시작하는 ''' """는 특별한 기능을 함 이 함수는 어떤 함수야! 어떤 모듈이야!라는 설명을 해줌 help() docstring이 나옴 

### 함수 기본 구조

선언과 호출

1.입력

3.문서화

2.출력

### 선언과 호출

함수의 선언은 def

호출할 때는 함수이름()

함수이름(값)

예시 

지금 함수 정의 부분을 볼 필요 없음

입력값 먼저 읽고 출력값 읽음 실제로 계산되는 시점은 fun3을 호출하는 시점

그리고 그에 맞는 정의로 넘어가서 해석

실습문제 

1 함수를 정의하자는것

2 함수를 호출하자는것

숫자를 받아서 (input)

세제곱 결과를 변환(output)

호출: cube(2) cube(10) 이름을 붙여줘야함

def cube(number):

​	# n =2 가 있다고 생각하면 됨

​	return number *number\*number    number**3

print(cube(2))

1.함수의 이름

2.input의 이름

3.로직

4.결과값 

함수의 결과값

명시적인 return 값이 없으면 none을 반환하고 종료

print 

out은 출력된게 아니라 반환된거야!

return 하게 되면 값 반환후 함수 종료(중요!)

출력하는 것과 저장하는 것은 다르다!

return  vs print

return은 함수 안에서만 사용되는 키워드

print는 출력을 위해 사용되는 함수, 값을 보려고 하는 것

두 개 이상의 값 반환

코드는 위에서 부터 아래로 진행되기 때문에 return을 만나는 순간 종료됨

어떻게 하면 두개의 값을 줄 수 있을까....?

반환 값으로 튜플 사용 -> 하나의 튜플!

Parameter 이름 매개변수 인수 함수를 정의할때 ()에 들어가는것

Argument 값 전달인자 인자 정의된 함수를 호출할때 

Argument란? 함수 호출시 전달되는 값 func_name(argument)

반드시 전달되어야 하는 argument a(1,2)

값을 전달하지 않아도 되는 경우는 기본 값이 전달  a()

함수는 순서대로 각각 값을 바인딩 시킴

키워드로 지정하는 순간 위치가 이미 박살나서 에러가 생김

위치로 지정.. 키워드는  괜찮음! ->왜?

디폴트 값을 설정할 수 있음 값을 미리 정의할때 정해둘 수 있음



정해지지 않은 여러개의 Arguments 처리

몇개를 넣을지 모를때 

\* 묶는다는 연산자..!!

** dictionary로 묶을 때

사전은 시퀀스가 없음 

여기서 father,moter,me는 함수를 정의할때 def(father,mother,me)에서 '' 해야하는거 아닌가와 같은 의미

함수 정의 주의 사항

복잡한건 뒤에 둬라... 

이럴때는 name과 age의 위치를 바꿔줌 기본값이 있는게 기본값이 없는 argu에 와야한다



분해 (로직)/ 추상화

함수 input 호출:1.위치 2.키워드  정의:1.필수 2.선택(기본값) 3.많이 *(tuple) **(dictionary)

​		output 반드시 하나의 객체 반환 0? None  , , ? tuple



함수의 범위

함수는 코드 내부에 local scope를 생성하고 그 외의 공간인 global scope로 구분

함수의 가장 기본: local scope!

블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용해야함

블랙박스 밖으로 결과를 주고 싶을때는 return 해야함

global scope .py파일이

local scope 함수가 종료될 때까지 return

함수는 블랙박스 이름이 없다면 LEGB순으로 이름을 찾아나감 찾아서 쓸 수 있는데 값xx 

def func():

​	a=65

a=함수 밖에서는 쓸 수 없다

global은소스코드 전체에 쓸 수 있어서 어디서든 사용할 수 있음..

변수 수명주기 읽어보고 넘어가기

이름공간(namespace) 파이썬이 어떠한 이름을 찾을 때 이 namespace에서 찾음

namespce에서 이름을 찾을 때 이 순서에서 찾는다는거

함수내부에 a가 있나 찾고 없으면 동봉된 상위함수에서 찾아보고 여기에도 없으면 global에 있나 찾아봄

점점 큰 개념에서 찾아본다! 이게바로 LEGB룰

nonlocal은 한칸 위에 있는 애랑 바인딩해줌..



상수:변하지 않을 값 영문대문자로 적는다

student_num = 26

STUDENT_NUM = 26 얘가 상수값

class Student

함수+변수 모두

스네이크 케이스 student_user

파스칼 케이스 StudentUSer  class에 적을 때 파스칼 케이스 사용함

캐멀 케이스 studentUser 낙타는 머리가 작다......

이름을 지을  때 길어도 상관없음 

함수의 문서화(Doc-String)

내장 함수()

map 알고리즘 풀 때 엄청 많이 사용함

iterable for문 돌릴 수 있는 애들(list,tuple) dictionary는 안됨..

map(function,iterable)이자리에 들어오는 iterable한 애들한테 function을 적용시켜줌 결과를 map object로 반환

input으로 들어오는건 모두 문자열

split된 결과는 리스트니까 함꺼번에 int로 감싸주면 안됨

각 요소에 적용하고 싶은 이름을 넣음



filter 많이 사용X

 iterable한 애들한테 function을 적용시켜 그 결과 True인 애들만 걸러줌 



zip 거의 사용X

묶어주는거

zip(*iterables) iterable한 애들이 많이 들어간다는거

for문이랑 묶어서 많이 씀 짝이 지어지는 애들만 페어를 만들어줌

```python
lst = [[1,2,3],[4,5,6],[7,8,9]] 
for i in lst:
    print(i)
print('\n-----\n')
lst2 = zip(*lst) # transpose / 전치
for i in lst2:
    print(i)
print('\n-----\n')
lst3 = list(zip(*lst))[::-1] # 90도 회전 시계 반대 방향
for i in lst3:
    print(i)
print('\n-----\n')
lst4 = zip(*lst[::-1]) # 90도 회전 시계 반대방향
for i in lst4:
    print(i)
```



lamda 이름없는 익명함수? 어떠한 함수를 잠시만 쓰고 싶을 때 딱 한번만 쓰고 싶을 때  아예 사용X

return문을 가질 수 없음

1.코드의 라인 수가 줄어든다. 2.컴퓨터의 메모리양이 적다.

def 함수이름 (매개변수):	

​	return 결과:결과  

lambda 매개변수: 결과    다 가지고 있는데 함수의 이름만 없는거

(lambda x : x+1)(10)

이 자체가 함수니까 

func = lambda x : x+1

func(1)

lst = [1,2,3,4,5]

filter(lambda n:n%2,lst)

재귀함수

1.자기 자신을 호출하는 함수

2.무한히 들어가서 return이 필요하다

1개 이상의 종료되는 상황이 존재하고 수렴하도록 작성...(중요)

팩토리얼 !

재귀 함수의 주의 사항

base case에 도달할 때까지 함수를 호출함, 

모듈 파이썬 파일 .py단위로 작성한 것



패키지 모듈의 집합

모듈: 

패키지:

라이브러리: 



모듈과 패키지 불러오기 

improt module 파이썬 파일을 다 불러오는건 비효율적이야  module.

= from modeule import *  * All 이라는 뜻 (정규표현식 참조)  같은표현이지만 살짝 다름 function() 이렇게 바로 쓸 수 있음!

from module  import var, fuction, Class 이 모듈에서 ~를 불러올 수 있다

from package import module 패키지에서 모듈을 불러 올 수 있다

form package.module ~

pprint는 정렬해서 좀 더 예쁘게 출력함

*전체를 가져오겠다는 뜻..?

import math

import random

파이썬에는 들어있지만 아직 불러오지는 않은 상태라서  import로 불러옴

print min max 등 은 이미 불러온 상태

파이썬 패키지 관리자 pip 외부 패키지들을 서치하도록 도와주는 패키지 관리 시스템 =프로그램

외부 패키지 덕분에 파이썬이 강력한 언어가 됨 

$ pip install 패키지 이름 가장 최신의 배포판을 설치해줌  이게 가장 좋은거? ㄴㄴ 버전이 달라지면 안에 함수가 달라질수도 있어서 내가 개발한 버전 자체가 중요함 내가 사용한 라이브러리나 패키지의 버전을 명시해줘야함

==특정버전

==>      최신법전 설치

unistall 패키지 이름 패키지 지우기

pip list 

pip freeze pip한테 멈춰! 꼼짝마!하고 얼리는거 내가 설치한 패키지의 목록과 패키지들의 버전을 파일로 만들어줌

cmd bash에서 설치하라는 뜻

pip feeze > requirements.txt

같이 프로젝트를 하는 친구가 패키지 버전을 같이 맞추지 않으면 안되니까 그럴때 공유함

pip install -r requirrements.txt requirements에 있는 외부 모듈,패키지를 한번에 설치할 수 있음

모듈 패키지 활용하기

 패키지 

my check.py login.py

my.chekck  

my라는 파일에 ___\init\__ .py를 만들어줘야함..(시험..?) 하위버전과의 호환을 위해서

사용자 모듈과 패키지

import check를 하면 내가 만들어둔 모듈을 확인 할 수 있음

내가 체크하는것 중에 이름만 궁금한데?

from check import Name

from check import *

가상환경

우리가 프로젝트를 한다고 했을 때 프로젝트 A 에서는 django2.2버전 프로젝트B에서는 django 3.x버전을 쓰는데 하나의 컴퓨터 안에서 패키지가 똑같은데 버전만 다른 경우

각각의 따로따로 패키지를 설치할 수 있는 환경을 제공함 프로젝트 A에서는 이 가상환경을 쓰고  프로젝트B 에서는 이 가상환경을 쓰자 

venv 특정 디렉토리에 가상 환경을 만들어줌

python -m venv <폴더명>

python -m venv venv(관례는 아니고 이름짓기 귀찮아서..)

script파일에 있는 내용을 지금 바로 activate 시켜줘 라는 의미로 soruce를 사용

가상환경 비활성화는 deactivate
