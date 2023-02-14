# Одинаковые цифры
#
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

print('YES' if len(set(input())) == 1 else 'NO')