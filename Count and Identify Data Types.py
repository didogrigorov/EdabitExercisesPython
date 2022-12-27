from collections import OrderedDict
def count_datatypes(*args):
    datatypes = OrderedDict({'int':0, 'str':0, 'bool':0, 'list':0, 'tuple':0, 'dict':0})

    for item in args:
        if type(item).__name__ in datatypes:
            datatypes[type(item).__name__] += 1

    result = []

    for value in datatypes.values():
        result.append(value)

    return result

print(count_datatypes(1, 45, "Hi", False))