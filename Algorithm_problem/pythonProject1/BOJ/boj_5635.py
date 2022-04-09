# 단순 정렬 문제

# 빈 리스트 생성
lst = []
n = int(input())
for _ in range(n):
  # 이름, 일, 월, 연도
    name, dd, mm, yyyy = input().split()
  # 하나의 튜플 안에 넣어주고 리스트에 추가해주기 -> 이름, 일, 월, 연도가 하나의 원소야!
    lst.append((name, int(dd), int(mm), int(yyyy)))
  # 원소의 연도, 월, 일 순으로 정렬해주기(오름차순)
    lst.sort(key= lambda x : (x[3], x[2], x[1]))
# print(lst)
# 가장 나이 적은 사람의 이름 출력
print(lst[-1][0])
# 가장 나이 많은 사람의 이름 출력
print(lst[0][0])



