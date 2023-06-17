from tkinter import *
import tkinter as tk
win = tk.Tk()
win.geometry("150x220")

def label_update(text):
    label1['text'] = text

label1 = tk.Label(win, text=f'Код цвета: ',
            font=('Times New Roman', 12),
            height = 1, 
            width = 150
            )
label1.pack()

button_dict={}
colors=[f'#ff0000', f'#ff7d00', f'#ffff00', f'#00ff00', f'#007dff', f'#0000ff', f'#7d00ff']

for i in colors:
    def func(x=i):
        return label_update(x)
    button_dict[i] = tk.Button(win,background=i,height=1,width=10,command=func)
    button_dict[i].pack(side=TOP)

win.mainloop()
