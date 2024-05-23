import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()


def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split(" ") for i in lst]
    return lst


def foo(text_file):
    count = 0
    ini_dict = {}
    for i in text_file:
        if i[0][:2] not in ini_dict and i[1] == "nie":
            ini_dict[i[0][:2]] = 1
        elif i[0][:2] in ini_dict and i[1] == "nie":
            ini_dict[i[0][:2]] += 1
    return ini_dict


def draw_histogram(values):
    print(values)
    x = 0
    y = 450
    for i in range(23):
        if i < 10:
            text = "0"+str(i)
        else:
            text = str(i)
        canvas.create_line(x, y, x+20, y)
        canvas.create_text(x + 6, y+20, text=text)
        if text in values.keys():
            val = values.get(text)
            canvas.create_rectangle(x, y, x + 20, y - (val * 20), fill="red")
        x += 30

draw_histogram(foo(read_file("6.txt")))
window.mainloop()