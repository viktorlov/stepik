z = int(input())


def cluster(arg: int) -> None:
    for i in range(1, 10):
        print(f'{arg} + {i} = {arg + i}')
    print()


for j in range(1, z + 1):
    cluster(j)
