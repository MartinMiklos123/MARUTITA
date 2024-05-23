def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
    return lst


def foo(text_file):
    count = len(text_file)
    for i in range(5220, 5230):
        with open(str(i), "w") as file:
            for q in range(len(text_file)):
                if text_file[q] == str(i):
                    print(str(q + 1), file=file)
    return count




print(foo(read_file("2.txt")))