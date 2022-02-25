import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    arr = [[0]*10 for _ in range(10)]  # 10X10 만들기
    for _ in range(n):
        row1, col1, row2, col2, color = map(int, input().split())
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
              if color == 1:
                  # 빈칸이라면 빨간색을 칠하고
                  if arr[i][j] == 0:
                      arr [i][j] = 1
                 # 파란색이면 보라색으로 색칠해
                  elif arr[i][j] == 2:
                       arr[i][j] == 3
                       cnt += 1  # 보라색 부분은 count해줘
              else: # color == 2이면
                  # 빈칸이라면 파란색을 색칠하고
                  if arr[i][j] == 0:
                      arr[i][j] = 2
                  # 빨간색이면 보라색으로 색칠해
                  elif arr[i][j] == 1:
                       arr[i][j] == 3
                       cnt += 1  # 보라색 부분은 count해줘


    print(f'#{tc} {cnt}')

