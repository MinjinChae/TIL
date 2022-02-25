n_lst = []
m_lst = []
for _ in range(3):
    n, m = map(int, input().split())
    n_lst.append(n)
    m_lst.append(m)

for i in range(3):
    if n_lst.count(n_lst[i]) == 1:
        x = n_lst[i]
    if m_lst.count(m_lst[i]) == 1:
        y = m_lst[i]

print(x, y)
