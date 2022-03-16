import sys

sys.stdin = open('input.txt')
# inorder 순회 -> 1.왼쪽 자식 2. 부모 3. 오른쪽 자식
def inorder(root):
    if root: # 루트가 있으면
        inorder(int(Tree[root][1]))  # 왼쪽 자식
        print(Tree[root][0], end='') # 문자
        inorder(int(Tree[root][2]))  # 오른쪽 자식


T = 10 # 테스트 케이스는 10개
for tc in range(1, T + 1):
    n = int(input())
    # 문자, 왼쪽자식, 오른쪽자식 3개 넣어줘야 하니까
    Tree = [[0] * 3 for _ in range(n+1)]
    for i in range(n):
        lst = list(input().split())
        p = int(lst[0])
        Tree[p][0:len(lst)-1] = lst[1:len(lst)]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()

