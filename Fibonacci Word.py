# def fibo_word(n):  # Fibonacci word
#     arr = ["b", "a"]
#     while len(arr) < n:
#         arr.append(arr[-1] + arr[-2])
#
#     return ", ".join(arr) if n > 1 else "invalid"
#

# Recursive version
def generate_word(num, a='b', b='a', res='b, a'):
    if num < 2:
        return 'invalid'

    a, b = b, a + b # a = 'a', b = 'ba'

    res += ', {}'.format(b)
    num -= 1

    return res if num == 2 else generate_word(num, a, b, res)


print(generate_word(6))
