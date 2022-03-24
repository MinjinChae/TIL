import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, number = input().split()
    # 알파벳 -> 10진수로 변환
    hex_to_binary = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    rlt = ''  # rlt 초기화

    for i in number[::-1]:
        if i in hex_to_binary:  # 딕셔너리 안에 있으면 숫자로 변환해줘!
            i = hex_to_binary[i]

        # 지금 str이니까 int로 바꿔주고
        i = int(i)
        # 4자리니까 4번 반복해주기
        for _ in range(4):
            # 2로 나눈 나머지를 넣어주고 다시 2로 나눠줘
            rlt = str(i % 2) + rlt
            i//= 2

    print(f'#{tc} {rlt}')

