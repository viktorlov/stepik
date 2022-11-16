[print(i * "*") for i in range(int(input()), 0, -1)]

# from math import tan, pi
#
# n = int(input())
# a = float(input())
#
# s = (n * a * a) / (4 * tan(pi / n))
#
# print(s)
#
# import math
#
# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# discr = b ** 2 - 4 * a * c
#
# if discr > 0:
#     x1 = (-b - math.sqrt(discr)) / (2 * a)
#     x2 = (-b + math.sqrt(discr)) / (2 * a)
#     print(x1)
#     print(x2)
# elif discr == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     print("Нет корней")

# # Формат входных данных
# # На вход программе подается четыре вещественных числа,
# # каждое на отдельной строке – x_{1}, y_{1}, x_{2}, y_{2}
#
# from math import sqrt
#
# x1, y1, x2, y2 = [float(input()) for _ in range(4)]
#
# print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# import re
#
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
#
# def check(arg):
#     if (re.fullmatch(regex, arg)):
#         print("YES")
#     else:
#         print("NO")
#
#
# if __name__ == '__main__':
#     email = input()
#     check(email)
#
# def email_checker(arg):
#
#


# str_ = input()
# FX = lambda x: True if ('суббота' in x) + ('воскресенье' in x) else False
#
# print("YES" if FX(str_) else "NO")
#
# nums = [len(input()) for _ in range(3)]
# nums.sort()
# MN = lambda x, y, z: True if x - y == y - z else False
# print("YES" if MN(*nums, ) else "NO")
#
# towns = [input() for _ in range(3)]
# towns.sort(key=len)
# print(towns[0], towns[-1], sep="\n")
#
# *num_, = list(int(input()) for _ in range(3))
# for _ in range(3):
#     print(sorted(num_, reverse=True)[_])
#
# print('\n'.join(sorted([input() for _ in range(3)], reverse=True)))
#
# nums = [int(input()) for _ in range(3)]
# nums.sort(reverse=True)
# print(*nums, sep='\n')

# nums = list(map(int, input()))
# print("Число интересное" if sorted(nums)[-1] - sorted(nums)[0] == sorted(nums)[1] else "Число неинтересное")

# s = [int(i) for i in input()]
# print(('Число неинтересное', 'Число интересное')[(max(s) - min(s)) == sorted(s)[1]])

# nums = [float(input()) for _ in range(5)]
# print(sum([abs(x) for x in nums]))
