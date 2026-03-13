# coded by Zenet

def change_order(string_):
    vowels = ["a", "e", "i", "o", "u"]

    vowels_in_str = [x for x in string_ if x in vowels]

    string_copy = [s for s in string_]

    if len(vowels_in_str) == 0:
        return string_
    if len(vowels_in_str) == 1:
        return string_

    vowel_number = 0

    for v in range(len(string_)):
        if string_copy[v] in vowels_in_str:
            index = generate_index(vowels_in_str, (vowel_number + 1))
            string_copy[v] = vowels_in_str[index]
            vowel_number += 1

    return string_copy

def generate_index(vowels, vowel_number):
    n = len(vowels)
    k = vowel_number

    if vowel_number == (n + 1) - n:
        return -1
    else:
        return ((n - (k - 1)) - 1)

n = change_order("pinkfairyarmadillo")
print(n)
