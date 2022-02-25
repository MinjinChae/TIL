T = int(input())
for tc in range(1, T+1):
    mars_lst = list(map(str,input().split()))
    ans = 0
    for i in range(len(mars_lst)):
        if i == 0:
            ans += float(mars_lst[i])
        else:
            if mars_lst[i] == '@':
                ans *= 3
            elif mars_lst[i] == '%':
                ans += 5
            elif mars_lst[i] == '#':
                ans -= 7

    print('%0.2f' %ans)



