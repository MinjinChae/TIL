import sys

sys.stdin = open('input.txt')

# 후위 표기식 구하기
def postfix(str):
    for token in str:
        if token.isdigit():
            result.append(token)
        else:
            if len(stack) == 0:
                stack.append(token)
            else:
                if token == '(':
                    stack.append(token)
                elif token == ')':
                    tmp = stack.pop()
                    while tmp != '(':
                        tmp = stack.pop()
                elif token == '*':
                        while stack and stack[-1] == '*':
                            result.append(stack.pop())
                        stack.append(token)
                elif token == '+':
                        while stack and stack[-1] == '+':
                            result.append(stack.pop())
                        stack.append(token)
    for token in range(len(stack)):
        result.append(stack.pop())

    return result



for tc in range(1, T + 1):
    n = int(input())
    str = list(map(input().split()))
    stack = []
    result = []

    print(f'#{tc} ')



