from math import floor


def sum_fractions(lst):
    sum = 0

    for i in range(len(lst)):
        calculation = lst[i][0] / lst[i][1]
        sum += calculation

    return round(sum)


print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))