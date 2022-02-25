import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str = list(input().split())
    stack = []
    for token in str:
        if token.isdecimal():  # 숫자인 경우
            stack.append(int(token))
        else:  # 연산자인 경우
            if token == '.':  # 마침표가 왔을 때
                if len(stack) == 1:
                    ans = stack.pop()
                    print(f'#{tc} {ans}')
                else:
                    print(f'#{tc}', end=' ')
                    print('error')
                    break

            elif len(stack) > 1:  # stack 안에 숫자가 2개 이상 있어야지 연산이 가능
                p2 = stack.pop()
                p1 = stack.pop()
                if token == '+':
                    rlt = p1 + p2
                    stack.append(rlt)
                elif token == '-':
                    rlt = p1 - p2
                    stack.append(rlt)
                elif token == '*':
                    rlt = p1 * p2
                    stack.append(rlt)
                elif token == '/':
                    rlt = p1 // p2  # 나눗셈은 항상 나누어 떨어지니까! //
                    stack.append(rlt)

            else:  # 1개 이하면 error
                print(f'#{tc}', end=' ')
                print('error')
                break





    # print(f'#{tc} {ans}')

