def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
       return "Buzz"
    if num % 3 == 0:
        return "Fizz"


    return str(num)


print(fizz_buzz(4))