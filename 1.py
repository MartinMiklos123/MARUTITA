def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split() for i in lst]
    return lst


def foo(text_file):
    countries = set([i[1] for i in text_file])
    count = [[i, [i[1] for i in text_file].count(i)] for i in countries]
    max_jump = [[i[0], max(i[2:])] for i in text_file]
    max_jump_2 = sorted(max_jump, key=lambda x: x[1])[-1][1]
    winners = [i[0] for i in max_jump if max_jump_2 in i]
    return countries, count, winners


r = foo(read_file("1.txt"))
print(r)
