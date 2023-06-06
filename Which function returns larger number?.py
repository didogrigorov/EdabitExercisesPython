def which_is_larger(f, g):
    result_f = f()  # Call function f and store the result
    result_g = g()  # Call function g and store the result

    if result_f > result_g:
        return "f"
    elif result_g > result_f:
        return "g"
    else:
        return "neither"

print(which_is_larger(lambda: 5, lambda:10))