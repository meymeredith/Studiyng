from tkinter import *

root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_oval(150,15,180,45,fill="orange")
c.create_rectangle(50,80,150,170,fill="powderblue")
c.create_polygon(30,80,170,80,100,40,fill="powderblue")

for i in range(10):
    c.create_polygon(2+i*10,200,2+i*10,170,1+i*10,160,fill="green")

root.mainloop()