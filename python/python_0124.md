# 데이터 구조(Data Structure)

메소드(method) -> 어떠한 것이 ~한다로 생각하면 됨!, 어떠한 방법 

ex. List.append(10) 리스트에 10을 추가하겠다 , String.split() String이 split을 한다.

-> S.V() 주어,동사의 형태로 생각하자

함수는 더 큰 개념 메소드는 조금 더 작은 개념

객체 안에 있는 함수가 메소드, 어떠한 객체가 하는 함수를 각각 정의한게 메소드!

## 순서가 있는 데이터 구조

 ### 문자열(String Type)

문자들의 나열(sequence of characters)

문자열은 작은 따옴표나 큰 따옴표로 활용하여 표기

문자열의 핵심 내용은 immutable 하다는 것! 문자열의 하나를 바꾸는게 불가능



### 문자열 조회/탐색 및 검증 메소드

s.find(x) x의 첫 번째 위치를 반환, 없으면 -1을 반환

s.index(x)  x의 첫 번째 위치를 반환, 없으면 오류 발생(index는 -1을 못내니까)

-> 비슷한 동작이지만 결과가 다름, 조심하기!

(cf.어떠한 상황에서 key가 없으면 에러가 나는 접근법이 있었고 get이라는 메소드를 사용하면 기본값을 주거나 없으면 none을 반환함)

s.isalpha() 알파벳 문자 여부 *단순 알파벳이 아닌 유니코드 상 Letter(한국어 포함)

s.isupper() 대문자 여부

s.islower() 소문자 여부

s.istitle() 타이틀 형식 여부

is가 있다면 '~인지' 

isalpah? 알파벳인지 isupper? 대문자인지 islower? 소문자인지 istilte? 타이틀의 형식인지 

-> boolean : True or False를 반환함

*어떠한 플래그변수를 두거나 True ,False 값을 저장하는 것들을 is를 달아두면 조금 더 가독성이 좋아짐 



### 문자열 조회/탐색

* .find(x)

  x의 첫 번째 위치를 반환, 없으면 -1을 반환함

  ```python
  'apple'.find('p')
  ```

  1 -> 모든 위치를 반환하는게 아니라 첫번째 위치만 반환한다!

  ```python
  'apple'.find('k')
  ```

  -1

* .index(x)

  x의 첫 번째 위치를 반환, 없으면 오류 발생 @.find랑 헷갈리지 말자!

  ```python
  'apple'.index('p')
  ```

  1

  ```python
  'apple'.index('k')
  ```

  ValueError : substring not found 이 문자가 존재하지 않는다



### 문자열 관련 검증 메소드

- .isalpha()

  ```python
  'abc'.isalpha()
  ```

  True

  ```python
  'ㄱㄴㄷ'.isalpha()
  ```

  True -> alpha라고해서 반드시 알파벳만 해당하는건 아님!

- .isupper()

  모든것들이 대문자인지

  ```python
  'Ab'.isupper()
  ```

  False

- .islower()

  모든것들이 소문자인지

  ```python
  'ab'.islower()
  ```

  True

- .istitle()

  공백을 기준으로 대문자로 표기 되었는지 여부를 나타내는게 타이틀을 뜻함

  ```python
  'Title Tilte!'.istitle()
  ```

  True

  

### 문자열 변경 메소드

Q. 문자열은  immutable한데 문자열 변경 메소드란 뭔가요...?

-> 해당하는 원본 문자열을 바꾸는 것이 아니라 변경된 문자열의 값을 반환한다는 것

- .replace(old, new[, count]) 

  바꿀 대상 글자를 새로운 글자로 바꿔서 반환, count를 지정하면 해당 개수만큼 시행

  ```python
  'coone'.replace('o','a')
  ```

  ​    'caane'

  ```python
  'wooooowoo'.replace('o','!',2)
  ```

  ​	'w!!ooowoo'

- .strip([chars]) 

  공백이나 특정 문자를 제거, 양쪽 제거(strip), 왼쪽 제거(lstrip), 오른쪽 제거(rstrip)

  문자열을 지정하지 않으면 공백을 제거함(' ', '\t, 'n')

  ```python
  '      와우!\n'.strip()
  ```

   '와우!'

  ```python
  '안녕하세요????'.rstrip('?')
  ```

  '안녕하세요'

- .split(sep=None, maxsplit=-1)  

  공백이나 특정 문자를 기준으로 분리  *알고리즘 문제 풀이 할 때 많이 사용!

  문자열을 리스트로 반환 

  sep는 seperate(구분자) 

  maxsplit은 내가 split을 몇 번 할 것인지 지정할 수 있음

  ```python
  a = "Life is too short"
  	a.split()
  ['Life','is','too','short']
  b = "a:b:c:d"
  	b.split()
  ['a','b','c','d']
  ```

- 'separator'.join([iterable]) 

  구분자로 iterable을 합침, 앞에 있는게 뒤에 있는거 사이로 들어감

  ```python
  '!'.join('happy')
  ```

  'h!a!p!p!y!'

  ```python
  ' '.join([3, 5])
  ```

  '3 5' 

- .capitalize() 가장 첫 번째 글자를 대문자로 변경

- .tilte() '나 공백 이후를 대문자로 변경

- .upper() 모두 대문자로 변경

- .lower() 모두 소문자로 변경

- .swapcase() 대-소문자 서로 변경

@tilte이랑 capitalize의 차이점





리스트로 반환 



tilte이랑 capitalize의 차이점

## 리스트(List)

### 리스트 메소드

리스트 메소드 리스트요소를 변경시키는것: mutable

insert 밀어줌 연산속도가 늘어짐

remove 있는 애를 찾으면 제거

pop 마지막꺼를 반환하고 제거

append,extend insert 차이점 시험@@

append는 값을 추가하고  extend는 iterable  -> 두 리스트를 합쳐줌

remove는 값을 삭제한거고  pop은 인덱스를 삭제해준것

.clear 모든 항목을 삭제

.sort  sorted의 차이 중요@

sort는 원본변경 sorted는 새로운 리스트가 반환@@

sort에는 key라는게 있다!!!

.reverse() 정렬하는 것이 아님 순서를 반대로 뒤집는 것

원본 자체의 순서를 뒤집는다. 



튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메소드만 지원

ex. append 는 사용x 



set

set은 순서가 없음 눈속임 당하지말자

set은 중복을 제거하여 서로 다른 원소의 개수를 셀 수 있는게 중요함

set은 추가할 때 append가 아니라 add

여러가지를 추가하는건 update



dictionary

append 나 index로 접근해서 가져오는 그런건 없음



얕은 복사와 깊은복사

할당

slice를 하면 새로운 리스트를 내놓음

리스트안에 그냥 숫자로만 구성되어있다면 그냥 얕은 복사를 해도 되는데 2차원으로 복잡하게 구성되어 있다면 딥카피를 해야함

import copy

deep copy를 하면 새로운 메모리에 저장이 되면서 원래 내용에는 영향이 없음 

import copy

deep_list = copy.deepcopy(o_list)

deep copy의 장점은 원래 데이터를 보존할 수 있다는 것 단점은 메모리를 많이 쓴다는 것...

그래서 deep copy를 많이 쓰면 space limit이 초과되서 문제가 틀림 (memory limit)



디버깅 @@@@@

print 문 활용 

branches 모드 조건을 커버 이상이나 이하로 했어야 했는데 초과나 미만으로 하는 등? 

for loops  반복문이 원하는 횟수만큼 진행이 되는지 반목문 자체가 돌아가는지, 반복문 안에서 값 변경이 내가 원하는대로 진행되고 있는지 이 결과가 맞는지 등 진입과 결과를 같이 봐야함

while loops for + 종료조건 이게 무한 루프에 빠지지 않았는지

function 호출이 잘 되었는지, 파라미터, 결과 // type

syntax error(Indentation) 

print함수 활용

특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

5줄 초기화

10줄 반복 값 결과

5줄 출력

코드를 작성하다가...

에러 메세지를 발생하는 경우 

해당 하는 위치를 찾아 메세지를 해결

로직 에러가 발생하는 경우

문법 에러 

EOL 얘가 안끝나고 잇어

EOF 파일이 안끝나

예외

ZeroDivisionError 0으로 나누고자 할 때

NameError name_error 변수를 선언하지 않았 을때namespace상에 이름이 없을 때. 이름을 잘못짜거나 잘못된 명령어 등등

index error

예외 처리

try문  문제가 될 가능성 있는 것을 전부  try 에

except절 문제가 발생하면 except에 



@@@@@

try  이거해 명령문

except 에러가 발생하면 이렇게해

else 에러가 터지지 않으면 이렇게 해(except가 발생하지 않았을때)

finally 에러가 터지든 터지지 않든 이걸 실행해

as는 별명을 붙이는거

발생하는 에러를 변수 1이라고 부르는거

발생하는 에러를 변수 2라고 부르는거

import ramdom as rd

에러가 나서 프로그램이 끝난건 정상적으로 끝난게 아님

except문 따라서 정상적으로 종료가 됨

value error를 쓰지 않으면   try에서 발생하는 모든 예외 상황들을 exccept에서 처리해줌

근데 이렇게 쓰는 건 좋지 않음.. error 내가 상상,생각할 수 있는 에러인지 그게 아닌지 구분이 안됨

어떠한 에러는 내가 핸들링할 것 인지 알고 쓰는게 좋음

except문으로 여러 에러를 잡을거라면 작은범위부터 써줘야 차례차례 잡힘

raise는 파이썬이 터지기전에 내가 에러를 발생시켜버리는거

내가(사용자가) 에러타입을 정할 수 있음 에러가 발생하면 그 에러가 정의된 except문으로!

 항상 assertioerror를 낸다

assert 표현식(조건식), 메시지

​               True False

상태검증에 사용 여기 들어간게 False면 assertionerror를 낸다

코드를 짜면서 불안한 부분들에 코딩하면서 가는 용도로 많이 사용함

assert는 assertionerror를 내고 raise는 다양한 에러를 받을 수 있다!!



