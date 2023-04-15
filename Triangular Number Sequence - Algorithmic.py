def triangle(num):
    dots = 0
    for i in range(num + 1):
        dots += i

    return dots


print(triangle(215))