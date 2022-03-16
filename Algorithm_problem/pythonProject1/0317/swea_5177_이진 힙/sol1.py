import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input()) # 노드 개수
    # 0추가해서 노드 입력 받기(나중에 tree에 넣어줄 때 idx 맞춰서 넣어줘야지~!)
    lst = [0] + list(map(int, input().split()))
    # 0으로 초기화 된 tree 리스트 만들기
    tree = [0 for _ in range(n+1)]
    # 트리에 노드 넣어줘
    for i in range(1, len(lst)):
        tree[i] = lst[i]
        # 부모노드 < 자식노드
        # 부모 노드가 자식 노드보다 클 때까지 반복해서 바꿔줘
        while tree[i//2] > tree[i]:
            tree[i//2], tree[i] = tree[i], tree[i//2] # 자리 바꿔줘
            i = i // 2 # 바꿔줬으니까 그 위에 부모도 확인해보자!

    total = 0
    while True:
        if n == 1: # root까지 다왔다! 멈춰!
            break
        # 부모 노드로 올라가면서 더해줘
        n = n // 2
        total += tree[n]
    # print(tree)
    print(f'#{tc} {total}')

