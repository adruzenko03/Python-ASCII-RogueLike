from tkinter import *

class Inventoryscreen(Frame):

    def __init__(self, master, back, level, player, x, y, floor, shopitems):
        super().__init__(master)
        self.back = back
        self.level = level
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.shopitems = shopitems
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=310, height=360, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=3, rowspan=7, sticky=NW)

        self.name = Label(self, text="Bup", font="fixedsys", bg="#cc7130").grid(row=0, column=0, rowspan=3)
        self.health_display = Label(self, text=" ❤ " + str(self.player.hp) + "/" + str(self.player.maxhealth) + " ", font="fixedsys", bg="#960c0c", width=11, relief=SUNKEN)
        self.health_display.grid(row=0, column=1)
        self.money_display = Label(self, text=" ¢ " + str(self.player.money) + " ", font="fixedsys", bg="#ce9d0a", width=11, relief=SUNKEN)
        self.money_display.grid(row=1, column=1)
        self.equip_display = Label(self, text=" Item: " + str(self.player.equipped.name) + " ", font="fixedsys", bg="#cc7130")
        self.equip_display.grid(row=2, column=1)

        self.sb = Scrollbar(self)
        self.sb.grid(row=3, column=0, sticky=NS)

        self.items = Listbox(self, width=28, height=10, yscrollcommand=self.sb.set, font="fixedsys")
        self.items.grid(row=3, column=1)
        self.items.bind("<<ListboxSelect>>", self.show_desc)
        for x in self.player.inventory:
            self.items.insert(END, x.name)

        self.sb["command"] = self.items.yview

        self.descbox = Text(self, font="fixedsys", wrap=WORD, width=28, height=6, state=DISABLED)
        self.descbox.grid(row=4, column=1, rowspan=3)

        self.goback = Button(self, text="GO BACK", font="fixedsys", bg="#8B4513", activebackground="#633310", command=self.go_back)
        self.goback.grid(row=4, column=0)
        self.use = Button(self, text="  USE  ", font="fixedsys", bg="#8B4513", activebackground="#633310", command=self.use_item)
        self.use.grid(row=5, column=0)
        self.equip = Button(self, text=" EQUIP ", font="fixedsys", bg="#8B4513", activebackground="#633310", command=self.equip_item)
        self.equip.grid(row=6, column=0)

    def show_desc(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.descbox["state"] = NORMAL
        self.descbox.delete(0.0, END)
        self.descbox.insert(0.0, self.player.inventory[index].desc)
        self.descbox["state"] = DISABLED

    def use_item(self):
        index = int(self.items.curselection()[0])
        if self.player.inventory[index].type == "potion":
            self.player.hp += self.player.inventory[index].output
            if self.player.hp >= self.player.maxhealth:
                self.player.hp = self.player.maxhealth
            del(self.player.inventory[index])
            self.items.destroy()
            self.items = Listbox(self, width=28, height=10, yscrollcommand=self.sb.set, font="fixedsys")
            self.items.grid(row=3, column=1)
            self.items.bind("<<ListboxSelect>>", self.show_desc)
            for x in self.player.inventory:
                self.items.insert(END, x.name)
            self.health_display["text"] = " ❤ " + str(self.player.hp) + "/" + str(self.player.maxhealth) + " "

    def equip_item(self):
        index = int(self.items.curselection()[0])
        if self.player.inventory[index].type == "weapon":
            self.player.equipped = self.player.inventory[index]
            self.equip_display["text"] = " Item: " + str(self.player.equipped.name) + " "

    def go_back(self):
        self.back(self.level, self.player, self.player_x, self.player_y, self.floor, self.shopitems)