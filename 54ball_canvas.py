from tkinter import *

root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

ball = c.create_oval(0,40,40,0,fill='blue')
def animation():
    c.move(ball,1,1)
    if c.coords(ball)[2] < 200:
        root.after(10, animation)

animation()
root.mainloop()
