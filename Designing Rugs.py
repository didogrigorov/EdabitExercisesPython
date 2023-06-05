def make_rug(rows, columns, symbol):
    element = ''
    result = []
    for i in range(rows):
        for j in range(columns):
            element += symbol
        result.append(element)
        element = ''

    return result



print(make_rug(2, 2, 'A'))