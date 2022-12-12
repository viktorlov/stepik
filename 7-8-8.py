n = int(input())
center = n // 2 + 1
count = 0
for i in range(1, n + 1):
    if i > center:
        count -= 1
    else:
        count += 1

    for _ in range(count):
        print('*', end='')
    print()
