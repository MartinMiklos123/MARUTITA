import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

def read_file(file):
    with open(file, "r") as file:
        lst = file.read().splitlines()
    return lst[0], lst[1].split()


def draw(text_file):
    canvas.create_text(200, 100, text=text_file[0], font="Arial 10 bold")
    texts = ["1)Ano", "2)Nie", "3)Neviem"]
    maximum = text_file[1].index(str(max([int(i) for i in text_file[1]])))
    x = 100
    y = 150
    x_2 = 150
    for i in range(3):
        if i == maximum:
            fill = "green"
        else:
            fill = "red"
        canvas.create_text(x, y, text=texts[i], font="Arial 10 bold")
        canvas.create_rectangle(x_2, y, x_2 + (int(text_file[1][i]) * 5), y + 20, fill=fill)
        y += 50

draw(read_file("10.txt"))


def adjust_values(event):
    n = read_file("10.txt")[1]
    if event.keysym == "1":
        n[0] = str(int(n[0]) + 1)
    elif event.keysym == "2":
        n[1] = str(int(n[1]) + 1)
    elif event.keysym == "3":
        n[2] = str(int(n[2]) + 1)
    rewrite_file(n)

def rewrite_file(n):
    with open("10.txt", "w") as file:
        print("Suhlasite so zavedenim zalohovania PET flias?", file=file)
        print(n[0]+" "+n[1]+" "+n[2], file=file)
    draw(read_file("10.txt"))


canvas.bind("<Key>", adjust_values)
canvas.focus_set()

window.mainloop()
