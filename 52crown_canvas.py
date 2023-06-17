from tkinter import *

root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_polygon(80,200,120,200,100,80,fill="red")
c.create_oval(90,70,110,90,fill="red")
c.create_polygon(50,200,80,200,85,170,20,110,fill="blue")
c.create_oval(10,98,30,118,fill="blue")
c.create_polygon(180,110,150,200,120,200,115,170,fill="green")
c.create_oval(170,98,190,118,fill="green")
c.create_polygon(85,180,98,178,100,170,102,178,110,180,102,182,100,195,98,182,90,180,fill="yellow")

root.mainloop()
