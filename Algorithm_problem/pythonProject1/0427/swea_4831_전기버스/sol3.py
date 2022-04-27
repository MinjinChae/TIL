# 문제 풀이의 포인트
# greedy(탐욕) -> 최대한 이동해서 최소한 충전하기
# K = 최대한 이동할 수 있는 정류장 수(최대 이동 거리)만큼 이동하지만,
# 거기에 충전기가 없으면 충전기가 있는 그나마 가까운 정류장으로 이동 -> 뒤로 빠꾸..위치를 -1 해줘야해
# 충전기가 있는 정류장을 찾으려고 뒤로 왔는데 다시 원위치로 온다면 영영 도착 못해

import sys

sys.stdin = open('input.txt')

def charging(K, N, charge_lst):
    bus = 0  # 버스의 현재 위치
    cnt = 0  # 충전횟수
    while True:
        # 버스가 최대한 이동할 수 있는 정류상 수 K만큼 이동해
        bus += K
        # 버스의 위치가 종점(N)이거나 더 멀리 갔다면 cnt 반환해
        if bus >= N:
            return cnt
        # 버스의 위치(지금 정류장)에 충전기가 없다면
        if charge_lst[bus] == 0:
            tmp = 0  # 뒤로 간 횟수
            # 충전기가 없으면 계속 반복해
            while charge_lst[bus] == 0:
                # 뒤로 간다~~(충전기가 있는 그나마 가까운 정류장으로 가자!)
                bus -= 1
                # 뒤로 가는 횟수는 +1
                tmp += 1
                # 뒤로 간 횟수가 K이면 원위치로 와버린거니까 도착못해..
                if tmp == K:
                    return 0
        # 충전기가 있으면 충전하자!
        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    # K: 한번 충전으로 최대한 이동할 수 있는 정류장 수 , N: 종점, M: 충전기가 있는 정류장 수
    K, N, M = map(int, input().split())
    # 충전기가 있는 정류장 번호
    charge = list(map(int, input().split()))
    # 충전기가 있는 정류장을 1로 표시해주기
    charge_lst = [0 for _ in range(N)]
    for i in charge:
        charge_lst[i] = 1
    # print(charge_lst)

    print(f'#{tc} {charging(K, N, charge_lst)}')

