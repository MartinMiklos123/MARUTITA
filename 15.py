def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split() for i in lst]
    return lst


def foo(text_file):
    num = len(text_file)
    ini_dict = {}
    for i in text_file:
        temp = i[1]
        if temp not in ini_dict:
            ini_dict[temp] = [1, i[0]]
        else:
            ini_dict[temp][0] += 1
            ini_dict[temp].append(i[0])

    for i in ini_dict.keys():
        if len(ini_dict.get(i)[1:]) < 20:
            print(f"menej ako dvacat is objednalo písmeno {i}, kod ziakov: {ini_dict.get(i)[1:]}")
    print(f"pocet jedal: {num}")


foo(read_file("15.txt"))



