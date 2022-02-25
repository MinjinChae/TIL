import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    word = input()
    stack = []  # 빈 stack 만들기

    for i in word:  # 문자열 돌리면서 체크
        if i not in stack:  # stack에 없으면 push해서 추가해
            stack.append(i)
        else:  # 이미 stack에 있을 때
            if stack[-1] == i:   # 연속하는 경우에는 마지막 값 pop해서 지워줘
                stack.pop()
            else:  # 연속하지 않으면 추가해줘
                stack.append(i)

    result = len(stack)

    print(f'#{tc} {result}')

