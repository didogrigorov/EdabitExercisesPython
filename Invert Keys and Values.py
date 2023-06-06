def invert(dct):
    new_dict = {}
    for key, value in dct.items():
        if value not in new_dict:
            new_dict[value] = key

    return new_dict


print(invert({ "a": 1, "b": 2, "c": 3 }))