import sys

sys.stdin = open('input.txt', encoding='utf-8')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    pattern = input()  # 찾을 문자열
    sentence = input()  # 전체 문장
    cnt = 0
    for i in range(len(sentence)):
        if sentence[i] == pattern[0]: # 첫글자가 똑같으면
            if sentence[i:i+len(pattern)] == pattern: # 슬라이싱으로 잘라서 비교
                cnt += 1

    print(f'#{tc} {cnt}')

