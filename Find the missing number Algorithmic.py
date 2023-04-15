def missing_num(lst):
    all_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(0, len(all_num)):
        if all_num[i] in lst:
            continue
        else:
            return all_num[i]

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))