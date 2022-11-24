# # print(__import__("numpy").prod([i for i in [int(input()) for __ in range(10)] if i]))

n = int(input())

cache = {0: 0, 1: 1}


def fibonacci_of(arg):
    if arg in cache:
        return cache[arg]
    cache[arg] = fibonacci_of(arg - 1) + fibonacci_of(arg - 2)
    return cache[arg]


print(*[fibonacci_of(n) for n in range(1, n + 1)], sep=" ")
