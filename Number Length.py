def length_of_number(number):
    num_to_str = str(number)
    counter = 0
    for item in num_to_str:
        counter += 1

    return counter


print(length_of_number(102938132080))