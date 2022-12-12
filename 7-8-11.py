total = 0
for n in range(1, 31):
    for k in range(1, 31):
        for m in range(1, 31):
            if n * 28 + k * 30 + m * 31 == 365:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)
