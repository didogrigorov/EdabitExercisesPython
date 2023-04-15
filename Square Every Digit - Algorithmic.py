def square_digits(digit):
    new_digit = str(digit)
    final_result = ''

    for item in new_digit:
        result = int(item) ** 2
        final_result += str(result)


    return int(final_result)


print(square_digits(3212))