import sys

sys.stdin = open('input2.txt')

T = int(input())



for tc in range(1, T + 1):
    n = int(input())  # 카드 장수
    card_lst = list(map(int, input()))

    counter = [0] * 10  # 숫자 count할 list
    for i in card_lst:
        counter[i] += 1

    max_num = 0  # 카드 장수
    max_idx = 0  # 가장 많은 카드에 적힌 숫자

    for i in range(len(counter)):
        if counter[i] >= max_num:
            max_num = counter[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_num}')

