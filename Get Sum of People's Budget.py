def get_budgets(people):
    total_sum = 0
    for item in people:
        total_sum += item["budget"]

    return total_sum


print(get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]))

#62600