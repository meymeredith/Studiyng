from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.title("Test")
        self.master.resizable(False, False)  

    def create_widgets(self):
        self.f1 = Frame()
        self.f1.pack()
        self.entry = Entry(self.f1, width=20)
        self.entry.pack(side=LEFT)
        Button(self.f1, text="open",command=self.file_load).pack(side=LEFT)
        Button(self.f1, text="save", command=self.file_save).pack(side=LEFT)
        self.f2 = Frame()
        self.f2.pack()
        self.text = Text(self.f2, width=50, height=20, wrap=NONE)
        self.text.pack(side=LEFT)

    def file_load(self):
        f = open(self.entry.get())
        self.text.delete(1.0, END)
        self.text.insert(1.0, f.read())

    def file_save(self):
        f = open(self.entry.get(), 'x')
        f.write(self.text.get(1.0, END))
        self.text.delete(1.0, END)

root = Tk()
app = Application(master=root)
root.mainloop()