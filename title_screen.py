# this makes the title screen!!!
from tkinter import *

class TitleScreen(Frame):
    def __init__(self, master, maingame):
        super(TitleScreen, self).__init__(master)

        self.maingame = maingame
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=540, height=300, bd=0, highlightthickness=0).grid(row=0, column=0,
                                                                                           columnspan=6, rowspan=6)
        Label(self,
               text = "   Title!   ",
               font = "Fixedsys 60",
               bg = "#cc7130"
               ).grid(row = 0, column = 0)

        Button(self,
               text = "Play!",
               font = "Fixedsys 15",
               command = self.cont,
               bg = "#8B4513",
               activebackground="#633310"
               ).grid(row = 1, column = 0)

        Button(self,
               text = "Quit",
               font = "Fixedsys 15",
               command = quit,
               bg = "#8B4513",
               activebackground="#633310"
               ).grid(row = 3, column = 0)
    def cont(self):
        self.maingame()

root = Tk()
# root.title("Title")
# app = TitleScreen(root)
# root.mainloop()