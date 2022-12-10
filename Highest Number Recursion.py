def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = find_highest(lst[1:])
        if m > lst[0]:
            return m
        else:
            return lst[0]

print(find_highest([5,21,35,45,15]))