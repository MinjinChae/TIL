import sys

sys.stdin = open('input.txt')

# 입력 받기
T = int(input())
for tc in range(1, T + 1):
     n = int(input())
     want_led = [0] + list(map(int, input().split()))
     led = [0 for _ in range(n+1)]

     cnt = 0 # 버튼 누르는 횟수
     for i in range(n+1):
          if i == 0:
               continue
          elif led[i] == want_led[i]:
               continue
          else:
               for j in range(i, n+1):
                    if j % i == 0:
                         if led[j] == 0:
                              led[j] = 1
                         else:
                              led[j] = 0
               cnt += 1

          if led == want_led:
               print(f'#{tc} {cnt}')
               break


