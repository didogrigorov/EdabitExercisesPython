def letter_counter(matrix, searched_letter):
  all_letters = {}

  for row in matrix:
    for letter in row:
      if letter not in all_letters:
        all_letters[letter] = 0

      all_letters[letter] += 1

  if searched_letter in all_letters:
    return all_letters[searched_letter]




print(letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "H"))