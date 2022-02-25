arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
bucket = [0] * 10
for i in range(len(arr)):
    bucket[arr[i]] += 1

for i in range(len(bucket)):
    for j in range(bucket[i]):
        print(i, end =' ')


