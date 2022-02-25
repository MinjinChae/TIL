# # 1. 5 x 5 matrix 초기화
# matrix = []
# for i in range(5):
#     row = [ 0 for _ in range(5)]
#
# # 2. 각각의 요소의 차구하기
# # 2.1 각 요소에 접근하기(델타를 이용)
# # 2.2 각 요소의 차구하기
# # 3. 절대값 처리하기
# # 4. 합 누적하기
# num_list = [list(map(int, input().split()))]
# for r in range(len(num_list)):
#     for c in range(len(num_list[0])):
#         # 상,하,좌,우 원소 출력
#         row_d = [-1, 1, 0, 0]
#         col_d =[0, 0, -1, 1]
#         for d in range(4):
#             each_row = r + row_d[d]
#             each_col = c + col_d[d]

arr = []
for i in range(5):
    row = [j + i * 5 for j in range(1, 6)]
    arr.append(row)
    print(row)