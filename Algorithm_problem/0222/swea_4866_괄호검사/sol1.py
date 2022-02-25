import sys

sys.stdin = open('input.txt')

# 함수는 위에서 정의
def check(string):
    stack = []  # 빈 stack 만들기
    for i in string:  # for문 이용해서 입력 받은 값 돌려보기
        if i == '(' or i == '{':  # 열린 소괄호, 중괄호는 push로 stack에 삽입해
            stack.append(i)
        elif i == ')' or i == '}':  # 닫힌 소괄호, 중괄호가 왔을 때
            if len(stack) == 0:  # stack이 비어있으면 0 반환해(짝이 맞지 않으니까)
                return 0
                break
            elif i == ')' and stack[-1] != '(' or i == '}' and stack[-1] != '{':  #  소괄호와 중괄호의 조합 확인
                return 0  # i와 stack의 마지막 요소(top)가 다르면 0 반환해
                break
            else:
                stack.pop()  # 짝이 맞으면 pop해서 지워줘

    if len(stack) == 0:  # stack이 비어있으면 1 반환해
        return 1
    else:  # stack에 괄호가 남아 있으면 오류! 0반환해
        return 0

T = int(input())

for tc in range(1, T + 1):
    string = input()  # str 입력받기

    print(f'#{tc} {check(string)}')

