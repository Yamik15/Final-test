from tkinter import *
from random import *

def Generation():
    x = randint(1, 700)
    y = randint(1, 700)
    f = randint(1, 700)
    e = randint(1, 700)
    g = randint(1, 700)
    h = randint(1, 700)
    canvas.delete('all')
    a = randint(1, 3)
    if a == 1:
        canvas.create_rectangle(x, y, f, e)
    elif a == 2:
        canvas.create_oval(x, y, f, e)
    else:
        canvas.create_polygon(x, y, f, e, g, h)

root = Tk()

root.title('Application')
root.geometry('800x800')
root.resizable(False, False)

canvas = Canvas(
    root,
    width=750,
    height=750,
    bg='cyan'
)
canvas.pack()

button = Button(
    root,
    text='Random Shape Generation (Click)',
    command=Generation
)
button.pack()

root.mainloop()







