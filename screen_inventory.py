from tkinter import *

class Inventoryscreen(Frame):

    def __init__(self, master, back, player, x, y, floor):
        super().__init__(master)
        self.back = back
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=275, height=200, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=3, rowspan=2, sticky=NW)

        self.sb = Scrollbar(self)
        self.sb.grid(row=0, column=0, sticky=NS)
        self.quantity = Listbox(self, width=2, height=10, yscrollcommand=self.sb.set, font="fixedsys")
        self.quantity.grid(row=0, column=1)
        self.items = Listbox(self, width=25, height=10, yscrollcommand=self.sb.set, font="fixedsys")
        self.items.grid(row=0, column=2)
        for x in range(0, 50):
            self.items.insert(END, x)
        for x in range(0, 50):
            self.quantity.insert(END, x)
        self.sb["command"] = self.scroll
        self.go_back = Button(self, text="BACK", font="fixedsys", command=self.goback)
        self.go_back.grid(row=1, column=0)

    def scroll(self, *args):
        self.quantity.yview(*args)
        self.items.yview(*args)

    def goback(self):
        self.back(self.player, self.player_x, self.player_y, self.floor)