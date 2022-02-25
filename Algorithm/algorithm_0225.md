rear에서 데이터의 삽입이 일어나고

front에서 데이터의 삭제가 일어남



isEmpty

isFull

rear =4 == front = 4

rear == size-1 

원형큐에서는 front와 rear가 같아도 한번만 더 addqueue를 하면 선형queue의 문제를 해결할 수 있음

front == rear empty일수도 full일수도 있어서 구별을 못할수도 있는데 이럴때는 변수를 하나 만들어서 addqueue할때마다 count하면서 isfull인지 isempty인지 구별하면됨



front변수

상상 빈자리로 두는건 아님!



원형 큐의 구현 예

모듈러 연산? 

rear은 계속 1씩 더해주고 모듈러 이용

len(cQ) size

%n index를 내가 원하는 범위안에서 반복할 때 많이 사용함(알고리즘에서..!)





DEQ는 양쪽에서 원소를 삽입,삭제 할 수 있음

AddQ_Front 

DeleteQ-Front

AddQ_Rear

DeleteQ_rear



우선순위 큐

아무위치에서건 deleteQ가 가능함 단, 우선순위가 높은 애 부터!

그래서 큐안에 있는 모든애들이 우선순위를 가지고 있음

임의의 위치에서 꺼낼 수 있어! 우선순위에 따라서!

heap에 의해서 우선순위 큐를 구현함



리스트에서 pop(0)를 하면 삭제할 수 있지만 너무 비효율적임 -> import queue 사용함

 maxsize보다 크게 넣으면 망함

maxsize를 명시하지 않으면 됨 파이썬이 알아서 늘려주니까!



Node

data = ""

next = 주소값

다음에 가리킬 노드의 메모리 주소값을 가지고 있음

이런 노드가 연결되어 있는 구조를 단순 연결 리스트라고 함!



DFS stack 이용

BFS queue 이용

큐 앞에 있는거 하나 꺼내면서 a에 갈 수 있는 애들 넣어!

큐 앞에 있는거 하나 꺼내면서 b에 갈 수 있는 애들 넣어!

큐 앞에 있는거 하나 꺼내면서 d에 갈  수 있는 애들 넣어!

큐 앞에 있는거 하나 꺼내면서 e에 갈 수 있는 애들 넣어!

없어 -> 탐색 끝!

