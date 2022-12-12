z = int(input())

def line(arg: int) -> None:
    print(f'{arg}' * arg)


for i in range(1, z + 1):
    line(i)
