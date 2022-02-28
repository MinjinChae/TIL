# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
#
# score_lst = []
# score_lst.append(A)
# score_lst.append(B)
# score_lst.append(C)
# score_lst.append(D)
# score_lst.append(E)
#
# sum_score = 0
# for i in score_lst:
#     if i < 40:
#         i = 40
#         sum_score += i
#     else:
#         sum_score += i
#
# average = sum_score // 5
#
# print(average)

# 위에서는 하나하나 input 받아서 리스트에 넣어줬는데
# 이렇게 짧게 쓸 수도 있어!
total = 0
for _ in range(5): # input 받는것을 5번 반복함
    score = int(input()) # score라는 변수, int형태로 input받음
    if score < 40:
        total += 40
    else:
        total += score
avg = total // 5
print(avg)