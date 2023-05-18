def face_interval(num):
    if isinstance(num, str):
        return ":/"
    else:
        num.sort()

    interval = num[-1] - num[0]

    if interval in num:
        return ":)"
    else:
        return ":("

print(face_interval([5, 2, 8, 3, 11]))