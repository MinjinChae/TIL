T = int(input())
for _ in range(T):
    ox_lst = list(input())
    score = 0
    cnt = 1
    for i in ox_lst:
        if i == 'o':
            score += cnt
            cnt += 1
        else:
            cnt = 1

    print(score)