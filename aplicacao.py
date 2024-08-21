import tkinter
from tkinter import *


class Janela:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='primeiro widget')
        self.msg['font'] = ("verdana", "20", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "sair"
        self.sair["font"] = ("Calibri", "20")
        self.sair["width"] = 15
        self.sair["command"] = self.widget1.quit
        self.sair.pack()
root = Tk()
Janela(root)
root.mainloop()
