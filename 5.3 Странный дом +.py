from tkinter import *

root = Tk()

c = Canvas(root, width=200, height=200, bg='powderblue')
c.pack()

c.create_rectangle(10,50,120,200,fill='green')
c.create_polygon(121,121,121,200,190,200,190,160,160,160,160,120,fill='red')
c.create_oval(170,10,190,30,fill='orange')
c.create_polygon(10,50,120,50,65,10,fill="blue")
c.create_line(120,50,120,30)
c.create_line(120,30,110,10)
c.create_line(120,30,130,10)
c.create_arc(37, 10, 10, 37, start=215,extent=100,style='arc')
c.create_rectangle(30,84,100,156,fill="powderblue")
c.create_line(30,84,100,156)
c.create_line(100,84,30,156)

for i in range(0,10):
    c.create_line(160+i*5,0,200-i*5,40,fill='orange')

root.mainloop()