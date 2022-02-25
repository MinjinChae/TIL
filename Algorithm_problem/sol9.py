from pprint import pprint
# 행 우선 순회
num_list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for r in range(len(num_list)):
    for c in range(len(num_list[0])):
        print(num_list[r][c], end=" ")
# 열 우선 순회

pprint(num_list, width=15)

for r in range(len(num_list)):
    for c in range(len(num_list[0])):
        # 5일 때, 상하좌우에 있는 원소 출력하기
        if num_list[r][c] == 5:
            print(num_list[r-1][c])  # 상
            print(num_list[r+1][c])  # 하
            print(num_list[r][c-1])  # 좌
            print(num_list[r][c+1])  # 우