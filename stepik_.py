# # print(__import__("numpy").prod([i for i in [int(input()) for __ in range(10)] if i]))

n = int(input())


def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


print(*[fibonacci_of(n) for n in range(1, n + 1)], sep=" ")
