import sys

sys.stdin = open('input.txt')

def powerset(idx, N)  # 함수
    if  idx == N:
        sum_num = 0
        for i in range(N):

            sum_num += a[i]

        if sum == 10:


    else:
        bit[idx] = 0
        powerset(idx+1, N)
        bit[idx] = 1
        powerset(idx+1, N)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(a)
bit = [0] * N
powerset(idx=0,N=N)

    # print(f'#{tc} ')

