n = int(input())
m_lst = []
for _ in range(n):
    m = int(input())
    m_lst.append(m)

if m_lst.count(1) > m_lst.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')