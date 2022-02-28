import sys

sys.stdin = open('input.txt')

def itoa(n):
    if n > 0: # 양수일때
        lst = []  # 빈 리스트 만들기
        while n > 0 :
            lst.append(chr((n % 10) + 48))
            n = n // 10
        tmp = ''.join(lst)
        result = tmp[::-1] # 거꾸로 담아주기
        return result

    elif n < 0: # 음수일때
        n = -n
        lst = []  # 빈 리스트 만들기
        while n > 0:
            lst.append(chr((n % 10) + 48))
            n = n // 10
        tmp = ''.join(lst)
        result = tmp[::-1]
        return '-' + result # 음수니까 '-' 더해주기

    else: # 0일때
        return chr(48) #아스키코드 48 = 0

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    result = itoa(n)


    print(f'#{tc} {result}')



