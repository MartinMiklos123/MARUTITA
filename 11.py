import random

def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
    return lst


def guess_word(word):
    num_of_tries = 10
    word_2 = ["*" for i in range(len(word))]
    found_letter = False
    while num_of_tries > 0:
        print(word_2)
        n = input("Zadaj písmeno: ")
        for i in range(len(word)):
            if n == word[i]:
                word_2[i] = n
                found_letter = True
        if not found_letter:
            num_of_tries -= 1
            print("neuhadol si pismeno")
        found_letter = False
        if "".join(word_2) == word:
            print(f"Uhadol si slovo {word}")



guess_word(random.choice(read_file("11.txt")))