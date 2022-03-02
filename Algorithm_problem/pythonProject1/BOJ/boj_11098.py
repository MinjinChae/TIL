# 리스트로 풀기
T = int(input())
for tc in range(1, T+1):
    lst = []
    n = int(input())
    for _ in range(n):
        c, name = input().split()
        lst.append([int(c), name])
        lst = sorted(lst, key = lambda x : x[0], reverse = True)
    print(lst[0][1])

# 딕셔너리로 풀기
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    player = {}
    for _ in range(n):
        c, name = input().split()
        c = int(c)
        player[c] = name
    print(player.get(max(player.keys())))
