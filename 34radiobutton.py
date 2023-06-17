from tkinter import *

root = Tk()

text = StringVar()
rb1=Radiobutton(text="Вася",value="+33333333",indicatoron=0,variable=text)
rb2=Radiobutton(text="Петя",value="+44444444",indicatoron=0,variable=text)
rb3=Radiobutton(text="Маша",value="+55555555",indicatoron=0,variable=text)
l = Label(textvariable=text)

rb1.pack(side=TOP)
rb2.pack(side=TOP)
rb3.pack(side=TOP)
l.pack(side=RIGHT)

root.mainloop()
