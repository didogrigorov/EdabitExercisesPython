import math


def line_length(dot1, dot2):
    solution = math.sqrt(math.pow(dot1[0] - dot2[0], 2) + math.pow(dot1[1] - dot2[1], 2))
    return round(solution, 2)

print(line_length([0, 0], [1, 1]))