def sum_of_evens(lst):
    evens_sum = 0

    for row in lst:
        for element in row:
            if element % 2 == 0:
                evens_sum += element

    return evens_sum


print(sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]))