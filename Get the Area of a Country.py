import math


def area_of_country(name, area):
    country = area // 2
    world = 148940000 // 2
    area = (country / world) * 100
    return f"{name} is {round(area, 2)}% of the total world's landmass"


print(area_of_country("Russia", 17098242))