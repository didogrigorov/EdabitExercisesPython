def shift_to_right(x, y):
    divisor = 2 ** y
    return x // divisor


print(shift_to_right(80, 3))