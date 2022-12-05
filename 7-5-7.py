class Number:
    """
    # Дано натуральное число. Напишите программу, которая вычисляет:
    #
    # сумму его цифр;
    # количество цифр в нем;
    # произведение его цифр;
    # среднее арифметическое его цифр;
    # его первую цифру;
    # сумму его первой и последней цифры.
    # Формат входных данных
    # На вход программе подается одно натуральное число.
    #
    # Формат выходных данных
    # Программа должна вывести значения указанных величин в указанном порядке.
    """

    def __init__(self, number: int):
        self.number = number

    def __repr__(self):
        return 'Number'

    def to_int_list(self):
        return [int(_) for _ in str(self.number)]

    def digit_sum(self):
        return sum(self.to_int_list())

    def digit_count(self):
        return len(self.to_int_list())

    def digit_prod(self):
        from math import prod
        return prod(self.to_int_list())

    def digit_mean(self):
        from statistics import mean
        return mean(self.to_int_list())

    def first_digit(self):
        return self.to_int_list()[0]

    def first_last_digit_sum(self):
        return self.to_int_list()[0] + self.to_int_list()[-1]


z = Number(int(input()))

print(z.digit_sum())
print(z.digit_count())
print(z.digit_prod())
print(z.digit_mean())
print(z.first_digit())
print(z.first_last_digit_sum())
