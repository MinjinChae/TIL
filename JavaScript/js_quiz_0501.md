1. 브라우저가 뭐야, 브라우저에서 할 수 있는 일

   url로 웹을 탐색하여 서버와 통신, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어

   돔조작, 봄조작

2. 돔이 뭐고 어떤 구조로 되어 있는지

   웹 페이지에 나타난 HTML 문서 전체를 각각에 대해 객체로 나타낸 것 head, meta, body 각각의 객체들이 트리구조로 이루어져있는것

3. var / let / const의 차이점은?

   var - 재할당, 재선언 가능, 함수 스코프

   let - 재할당 가능, 재선언 불가능, 블록 스코프

   const - 재할당, 재선언 둘다 불가능, 블록 스코프

4. var의 문제점? 호이스팅이 뭐야? 

   호이스팅이 일어나요!

   변수 선언전에 참조할 수 있는 상황을 말함 -> undefined 반환

5. 원시타입의 종류, 참조타입의 종류

   원시타입: number, boolean, string, null, undefined, symbol

   참조타입: objects - array, function

6. null의 typeof 결과는?

   object / undefined -> undefined

7. 일치 비교 연산자와 동등 비교 연산자의 차이는?

   === 엄격한 비교-> 타입이랑 값을 모두 같은 값인지 비교함

8. for in / for of의 차이는?

   for in : 객체의 속성을 순회 

   for of : iterable한 객체를 순회하는데 사용함 -> array map set string

9. 자바스크립트에서 함수의 특징은?

   일급객체 -> 1.변수에 할당이 가능하다. 2. 다른 함수의 인자로 들어갈 수 있다.(함수의 매개변수로 전달 가능하다.)  3.반환 값이 될 수 있다.

10. 함수 선언식과 표현식의 차이점

    함수 선언식: 호이스팅 발생, 익명함수 ㄴㄴ 

    함수 표현식: 호이스팅 ㄴㄴ -> reference error, 익명함수 ㅇㅇ -> var를 쓰면 type error

11. 매개변수보다 인자의 개수가 적을 경우 어떻게 출력?

    undefined

12. 함수 호이스팅 어떤 에러가 나는거야?

    

13.  화살표 함수 어떤 경우에 무엇을 생략할 수 있는지?

    1. function 생략가능, 2. 매개변수가 한개일때 () 생략가능 3. 몸통에 들어가는 표현식이 하나면 {}, return  생략가능

14. 배열의 가장 뒤에 요소 추가 제거 하는  method

    push pop

15. 배열의 가장 앞에  요소 추가 제거 하는  method

    unshift shift

16. forEach의 특징은?

    배열의 각 요소를 순환하면서 콜백 함수를 실행함, 반환 값이 없는 메서드

17. forloop for of forEach 각각의 특징과 차이점은?

    for loop 인덱스를 활용해서 배열의 요소에 접근

    for of 인덱스 없이 배열의 요소에 바로 접근

    forEach break contine 사용 불가능

18. key에는 뭐? value는?

    string, 전부 다

19. js 객체는 무슨 형태?

    JSON

20.  구조 분해 할당

    ```
    const userInformation = {
    name = 'minjin',
    userId = 'abcdefg123',
    phoneNumber = '010-2345-6789',
    email = 'ssafy@ssafy.com',
    }
    ```

    ```
    const name = userInformation.name
    const userId = userInformation.userId
    const phoneNumber = userInformation.phoneNumber
    const email = userInformation.email
    ```

    ```
    const { name } = userInformation
    ```

    ```
    // 여러개도 가능 -> phonenumber, email
    const { phoneNumber, email } = userInformation
    ```

21. JSON -> 자바스크립트 객체로 바꾸는 메서드

    JSON.parse()

22. 자바스크립트 객체 ->JSON으로 바꾸는 메서드

    JSON.stringfy()

23. JS 아버지 이름?

    브랜던 아이크

24. ES6의 탄생은 몇년도?

    2015

25. querySelector, querySelectorAll() 안에 뭐가 들어가는지? (3개)  어떻게 쓰나요?

    class, id, tag 선택자

    '.class'  '#id' '태그'

26.  querySelecorAll은 무엇을 반환해?

    NodeList

27. 얘네 왜 사용하는지?

    클래스, id, 태그 선택이 가능하고 유연하게 사용 가능

28. 요소를 생성하는 method는 무엇?

    .createElement()

29. 요소를 추가하는 method 2개와 차이점

    .append() -> 여러 노드 추가 가능 문자열 추가 가능

    .appendChild() -> 하나만 추가 가능 문자열 추가 불가능

30. innerText와 innerHTML의 차이점

    innerText 텍스트 컨텐츠를 표현(사람이 읽을 수 있는 요소만 남김)

    innerHTML 요소 내에 포함된 HTML 마크업을 반환함

31. node를 삭제하는method는?

    .remove()

32. 속성을 갱신하거나 추가하는 method는?

    .setAttribute()

33. addEventListner()에는 뭐가 들어가고 무엇을 뜻하는지?

    첫번째 인자에는 type -> 행위 

    두번째 인자에는 listner -> 콜백함수 어떤 이벤트가 실행되는지 명세

34. 이벤트의 기본 동작을 중단하는 method는?, 어떨 때 사용해?

.preventDefault()

a태그의 기본ㄴ 동작은 클릭 시 링크 이동

form태그의 기본 동작은 form 데이터 전송