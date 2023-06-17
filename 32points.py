from tkinter import *
import tkinter as tk
win = tk.Tk()
win.geometry("500x500")

entry1=tk.Entry(win)
entry1.pack(side=LEFT)
tk.Button(win,text="Открыть").pack(side=RIGHT)
tk.Button(win,text="Сохранить").pack(side=RIGHT)
text = Text(width=500, height=100, bg="darkgreen",fg='white', wrap=WORD)
text.pack(side=BOTTOM)
win.mainloop()
