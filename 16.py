def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
    return lst


def foo(text_file, text_file_fre):
    lst = [i.split() for i in text_file_fre]
    ini_dict = {}
    for i in text_file:
        for q in i:
            if q not in ini_dict:
                ini_dict[q] = 1
            else:
                ini_dict[q] += 1
    print(ini_dict)
    print(lst)
    for i in lst:
        if len(i) == 1:
            temp = int(i[0])
        else:
            temp = int(i[1])
        for q in ini_dict.keys():
            if ini_dict.get(q) == temp:
                ini_dict[q] = i[0] if len(i) != 1 else " "
    print(text_file)
    decrypted = []
    for i in text_file:
        temp_2 = list(i)
        for q in range(len(temp_2)):
            for z in ini_dict.keys():
                if z == temp_2[q]:
                    temp_2[q] = ini_dict.get(z)
        decrypted.append(temp_2)
    print(decrypted)





    print(ini_dict)



foo(read_file("16_sifra.txt"), read_file("16_frekv.txt"))

