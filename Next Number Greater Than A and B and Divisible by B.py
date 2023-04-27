import sys


def divisible_by_b(a, b):
    max = sys.maxsize
    for i in range(a, max):
        if i % b == 0:
            return i


print(divisible_by_b(17, 8))