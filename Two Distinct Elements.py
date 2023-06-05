def return_unique(lst):
    result = []
    for item in lst:
        if lst.count(item) > 1:
            continue
        result.append(item)

    return result

lst = [1, 9, 8, 8, 7, 6, 1, 6]
print(return_unique(lst))