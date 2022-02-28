import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    building = list(map(int, input().split()))  # 빌딩 리스트(높이들)
    cnt = 0 # 조망권 확보
    for i in range(2, T-2):  # 맨 왼쪽 2칸, 맨 오른쪽 2칸은 제외
        # 빌딩-조망권 확보 조건:좌,우 건물 2개보다 높아야 함
        if building[i] > building[i+1] and building[i] > building[i+2] and building[i] > building[i-1] and building[i] > building[i-2]:
            # 조망권 확보 세대-양쪽 4개 건물 중 가장 높은 건물을 빼줘야해
            list_building = [building[i + 1], building[i + 2], building[i - 1], building[i - 2]]
            max_height = list_building[0]  # 가장 높은 건물 변수 초기화
            for j in range(len(list_building)):
                if max_height < j:
                    max_height = j
                cnt += (building[i]-building[j])  # 조망권 확보 세대 수 = 건물-비교하는 건물 중 가장 높은 건물



print(f'#{tc} {cnt}')



