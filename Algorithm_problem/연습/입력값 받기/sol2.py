#  정수 한 개 입력 받기
# n = int(input())
# print(n)

#  정수 여러개 입력 받기
# a, b = map(int, input().split())
# print(a, b)

# 정수 형태를 일차원 리스트로 입력 받기
# num_lst = list(map(int, input().split()))

# 이렇게 하는거 아니야!
# num_lst = [map(int, input().split())]
# print(num_lst)

# 띄어쓰기가 없는 정수 입력받아서 리스트 만들기 ?????????????
# numbers = list(map(int, list(input())))
# print(numbers)

# 2차원 리스트 만들기
# matrix = []
# for _ in range(2):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# print(matrix)

# matrix_2 = [x for x in range(10)]
# print(matrix_2)
# matrix_3 = [list(map(int, input().split())) for _ in range(2)]
# print(matrix_3)

# # 얕은 복사와 깊은 복사
# lst = [1, 2, 3, 4]
# temp = []
# # temp.append(lst)
# # print(temp)
# temp.append(lst[:])
# # print(temp)
#
# lst.pop()
# print(temp)

# arr = [0] * 10
# print(arr)
# import pprint
# N = int(input())
# arr  = [list(map(int, input().split())) for _ in range(N)]
# pprint.pprint(arr)

import pprint
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
pprint.pprint(arr)