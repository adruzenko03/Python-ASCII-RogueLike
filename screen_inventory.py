from tkinter import *

class Inventoryscreen(Frame):

    def __init__(self, master, back, player, x, y, floor):
        super().__init__(master)
        self.back = back
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=275, height=280, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=3, rowspan=4, sticky=NW)

        self.sb = Scrollbar(self)
        self.sb.grid(row=0, column=0, sticky=NS)

        self.items = Listbox(self, width=25, height=10, yscrollcommand=self.sb.set, font="fixedsys")
        self.items.grid(row=0, column=1)
        self.items.bind("<<ListboxSelect>>", self.showdesc)
        for x in self.player.inventory:
            self.items.insert(END, x.name)

        self.sb["command"] = self.items.yview

        self.descbox = Text(self, font="fixedsys", wrap=WORD, width=25, height=6, state=DISABLED)
        self.descbox.grid(row=1, column=1, rowspan=3)

        self.go_back = Button(self, text="GO BACK", font="fixedsys", command=self.goback)
        self.go_back.grid(row=1, column=0)
        self.go_back = Button(self, text="USE", font="fixedsys")
        self.go_back.grid(row=2, column=0)
        self.go_back = Button(self, text="EQUIP", font="fixedsys")
        self.go_back.grid(row=3, column=0)

    def showdesc(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.descbox["state"] = NORMAL
        self.descbox.delete(0.0, END)
        self.descbox.insert(0.0, self.player.inventory[index].desc)
        self.descbox["state"] = DISABLED

    def goback(self):
        self.back(self.player, self.player_x, self.player_y, self.floor)