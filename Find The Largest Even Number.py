def largest_even(lst):
    res = -1

    for x in lst:
        if not x % 2 and x > res:
            res = x
    return res


print(largest_even([1,3,5,7]))