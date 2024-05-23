def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split(" ") for i in lst]
    for i in range(len(lst)):
        temp = float(lst[i][-2].replace(",", ".")) # IMPORTANT STEP
        lst[i][-2] = temp


    return lst

def foo(text_file):
    temps = [i[-2] for i in text_file]
    sor = sorted(temps)[-1]
    stanica = ""
    for i in text_file:
        if sor in i:
            stanica += i[0] + " "
    ar_p = round(sum(temps) / len(temps), 2)
    return sor, stanica, ar_p


print(foo(read_file("4.txt")))
