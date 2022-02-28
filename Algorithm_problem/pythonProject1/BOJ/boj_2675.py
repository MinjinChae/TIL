T = int(input())
for tc in range(1, T+1):
    n, word = map(str, input().split())
    new_word = ''
    for i in word:
        new_word += i * int(n)
    print(new_word)
# for i in range(len(word)):
#     new_word += word[i] * int(n)
# print(new_word)