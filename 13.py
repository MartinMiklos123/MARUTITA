import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()


def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
        lst = [i.split() for i in lst]
    return lst


def draw_buildings(text_file):
    x = 0
    y = 400
    for i in text_file:
        if i[1] == "0":
            fill = "green"
        else:
            fill = "grey"
        canvas.create_rectangle(x, y, x+int(i[0]), y - int(i[1]), fill=fill)
        x += int(i[0])


draw_buildings(read_file("13.txt"))


def line():
    x = 0
    y = 400
    text_file = read_file("13.txt")
    height = Entry.get()
    height = int(height)
    for i in range(len(text_file) - 1):
        x_1 = int(text_file[i][0])
        y_1 = int(text_file[i][1])
        y_2 = int(text_file[i+1][1])
        if y_1 >= (y_2 + height):
            if y_2 != 0 and y_1 != 0:
                canvas.create_line(x + x_1, y - y_2, x + x_1, y-y_1, fill="red")
        if y_1 <= (y_2 - height):
            if y_2 != 0 and y_1 != 0:
                canvas.create_line(x + x_1, y-y_2, x+x_1, y-y_1, fill="red")
        x += x_1

Button = tk.Button(window, command=line)
Button.pack()
Entry = tk.Entry(window)
Entry.pack()


window.mainloop()