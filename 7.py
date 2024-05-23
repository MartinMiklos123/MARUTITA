import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=500)
canvas.pack()

def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()

    return lst


r = read_file("7.txt")

def foo(text_file):
    x = 0
    y = 450
    for i in text_file[1:]:
        canvas.create_line(x, y, x+45, y, fill=text_file[0])
        if i == text_file[1] or i == text_file[-1]:
            canvas.create_rectangle(x, y + 10, x + 20, y - 10, fill="red")
            text = i
        else:
            if "*" in i:
                canvas.create_oval(x, y + 10, x + 10, y - 10)
                text = i.replace("*", "")
            else:
                canvas.create_oval(x, y + 10, x + 10, y - 10, fill="red")
                text = i
        canvas.create_text((x + 15, y - 50), text=text, font='Arial 10', angle=45)
        x += 45


foo(r)

window.mainloop()