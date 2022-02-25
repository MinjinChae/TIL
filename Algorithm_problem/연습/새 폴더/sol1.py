import pprint

a = [[4, 5, 6, 7, 8], [4, 7, 8, 9, 2], [3, 1, 6, 8, 9], [3, 1, 8, 9, 0], [3, 1, 9, 6, 7]]
pprint.pprint(a)
print('-------------------------------')

# 대각선 왼쪽에서 아래로
for i in range(len(a)):
    # for j in range(5):
    #     if i == j:
            print(a[i][i], end = '')
print('-------------------------------')

# 대각선 오른쪽에서  아래로
for i in range(len(a)):
    print(a[i][len(a)-i-1], end = '')

print('-------------------------------')

# 열로 뽑기(세로)






pprint.pprint(a)

