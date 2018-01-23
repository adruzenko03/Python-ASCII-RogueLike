from tkinter import *
class Winscreen(Frame):
    def __init__(self, master, restart):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.restart = restart
    def create_widgets(self):
        x = 1
        Canvas(self, bg="#cc7130", width=500, height=300, bd=0, highlightthickness=0).grid(row=0, column=0,columnspan=6, rowspan=6)
        Label(self,
              text = "You beat level"+ str(x),
              bg = "#cc7130",
              fg = "Black",
              font = ("Fixedsys 50"),
             ). grid(row=0, column=1, columnspan = 3)
        Button(self,
               text = "Continue",
               font = ("Fixedsys 16"),
               bg ="#8B4513",
               command= self.restartF
               ).grid(row=2,column=1,sticky=W)
        Button(self,
               text="Exit",
               font=("Fixedsys 16"),
               bg="#8B4513",
               command = exit
               ).grid(row=2, column=3, sticky=W)
        x += 1
    def restartF(self):
        self.restart()

#root = Tk()
#root.title("Win Screen")
#app = Winscreen(root)
#root.mainloop()