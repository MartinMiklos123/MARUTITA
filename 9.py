import tkinter as tk
import random
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
correct_answer = 0
delenec = random.randint(11, 20)
delitel = random.randint(2, 9)


def gen_príklad():
    global correct_answer
    text = f"{delenec} : {delitel} = "
    canvas.create_text(250, 250, text=text, font="Arial 30 bold")
    correct_answer = delenec // delitel



def skontroluj():
    colors = ["black", "blue", "purple", "pink", "yellow", "orange", "bisque", "red", "green"]
    ans = Entry.get()
    zvysok = delenec - (correct_answer * delitel)
    if int(ans) == correct_answer:
        canvas.create_text(250, 400, text="Správne", font="Arial 20 bold")
    x = 50
    y = 300
    pointer = 0
    for i in range(correct_answer):
        for q in range(delitel):
            canvas.create_oval(x, y, x + 20, y + 20, fill=colors[pointer])
            x += 20
        pointer += 1

    x += 20
    print(zvysok)
    for i in range(zvysok):
        canvas.create_oval(x, y, x + 20, y + 20, fill=colors[pointer])
        x += 20


Entry = tk.Entry(window)
Entry.pack()
Button = tk.Button(window, text="Click", command=skontroluj)
Button.pack()

gen_príklad()

window.mainloop()