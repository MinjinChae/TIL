word = input()
if word == word[::-1]:
    print(1)
else:
    print(0)

# # reversed 함수 사용
# word = list(input())
# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)
#
# # 이거 아니야
# word = list(input())
# if word.reverse() == word:
#     print(1)
# else:
#     print(0)
