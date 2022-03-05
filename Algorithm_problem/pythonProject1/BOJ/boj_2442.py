# 처음에한거 -> 실패! '출력 형식이 잘못되었습니다.' (아마도 뒤에 공백 때문에)
n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1) + ' ' * (n - i))

# 수정한거
n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1))