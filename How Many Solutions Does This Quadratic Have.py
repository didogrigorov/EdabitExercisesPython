import math
def solutions(a, b, c):
    d = b ** 2 - 4 * a * c

    if d < 0:
        return 0
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return 1
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return len([x1, x2])


print(solutions(1, 0, 1))