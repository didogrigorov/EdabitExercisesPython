def sum_of_vowels(sentence):
    vowel_dict = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 0}
    sum = 0

    for item in sentence:
        item = item.lower()
        if item == ' ' or not item.isalpha():
            continue
        if item in vowel_dict:
            sum += vowel_dict.get(item)


    return sum
