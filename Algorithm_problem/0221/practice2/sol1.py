import sys

sys.stdin = open('input.txt')

def check(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

T = 2

for tc in range(1, T + 1):
    p = input()

    print(f'#{tc} {check(p)}')

