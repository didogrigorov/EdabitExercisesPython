import math


def number_split(num):
    num1 = num // 2
    num2 = math.ceil(num / 2)
    return [num1, num2]

print(number_split(-9))