user_string = "Hello World"

def convert_to_hex(txt):
  solution=""
  for chr in txt:
    solution = solution + format(ord(chr), "x") + " "
  return solution[:-1]

print(convert_to_hex(user_string))