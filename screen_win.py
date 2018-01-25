from tkinter import *
from time import *
from threading import *

class Winscreen(Frame):
    def __init__(self, master, restart, level, player):
        super().__init__(master)
        self.grid()
        self.level = level
        self.player = player
        self.create_widgets()
        self.restart = restart

    def create_widgets(self):
        self.c = Canvas(self, bg="black", width=500, height=300, bd=0, highlightthickness=0)
        self.c.grid(row=0, column=0)
        self.l = Label(self,
              text = "Level "+ str(self.level),
              bg = "black",
              fg = "Black",
              font = ("Fixedsys 40"))
        self.l.grid(row=0, column=0)
        """ Button(self,
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
               ).grid(row=2, column=3, sticky=W) """
        t = Thread(target=self.change_color)
        t.start()

    def change_color(self):
        sleep(0.1)
        self.c["bg"] = "#261001"
        self.l["bg"] = "#261001"
        sleep(0.15)
        self.c["bg"] = "#441e04"
        self.l["bg"] = "#441e04"
        sleep(0.2)
        self.c["bg"] = "#68310a"
        self.l["bg"] = "#68310a"
        sleep(0.25)
        self.c["bg"] = "#8c4513"
        self.l["bg"] = "#8c4513"
        sleep(0.3)
        self.c["bg"] = "#a0531c"
        self.l["bg"] = "#a0531c"
        sleep(0.35)
        self.c["bg"] = "#cc7130"
        self.l["bg"] = "#cc7130"
        sleep(1)
        self.c["bg"] = "#a0531c"
        self.l["bg"] = "#a0531c"
        sleep(0.35)
        self.c["bg"] = "#8c4513"
        self.l["bg"] = "#8c4513"
        sleep(0.3)
        self.c["bg"] = "#68310a"
        self.l["bg"] = "#68310a"
        sleep(0.25)
        self.c["bg"] = "#441e04"
        self.l["bg"] = "#441e04"
        sleep(0.2)
        self.c["bg"] = "#261001"
        self.l["bg"] = "#261001"
        sleep(0.15)
        self.c["bg"] = "black"
        self.l["bg"] = "black"
        sleep(0.1)
        self.restartF()

    def restartF(self):
        if self.level == 1:
            self.restart()
        else:
            self.restart(self.level, self.player)

#root = Tk()
#root.title("Win Screen")
#app = Winscreen(root)
#root.mainloop()