import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
   n = int(input())
   num_lst = list(map(int, input().split()))

   cnt = 0
   for i in num_lst:
       if i < num_lst[n-1]:
          cnt += i
       # else:
       #     cnt += 0

       revenue = num_lst[n-1] * (n-1) - cnt


   print(revenue)
    # print(f'#{tc} ')

