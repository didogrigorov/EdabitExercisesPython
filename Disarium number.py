def is_disarium(n):
    num = [int(x) for x in str(n)]
    result = 0
    for item in num:
        index_item = num.index(item) + 1
        calculation = item ** index_item
        result += calculation

    if result == n:
        return True
    else:
        return False

# is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32
# is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
# is_disarium(544) ➞ False
# is_disarium(518) ➞ True
# is_disarium(466) ➞ False
# is_disarium(8) ➞ True
