number = 101

def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if num != 1 and flag == True:
        print('Число', num, 'простое.')
    else:
        print('Число', num, 'составное.')


x = 17
y = int(input())
is_prime(x)
is_prime(y)
is_prime(number)