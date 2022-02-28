n = int(input())  # 정수 한 개 입력 받기
a, b = map(int, input().split())  # 정수 여러개 입력 받기

lst_1 = list(map(int, input().split()))  # 정수 형태를 일차원 리스트로 입력 받기
lst_2 = [map(int, input().split())]  # 이건 안돼

numbers = list(map(int, list(input())))  # 띄어쓰기가 없는 정수 입력받아서 리스트 만들기
print(numbers)

matrix = []
for _ in range(2):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)

matrix_2 = [x for x in range(10)]
matrix = [list(map(int, input().split())) for _ in range(2)] # 이렇게도 할 수 있다?
print(matrix)

얕은 복사와 깊은 복사

lst = [1, 2, 3, 4]
temp = []
# temp.append(lst)  # 얕은 복사가 일어나서 안되는구나 !
temp.append(lst[:])

lst.pop()
lst.insert(0, 5)

print(temp)

copy.deepcopy() 사용해라!
lst = [[1, 2], [3, 4]]
temp = []
temp.append(lst[:])
lst[0][0] = 5
print(temp)


빈 matrix 만들기
zeros = [[0] * 5] * 5  # 얕은 복사가 일어난다
zeros[0][0] = 99
print(zeros)

zeros = []
for _ in range(5):
    row = [0] * 5
    zeros.append(row)

for row in zeros:
    print(row)

zero_matrix = [[0] * 5 for _ in range(5)]  # 이렇게 쓸 수 도 있어요.


리스트 사이에 리스트 넣기

lst = [1, 2, 3, 4]
# lst[2:2] = ["a", "b", "c"]
# lst[1:3] = ["a", "b"]
lst[1:3] = ["a", "b", "c", "d", "e"]
print(lst)

