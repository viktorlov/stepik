# https://www.cyberforum.ru/python-tasks/thread2934310.html

a = [i ** 5 for i in range(1, 151)]
print(f'{a = }')
b = {}
print(f'{b = }')
c = {}
print(f'{c = }')
for i in range(150):
    for j in range(i, 150):
        c.setdefault(a[j] - a[i], []).append([j + 1, i + 1])
        for k in range(j, 150):
            b.setdefault(a[i] + a[j] + a[k], []).append([k + 1, j + 1, i + 1])

lst = sorted(set(b.keys()) & set(c.keys()))
res = sum(sum(c[lst[0]] + b[lst[0]], []))
print(res)
