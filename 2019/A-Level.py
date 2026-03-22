def get_both_words():
    first_word = input("First word: ").upper()
    second_word = input("Second word: ").upper()
    return first_word, second_word

def main():
    first_word, second_word = get_both_words()

    first_word_list = [w for w in first_word]
    second_word_list = [w for w in second_word]

    count = 0

    for x in range(len(first_word)):
        if first_word[x] in second_word_list:
            count += 1
            first_word_list.remove(first_word[x])
            second_word_list.remove(first_word[x])

    if count == len(first_word):
        return f"The word: {first_word} can be formed from the word: {second_word}"
    return f"The word: {first_word} cannot be formed from the word: {second_word}"

message = main()
print(message)
