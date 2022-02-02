# Python 기초

## 파이썬 개발 환경(Python Environment)

### 파이썬(Ptyhon)

#### 파이썬이란?

쉽게 배울 수 있음, 타언어보다 간결함, 인터프리터 언어, 객체 지향 프로그래밍

인터프리터 언어 vs 컴파일 언어(컴파일러)



인터프리터 언어:  코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음(한줄 읽고 번역해서 실행하고 또 한줄을 읽고 번역해서 실행함) 

컴파일 언어:사용자가 입력한것을 컴퓨터가 변환을 해주는것을 컴파일러 (ex.C,C++)

컴파일 언어는 작성한 모든 소스코드를 한번에 컴파일러가 기계언어로 변경해서 실행파일을 만들고 나서 실행을 하여 빠름 

JAVA는 인터프리터 언어이면서 동시에 컴파일 언어

객체 지향 프로그래밍  / 절차 지향 프로그래밍 / 함수형 프로그래밍

모든 프로그래밍은 절차를 지향함(ex.C언어, 포트란) -> 불편해짐 -> 데이터+함수를 묶어버리자! 객체 지향 프로그래밍을 쓰자! (유지보수가 쉬움) -> 프로그래밍의 크기가 커져서 객체 지향을 설계하기 복잡해짐 -> 함수형 프로그래밍

하지만 여전히 객체 지향 프로그래밍을 쓰고 있음 



## 파이썬 개발환경

디버깅이란? 실행을 했을 때 내가 원하는 결과가 나오지 않을 때 오류를 찾아내기 위한 테스트 과정을 뜻함

주피터 랩은 데이터 분석,머신러닝,딥러닝에서 사용함

Pycharm  파이썬에 특화됨(나중에 알고리즘에서 사용함)

Visula Studio Code MS에서 내놓은 코드를 편집 할 수 있는 코드 전용 메모장, 거의 모든 소스코드 포맷을 지원함



## 기초 문법

#### 코드 스타일 가이드

 코드를 어떻게 작성할지에 재한 가이드라인,파이썬에서 제안하는 스타일 가이드(PEP8)

일관적인 코드 작성스타일이 중요!  -> 작은따옴표,큰따옴표의 통일, 들여쓰기는 4칸!



#### 변수(Variable)

어떻게 저장하고 이름 지을까?

dust(상자) = 60 -> 왼쪽에 이름을 지어주고 오른쪽에 값  '='는 같다가 아니라 '할당'한다는 뜻!

- 변수란? 컴퓨터 메모리(Ram) 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름 ->  box 라고 쉽게 생각하면 됨

객체(object): 숫자,문자,클래스 등 값을 가지고 있는 모든 것 -> 그냥 쉽게 things로 생각하자 어떠한 것을 지칭하고 있구나!정도로 생각

- 변수는 할당 연산자(=)를 통해 값을 할당(assignment)

​      -type() 변수에 할당된 값의 타입

​      - id() 메모리 주소



#### 변수 연산

```python
i = 5
j = 3
s = '파이썬'
```

숫자+숫자

```python
i + j
```

8

```python
i = i - j
i
```

2

```python
i * j / 3
```

5.0

문자+문자(문자를 연결) 

```python
'안녕' + s 
```

'안녕파이썬'

문자*문자

```python
s = s * 3
s
```

'파이썬파이썬파이썬'

```
s = 'Python'
s + ' is fun'
```

'Python is fun'

*변수의 타입을 생각하는게 중요! 오른쪽에 할당한다고 생각



#### 변수 할당

- 값은 값을 동시에 할당할 수 있음

```python
x = y = 1004
print(x,y)
```

1004 1004

- 다른 값을 동시에 할당할 수 있음(mutiple assignment)

```
x, y = 1, 2
print(x, y)
```

1 2

```
x, y = 1
```

TypeError:cannot upack~  풀어 나가려고 했었는데 풀 수 없었구나

```python
x, y = 1, 2, 3
```

ValueError:Too many values to unpack~ 언팩 하기에는 너무 많은 값이 있다



#### 실습 문제

x = 10 y = 20 각각 값을 바꿔서 저장하는 코드를 작성하시오.

쉽게 물과 우유라고 생각했을때 그릇을 가져와서 물을 그릇에 옮겨 담고 우유를 물 상자에 옮기고 그릇에 있던 물을 우유에 담는..?

방법 1)임시 변수 활용

```python
x, y = 10, 20
tmp = x
x = y
y = tmp
print(x, y)
```

20 10

방법 2) y, x = x, y 각각 값을 넣어준다 Pythonic!

```python
x, y = 10, 20
y, x = x, y
print(x, y)
```

20 10



#### 식별자(Identifiers)

변수(박스)의 이름을 어떻게 지을까? 

규칙

- 식별자의 이름은 영문 알파벳,언더스코어,숫자로 구성

- 첫 글자에 숫자 올 수 없음

- 길이제한 없고 대소문자를 구별

- 키워드/예약어는 사용 못 함

  False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, form, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

RedApple (x) camel case

red_apple(o) snake-case 

- 내장함수나 모듈 등의 이름으로 만들면 안됨 (ex.print = 5)



#### 사용자 입력

input([prompt])

- 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

- 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음

- 반환값은 항상 문자열 형태로 반환

```python
name = input('이름을 입력해주세요 : ')
print(name)
```

이름을 입력해주세요 :  채민진

채민진

```python
type(name)
```

str



#### 주석(Comment)

- 한 줄 주석 : #을 입력

- 여러 줄의 주석 : 한 줄씩 #을 사용하거나 """  """ 또는 ''' ''' 입력

주석 꼭꼭꼭 달기...!! (습관가지기)



## 파이썬 자료형(Python Datatype)

#### 자료형 

- 불린형(Boolean Type) True/False 

- 수치형(Numeric Type) 

  int(정수), float(부동소수점, 실수), complex(복소수)

- 문자형(String Type) 

- None 

  

### None

값이 없음을 표현하기 위한 타입

```python
print(type(None))
```

<class 'NoneType'>

```python
a = None
print(a)
```

None



### 불린형(Boolean)

#### 불린(Boolean)

- True/False값을 가진 타입

- 비교/논리 연산에서 활용됨
- 비어 있으면 False로 반환됨 -> 0, 0.0, (), [], {}, ' ', None

bool() 함수

bool(0) False  

bool(1) True

bool(-1) True 

bool(' ') False

 bool([]) False

bool([1,2,3]) True -> 리스트가 비어있지 않기 때문에



### 수치형(Numeric Type)

#### 정수(Int)

모든 정수의 타입은 int, 매우 큰 수를 나타낼 때 오버플로우가 발생하지 않음=슈퍼계산기

진수표현 

2진수: 0b

8진수: 0o

16진수: 0x



#### 실수(Float)

정수가 아닌 모든 실수는 Float타입, 실수 연산 과정에서 Floating point roundig error이  발생함

값 비교하는 과정에서 정수가 아닌 실수인 경우 주의하기

```python
# 왼쪽의 계산 결과와 오른쪽 값은 같은 값일까?
3.14 - 3.02 == 0.12
```

False -> 3.14-3.02 =0.1200~001 실수체계의 표현 때문에 정수가 아닌 실수를 계산 할 때는 이를 꼭 고려하자

절대값으로 표현하고 엄청 작은 수보다 작은지 확인하거나 math 모듈 활용하기!

```python
#1. 임의의 작은 수
abs(a - b) <= le-10
```

True

```python
#2. system상의 machine epslion
import sys
print(abs(a - b)) <= sys.float_info.epsilon
print(sys.float_info.epsilon)
```

True

```python
#3. Python 3.5이상
import math
math.isclose(a,b)
```

True



#### 복소수(Complex)

실수부와 허수부로 구성된 복소수는 모두 complex 타입 ->이런게 있구나.. 정도로 생각하기



### 문자열(String Type)

- 모든 문자는 str타입, 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기

- 문자열을 묶을 때는 동일한 문장부호를 활용(문장부호 통일)

- Immutable 어떠한 값이 불변하다 ,특정 값 하나만 바꿀 수 없다, 중간을 바꿀 수 없다!

- Iterable 반복해서 표현 가능 for문에서 사용 가능

​       ->이 두가지 특징은 반드시 기억하자



#### 중첩따옴표(Nested Quotes)

따옴표 안에 따옴표를 표현할 경우

작은 따옴표가 들어 있으면 큰 따옴표로 문자열 생성, 큰 따옴표가 들어 있으면 작은 따옴표로 문자열 생성



####  삼중따옴표(Triple Quotes)

작은 따옴표나 큰 따옴표를 삼중으로 사용함 ''' ''' 

-> 문자열 안에 작은 따옴표나 큰 따옴표를 사용할 수 있고 여러 줄을 사용할 때 편리함



#### Escape sequence

문자를 나열을 했는데 특별한 기능을 가지게 되는 문자열 

엔터를 표현하고 싶은데 표현 할 방법이 없네? 

\n new line 줄바꿈

\t tab 탭

\r 캐리지리턴  ex. abce \r fg  fg가 맨앞으로 감

\0 널(Null)

\\\ \ (역슬래시)

\\\' 단일인용부호(')

\\" 이중인용부호(")

```python
print('철수 \'안녕\'')
```

철수 '안녕'

```python
print('이 다음은 엔터.\n그리고 탭\t탭')
```

이 다음은 엔터.

그리고 탭	탭



#### String Interpolation

문자열 사이에 변수를 넣고 싶을 때 사용

- %-formatting 거의 대부분 타 프로그래밍 언어에서 쓰임, 불편함

  ```python
  print('Hello, %s' % name)
  print('내 성적은 %d' % score)
  print('내 성적은 %f' % score)
  ```

  Hello, Kim

  내 성적은 4

  내 성적은 4.500000

- str.format() {} 세줘야해서 불편함

  ````python
  print('Hello, {}! 성적은 {}'.format(name,score))
  ````

  Hello, Kim! 성적은 4.5

- f-strings : python 3.6+ (굉장히 잘 쓰니까 연습해두기, 이걸로 쓰기ㅎㅎ)

  ```python
  print(f'Hello, {name}! 성적은 {score}')
  ```
  
  Hello, Kim! 성적은 4.5



#### None

결과가 없다는 것, 반환 값이 없는 함수에서 사용



## 컨테이너(Container)

#### 컨테이너(Container)정의

여러 개의 값을 담을 수 잇는 것(객체)

순서가 있는 데이터 (Ordered) vs 순서가 없는 데이터 (Unordered)

순서가 있는 데이터 시퀀스형 : 리스트,튜플,레인지

순서가 없는 데이터 비시퀀스형 : 셋,딕셔너리

순서가 있다 != 정렬되어 있다.  순서가 있는거랑 정렬은 다른거!



# 시퀀스형 컨테이너(Sequence Container)

## 리스트(List)

### 리스트(List) 정의

박스가 붙어있는거  컴퓨터 언어는 0부터 센다는점 주의하기!

생성된 이후 내용 변경이 가능 -> 가변자료형

항상 대괄호 형태로 출력

### 생성과 접근

리스트는 대괄호([ ]) 혹은 list()를 통해 생성

순서가 있는 시퀀스로 인덱스를 통해 접근함

값에 대한 접근은 list[i] 

처음 값을 알고 싶을때 list[0] / 맨 뒤에 값을 알고 싶을 때는 list[-1]

Negative index 길이가 뭔지 몰라도 -1하면 맨 끝에 있는 애가 나옴

Positive index 는 0부터 시작하지만 Negative index는 -1부터 시작하는거 주의하기!



## 튜플(Tuple)

### 튜플(Tuple) 정의

리스트와 비슷한데 수정 불가능, 불변하다!  -> 불변 자료형 (immutable)

값에 접근은 가능하나 값을 변경하는건 불가능함

 ### 생성과 접근

소괄호(()) 혹은  tuple() 을 통해 생성

수정 불가능한 시퀀스로 인덱스로 접근 가능

값에 대한 접근은 tuple[i]

단일 항목의 경우 반드시 쉼표를 붙여야함

```python
a = 1,
print(a)
print(type(a))
```

(1, )

<class 'tuple'>

복수항목의 경우 마지막 항목에 붙은 쉼표는 불필요함

```python
b = 1,2,3
print(b)
print(type(b))
```

(1, 2, 3)

<class 'tuple'>

### 튜플 대입(Tuple assignment)

우변의 값을 좌변의 변수에한번에 할당하는 것, 튜플은 일반적으로 파이썬 내부에서 활용된다!

*리스트와 튜플의 차이점은  자료변경 가능/불가능 이라는 점!



## 레인지(Range)

### 레인지(Range)

숫자의 시퀀스를 나타내기 위해 사용

- 기본형 : range(n)  -> 0부터 n-1까지의 숫자의 시퀀스

- 범위 지정 : range(n, m) -> n부터 m-1까지의 숫자의 시퀀스

- 범위 및 스텝 지정 : range(n, m, s) -> n부터 m-1까지 s만큼 증가시키는 숫자의 시퀀스

  스텝 얼만큼 건너 뛸 수 있는지 설정 가능

@(range 문제 내기 좋을듯...)



## 패킹/언패킹(Packing/Unpacking)

### 패킹/언패킹 연산자(Packing/Unpacking)*

모든 시퀀스형 즉,순서가 있는 데이터들(ex.리스트,튜플 등) 은 패킹/언패킹 연산자*를 사용하여 패킹 또는 언패킹이 가능 

-> 패킹 : 묶어주는거 언패킹 : 짐풀기

언패킹의 경우 튜플 형태로 대입 ->튜플로 묶어두면 순서가 변하지 않기 때문에 이 형태로 언패킹을 한다

패킹 할 때는 내마음대로 내마음대로 대입 가능!

나머지 항목들이 별 기호에 표시된 변수에 리스트로 대입됨

```python
x, *y = 1, 2, 3, 4
print(x)  1 (int)
print(y)  [2,3,4] (list) 
```



```python
a =(1, 2, 3, 4, 5)
x, *y = a
print(x) 1
print(y) [2, 3, 4, 5]
```



# 비시퀀스형 컨테이너(Associative Container)

## 셋(Set)

### 셋(Set)

중복을 제거한다는것!!! 중요한 특징

순서없이 해시가능한 객체를 담을 수 있음

담고있는 객체를 삽입 변경,삭제 가능 -> 가변자료형(mutable)

수학에서의 집합과 동일한 구조

### 셋 생성

중복없이 순서가 없는 자료구조

중복 값 제거 -> 순서를 보장 할 수 없음, 순서가 중요한 경우에는 사용할 수 없음

순서가 없어 인덱스 접근이 절대 불가능함!!

중괄호({}) 혹은 set()을 통해 생성함

빈 중괄호는 Dicitionary

```python
blank = {}
print(type(blank))
```

<class 'dict'>

### 셋 활용

알고리즘에서 중복 제거 할 때 도움됨

set을 사용하는 순간 순서가 사라짐

이런 경우 수동으로 반복문과 조건문을 확인할 필요가 있다(가나다 순이다 라고 생각하면 안됨!!)



## 딕셔너리(Dictionary)

### 딕셔너리(Dicitonary)

견출지(key) 이름표가 붙여진 박스(value)

키-값이 쌍으로 이뤄진 객체를 참조함

사전은 단어-뜻의 조합

value에는 숫자,리스트 뭐든 들어갈 수 있음

key는 immutable한 데이터만 활용 가능 ->리스트 들어갈 수 없음



### 딕셔너리 생성

중괄호({}) 혹은 dict()을 통해 생성

```python
dict_a = {}
print(type(dict_a))
```

<class 'dict'>

```python
dict_b = dict()
print(tpye(dict_b))
```

<class 'dict'>

key를 통해 value에 접근함

```python
dict_a = {'a': 'apple', 'b': 'banna', 'list': [1, 2, 3]}
dict_a['list'] #딕셔너리명 대괄호 작은따옴표에 key값
```

[1, 2, 3]

```python
dict_a = {'a': 'apple', 'b': 'banna', 'list': [1, 2, 3]}
dict_a['list'][0] 
```

1



## 형 변환(Typecasting)

### 자료형 변환(Typecasting)

암시적 형 변환 : 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 1.편하다 2.위험한데?

명시적 형 변환 : 사용자가 직접 의도적으로 자료형을 변환 

### 암시적 형 변환(Implicit Typecasting)

```python
True + 3  #True를 1로 바꿔서 계산해줌 왜? 편하라고
```

4

```python
3 + 5.0  #3은 int고 5.0은 3을 float로 바꿔서 계산해줌
```

8.0

### 명시적 형 변환(Explicit Typecasting)

- str, float -> int

- str, int -> float
- int, float, list, tuple, dict -> str



# 연산자(Operator)

핵심은 데이터를 조작할 때 쓰는것

### 산술 연산자

\+ 덧셈

\- 뺄셈

\* 곱셈

/ 나눗셈 -> 나눗셈은 항상 결과가 float!

// 몫(소수점 이하의 수를 버리고 정수 부분의 수만 구함)

% 나머지

** 거듭제곱

(// 몫 % 나머지 이게 바로 핵심!!)

특히 %(modulo) 홀수와 짝수를 구분할 때 사용함!

divmod()

```python
print(divmod(5, 2))
qutoient, remainder = divmod(5, 2)
print(qutoient, remainder)
```

(2, 1)

2 1

### 비교연산자

값을 비교하고 True,False값을 리턴함

< 미만

<=  이하

\> 초과

\>=  이상

== 같음 ( =는 할당연산자 ==같음)

!= 같지않음

is 객체 아이덴티티

is not  객체 아이덴티티가 아닌 경우

### 논리 연산자

A and B A와 B 모두 True시, True

A or B  A와 B 모두 False시, False

Not True를 False로  False를 True로

일반적으로 비교연산자와 함께 사용됨

```python
num = 100
num >= 100 num % 3 == 1
```

True

### 논리 연산자 단축평가  

결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째  값 반환!

and 모두 True여만함

or 하나라도 True면 됨

```python
a =  5 and 4
print(a)
```

4  ->and는 둘다 True여야함 5가 True인걸 봤는데 뒤에꺼까지 봐야함 그래서 4가 나옴

```python
b =  5 or 3
print(b)
```

5   ->or 는 둘중 하나면 됨 5에서 True인걸 확인했으니 5

```python
c=  0 and 5
print(c)
```

0  ->0이 False인게 확정 되었으니까 0

```python
d=  5 or o
print(d)
```

5  ->5에서 이미 True 이니까 뒤에 볼 필요 없음 

만약 0 or 5 였다면 뒤에꺼에따라 결과가 달라지니까 뒤에꺼도 봐야함 그래서 5가 나옴

### 복합 연산자

연산과 대입이 함께 이뤄짐

```python
cnt = 0
while cnt < 3:
	print(cnt)
	cnt += 1
```

0

1

2

### 식별 연산자

is연산자를 이용해 객체인지 확인 가능함

```python
x = 3
x is None # 특정 변수가 비어 있는지 확인하기 위해서는 x == None이 아닌 x is None을 사용
```

False 

### 멤버십 연산자

포함 여부 확인

in

not in

### 시퀀스형 연산자

산술 연산자(+)

리스트에 합쳐주고 튜플에 합쳐줌 

반복 연산자(*)

곱하기는 반복

range는 안됨!!!!!

### 인덱싱

특정 인덱스 값에 접근

IndexError는 없는 인덱스에 접근한 것

### 슬라이싱

특정 단위로 슬라이싱

```python
[1, 2, 3, 5][1:4]
```

[2, 3, 5]

```python
(1, 2, 3)[:2]
```

(1, 2)

시퀀스를 k간격으로 슬라이싱

```python
[1, 2, 3, 5][0:4:2]
```

[1, 3]

```python
(1, 2, 3, 5)[0:4:2]
```

(1, 3)

s[::] 

s[::-1]

### set 연산자

집합 연산자 거의 쓸 일 없음..

| 합집합

& 교집합

\- 여집합

^ 대칭차

###  

출력된 결과로만 보면 안됨

제어문

위에서부터 아래로 순차적으로 수행

선택적으로 실행하거나 계속하여 실행하는 제어가 필요함

순서도로 표현 가능 

조건문 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

연산자를 사용 num=3 >=3 <=3 >3 <3

if <expression == True>:

​	#Run this Code block

else:

 

반드시 : 사용 그리고 들여쓰기 조심!

그냥 input('숫자를 입력해주세요 : ')

타입이 str 그래서 int로 감싸주고 형변환을 해줘야함



복수조건문  복수의 조건식을 활용할 경우 elif를 활용

여기서 유의할 점은 else에는 expression이 들어갈 수 없다 else는 조건이 들어갈 수 없다는것

else는 나머지 모든것이기 때문에 열려있어야함

SyntaxError는 문법오류

반복문

while for의 차이는?

반복문은 특정한 조건에 도달할때까지 반복하는거

while문은 조건식이 참인 경우 반복적으로 코드를 실행

별표 반드시 종료 조건이 필요!!!



파이썬튜터 활용

실습 

숫자로 활용하고 싶다면  int로 형변환 필요

어떤값을 초기화 하는게 좋을지 생각하는것이 중요!!



for문 시퀀스를 포함한 순회가능한 객체요소를 모두 순회함

변수의 이름으로 값이 할당된다

for문 단순순회 ,range사용한 인덱싱 두가지 방법이 있으니 꼭 기억하자!!

range(len   많이 씀! happy 면 len 5 0,1,2,3,4

print 함수는 자동으로 줄 바꿈..!

print(     ,end='\n' )

print(   ,end=' ') h a p p y

딕셔너리 순회

중요! 딕셔너리는 기본적으로 key를 순회하며 key를 통해 

모든 키를 나에게 줘

모든 value 를 나ㅔ게줘



enumerate 순회

i=0 i+=1 

0부터 시작해서 계속 1씩 증가하는 것을  idx에 넣어줌

enumerate 의 짝꿍은 for문



List Comprehension 

이해 이해력 포함 압축

리스트를 잘 이해해서 압축해서 쓸 수 있는 표현 -> 코드줄이기

1번까지는 추천..ㅎ



반복문 제어

break loop exit 반복문을 종료

continue  다음 반복을 수행

pass 아무것도 하지 않음 syntax error를 피하기 위해서 사용 

else  if의 조건문이 수행이 되냐 안되냐 끝까지 반복문을 실행한 이후에 else문 실행 break에 걸리면 else문이 실행안됨

if else로 연결되는것이 아니기 때문에 else문 들여쓰기 하지 않아도 됨

for vs while

for는 반복 가능한 애들을 꺼내준다 통(컨테이너)을 어떻게 만들지 생각하기

while은 어떠한 조건이 참일 때 실행한다 -> 종료조건(거짓) 조건을 어떻게 설계할지 생각하기

=> 결과 변수를 초기화하는데 많은 생각을 해야함...



```python
        numbers = [1,2,3,4,5]
# for num in numbers:
#     if num == 3:
#         continue
#         print(num)
#     else:
#         print(num)
# for num in numbers:
#     if num == 3:
#         pass
#         print(num)
#     else:
#         print(num)
for num in numbers:
    if num == 3:
        pass
```



함수 

특정 명령을 수행하는 코드의 묶음

def 써서 정의하는거

 이 함수가 여러개 모인게 모이듈

.py가 모인 덩어리가 모듈

.py 이 묶인게 패키지

패키지가 묶인게 라이브러리
