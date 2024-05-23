def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
    return lst


def foo(text_file):
    count = len(text_file)
    max_length = max([len(i) for i in text_file])
    temp = ""
    vals = ["H", "P", "L", "R", "D"]
    with open("3.c.txt", "w") as file:
        for i in text_file:
            for q in vals:
                if i.count(q) != 0:
                    temp += q + " " + str(i.count(q)) + " "
            print(temp, file=file)
            temp = ""




foo(read_file("3.txt"))
