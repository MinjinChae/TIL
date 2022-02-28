bowl = input()
sum_bowl = 10
for i in range(1, len(bowl)):
    if bowl[i-1] == bowl[i]:
        sum_bowl += 5
    else:
        sum_bowl += 10

print(sum_bowl)