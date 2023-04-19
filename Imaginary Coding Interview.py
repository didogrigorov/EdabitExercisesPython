# Imaginary Coding Interview
def interview(lst, tot):
    is_ok = False
    all_true = []

    if len(lst) != 8 or tot > 120:
        return "disqualified"

    #very easy
    very_easy = lst[0:2]
    very_easy_result = [True if x <= 5 else False for x in very_easy]

    if all(very_easy_result):
        is_ok = True
        all_true.append(True)
    else:
        all_true.append(False)

    #easy
    easy = lst[2:4]
    easy_result = [True if x <= 10 else False for x in easy]

    if all(easy_result):
        is_ok = True
        all_true.append(True)
    else:
        all_true.append(False)

    #medium
    medium = lst[4:6]
    medium_result = [True if x <= 15 else False for x in medium]

    if all(medium_result):
        is_ok = True
        all_true.append(True)
    else:
        all_true.append(False)

    #hard
    hard = lst[6:8]
    hard_result = [True if x <= 20 else False for x in hard]

    if all(hard_result):
        is_ok = True
        all_true.append(True)
    else:
        all_true.append(False)


    return "qualified" if all(all_true) else "disqualified"