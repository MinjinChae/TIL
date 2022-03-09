# 반복문으로 여러줄 입력 받을 때 int(input()) 형태로 입력 받으면 시간초과 발생
# sys.stdin.readline()은 한줄 단위로 입력받아서 시간초과 발생 x
import sys
n = int(sys.stdin.readline())
total = 0
for _ in range(n):
    plug = int(sys.stdin.readline())
    total += plug
print(total - (n - 1))