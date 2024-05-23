import random


def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split() for i in lst]
    return lst

def foo(text_file):
    chance_rows = random.randint(0, 1)
    lst = text_file
    if chance_rows == 1:
        random.shuffle(lst)
    for i in range(len(text_file)):
        chance_words = random.randint(0, 1)
        if chance_words == 1:
            random.shuffle(lst[i])
        for q in range(len(lst[i])):
            chance_word = random.randint(0, 1)
            if chance_word == 1:
                lst[i][q] = lst[i][q][::-1]
    with open("14_vystup.txt", "w") as file:
        for i in lst:
            print(" ".join(i), file=file)




foo(read_file("14.txt"))
