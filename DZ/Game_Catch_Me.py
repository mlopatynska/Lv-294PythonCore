#Connecting libreries
from tkinter import *
from random import randrange as rnd, choice
#Creating window
root = Tk()
root.geometry('800x600')
#Background
canv = Canvas(root, bg='lightblue')
canv.pack(fill=BOTH, expand=1)
#Colors of balls
colors = ['red', 'orange', 'yellow', 'green', 'blue']
#Creating ball
def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_text(20, 20, text=str(points), font='Arial 20')
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)
#Click calculating by Pyfagor theory
def click(event):
    global points
    if (event.y - y) ** 2 + (event.x - x) ** 2 <= r ** 2:
        points += 1
#Points reset to 0
points = 0
new_ball()
canv.bind('<Button-1>', click)
mainloop()