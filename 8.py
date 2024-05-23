n = input("Zadaj číslo a sústavu: ")
n = n.split(" ")
sustava = n[1]
cislo = n[0]
lst = [["A", 10], ["B", 11], ["C", 12], ["D", 13], ["E", 14], ["F", 15]]
count = 0
count_2 = 0
for i in cislo[::-1]:
    try:
        count += int(i) * (int(sustava)**count_2)
    except:
        for q in lst:
            if i in q:
                count += q[1] * (int(sustava)**count_2)
                break
    count_2 += 1


print(f"{cislo}({sustava}) = {count}")








