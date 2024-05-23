import random

def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split() for i in lst]
    return lst


def get_input():
    string = input("Zadaj 6 čísiel: ")
    return string.split(" ")


def los():
    n = [str(random.randint(1, 49)) for i in range(6)]
    return n


ticket = los()
print(ticket)
my_ticket = get_input()
print(my_ticket)

def compare_my(my_tic, tic):
    correct_nums = []
    for i in my_tic:
        for q in tic:
            if i == q:
                correct_nums.append(i)
                break
    return correct_nums, len(correct_nums)


print(f"uhadol som: {compare_my(my_ticket, ticket)}")


def compare_others(text_file, tic):
    lst = [["1", 0], ["2", 0], ["3", 0], ["4", 0], ["5", 0], ["6", 0]]
    for i in text_file:
        n = compare_my(i, tic)[1]
        for q in range(len(lst)):
            if str(n) in lst[q]:
                lst[q][1] += 1
                break
    print(lst)


compare_others(read_file("5.txt"), ticket)




















