# n = int(input())  # 정수 한 개 입력 받기
# a, b = map(int, input().split())  # 정수 여러개 입력 받기
#
# # 정수 형태를 일차원 리스트로 입력 받기, 굉장히 많이 사용
# lst = list(map(int, input().split()))
# lst = [(map(int, input().split()))]  # 이건 안돼

# numbers = list(map(int, list(int(input()))) # 띄어쓰기가 없는 정수 입력받아서 리스트 만들기
#
# matrix = []
# for _ in range(2):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# matrix_2 = [x for x in range(10)]
# matrix = [list(map(int, input().split())) for _ in range(2)]
# print(matrix)

# # 얕은 복사와 깊은 복사
# lst = [1, 2, 3, 4]
# temp = []
# temp.append(lst)  # 얕은 복사가 일어나서 안 되는구나!
# temp.append(lst[:])  # 리스트에서 인덱싱 슬라이싱은 원본 바꾸지않고 새로운 리스트 반환
#
# lst.pop()
# lst.insert(0, 5)
#
# print(temp)

#  리스트 안에 있는것도 각각이 리스트이기 때문에 밖에 껍질만 복사됨 깊은 복사가 안된다

# 빈 matrix 만들기
# zeros = [[0] * 5] * 5  #얕은 복사가 일어난다
#
# zeros = []
# for _ in range(5):
#     row = [0,0,0,0,0]
#     zeros.append(row)

# 리스트 사이에 리스트 넣기
lst = [1, 2, 3, 4]
lst[2:2] = ('a','b','c')
print(lst)
lst[1:3] = ['a','b','c','d','e']
