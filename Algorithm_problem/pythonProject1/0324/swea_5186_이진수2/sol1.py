import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = float(input())  # 소수 입력받기
    cnt = 0  # 자리 수 count 초기화
    rlt = '' # 이진수 저장


    while n > 0: # n이 0보다 작을 때까지 반복
        tmp = n * 2
        rlt += str(tmp)[0]  # 정수부분만 저장
        n = tmp - int(tmp)  # 정수 제외, 소수점만 가져오기
        cnt += 1

        if cnt > 12:    # 소수점 아래 13자리 이상이면
            break  # 멈춰!

    if cnt > 12:  # 소수점 아래 13자리 이상이면 overflow 출력
        print(f'#{tc}', 'overflow')

    else:  # 그게 아니라면 이진수 출력
        print(f'#{tc} {rlt}')

