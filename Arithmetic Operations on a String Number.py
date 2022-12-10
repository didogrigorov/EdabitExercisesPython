def arithmetic_operation(n):
    result = 0
    n = n.split()
    nums = []
    for item in n:
        if item.isdigit():
            nums.append(int(item))
    if "//" in n:
        if nums[1] == 0:
            result = -1
        else:
            result = nums[0] // nums[1]
    elif "*" in n:
        result = nums[0] * nums[1]
    elif "-" in n:
        result = nums[0] - nums[1]
    elif "+" in n:
        result = nums[0] + nums[1]

    return result

# print(arithmetic_operation("12 + 12"))
# arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
# arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0
# arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
# arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1