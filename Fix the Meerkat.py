def fix_the_meerkat(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp

    return arr


print(fix_the_meerkat(['tail', 'body', 'head']))