import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    # 0으로 초기화 된 트리 만들어주기
    tree = [0 for _ in range(n+1)]
    # m개의 줄 입력해
    for _ in range(m):
        # idx는 리프 노드 번호, value는 안에 들어가는 값
        idx, value = map(int, input().split())
        tree[idx] = value
    # 트리의 맨 뒤에서 노드 탐색!
    for i in range(n, 0, -1):
        if i // 2 > 0:
            tree[i//2] += tree[i] # 부모 노드에 자식 노드 더해주기

    print(f'#{tc} {tree[l]}')


