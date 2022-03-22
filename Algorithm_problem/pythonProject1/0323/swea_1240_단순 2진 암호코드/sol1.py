import sys

sys.stdin = open('input.txt')

# 0 ~ 9까지의 수와 대응하는 이진 코드
P = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    my_code = []
    # print(arr)
    # 한 행의 끝에서 부터 1이 있는지 찾기!
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if arr[i][j] == 1:  # 너 1이야?
                for k in range(j, j - 56, -7):  # 그럼 뒤에서부터 7개씩 끊어서 넣어!
                    # '000100'이런식으로 넣어줘야 하니까 str로 변환하고 숫자 붙여주기
                    my_code.insert(0, ''.join(map(str, arr[i][k - 6: k + 1])))
                break  # 넣어줬으니까 멈춰!
            else:  # 그게 아니라면
                continue  # 그냥 넘어가~

        if my_code:  # 코드가 들어가 있으면(어차피 똑같은 암호들이 반복하니까)
            break  # 멈춰!
    # print(my_code)

    # 딕셔너리 값으로 치환해주기
    for i in range(len(my_code)):
        my_code[i] = P[my_code[i]]  # 딕셔너리는 key로 접근해

    # 검증코드 계산해주기
    confirm_code = 0
    for i in range(1, len(my_code) + 1):
        if i % 2:  # 2로 나눴을 때 나머지가 있다면 -> 홀수
            confirm_code += my_code[i - 1] * 3
        else:
            confirm_code += my_code[i - 1]

    # 정상코드/비정상코드 확인하기
    if confirm_code % 10: # 10의 배수가 아니라면
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum(my_code)}')

