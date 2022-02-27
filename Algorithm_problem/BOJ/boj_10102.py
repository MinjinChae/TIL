v = int(input())
v_lst = list(input())

if v_lst.count('A') > v_lst.count('B'):
    print('A')
elif v_lst.count('A') < v_lst.count('B'):
    print('B')
else:
    print('Tie')