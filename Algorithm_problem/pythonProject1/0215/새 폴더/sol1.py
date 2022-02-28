import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
   n = int(input())
   num_lst = list(map(int,input().split()))

    #bubble sort로 내림차순 정렬
   for i in range(len(num_lst)-1):
       for j in range(0, len(num_lst)-1-i):
           if num_lst[j] < num_lst[j+1]:
               num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]
# print(num_lst)

   lst = [] # 빈 리스트 만들기
   for i in range(5): # 10개까지 출력이니까 5번
       lst.append(num_lst[i]) # 큰 수
       lst.append(num_lst[-1-i]) # 작은 수
   # print(lst)


   print(f'#{tc}', end = ' ')
   for i in range(10):
      print(f'{lst[i]}', end=' ')
   print()

   # print(lst[:10])




