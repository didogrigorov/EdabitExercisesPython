def sum_odd_and_even(lst):
    odd = 0
    even = 0

    for i in range(len(lst)):
        if i % 2 == 0:
            odd += lst[i]
        else:
            even += lst[i]

    return [even, odd]



print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))