import sys

sys.stdin = open('input.txt')

def preorder(v):
    # cnt를 함수 밖에서 호출하면 에러가 나니까 전역변수 선언해주기!
    global cnt
    if v:
        cnt += 1  # 순회하면서 cnt 증가시키기
        preorder(tree[v][0])
        preorder(tree[v][1])

T = int(input())

for tc in range(1, T + 1):
    e, v = map(int, input().split())  # e: 간선의 개수 v: 시작 노드
    lst = list(map(int, input().split()))
    # 0으로 초기화된 tree 리스트 만들기
    # 왼쪽자식, 오른쪽자식 두명이니까 * 2
    # 노드의 갯수 = 간선 + 1 -> range니까 +2 해주기
    tree = [[0] * 2 for _ in range(e + 2)]
    # 부모를 인덱스로 자식 저장하기
    for i in range(0, len(lst)-1, 2):
        # 부모, 자식 노드 가져오기
        p = lst[i]
        c = lst[i+1]
        # p의 왼쪽 자식이 비어있으면 넣어줘
        if tree[p][0] == 0:
            tree[p][0] = c
        # 그렇지 않으면 오른쪽에 넣어줘
        else:
            tree[p][1] = c

    # cnt 초기화
    cnt = 0
    preorder(v)
    print(f'#{tc} {cnt}')

