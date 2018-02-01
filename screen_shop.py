from tkinter import *
from itemcreator import *

class Shopscreen(Frame):

    def __init__(self, master, back, level, player, x, y, floor, shoplist):
        super().__init__(master)
        self.back = back
        self.level = level
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.shoplist = shoplist
        self.create_widgets()
        self.grid()

    def create_widgets(self):

        Canvas(self, bg="#cc7130", width=600, height=300).grid(row=0, column=0, columnspan=5, rowspan=6)

        self.itemfile = load_item_file("items.txt")

        self.playersb = Scrollbar(self)
        self.playersb.grid(row=1, column=0, rowspan=3, sticky=NS)

        self.playeritems = Listbox(self, width=28, height=10, yscrollcommand=self.playersb.set, font="fixedsys")
        self.playeritems.grid(row=1, column=1, rowspan=3)
        self.playeritems.bind("<<ListboxSelect>>", self.show_player_desc)
        for x in self.player.inventory:
            self.playeritems.insert(END, x.name)

        self.playersb["command"] = self.playeritems.yview

        self.shopsb = Scrollbar(self)
        self.shopsb.grid(row=1, column=4, rowspan=3, sticky=NS)

        self.shopitems = Listbox(self, width=28, height=10, yscrollcommand=self.shopsb.set, font="fixedsys")
        self.shopitems.grid(row=1, column=3, rowspan=3)
        self.shopitems.bind("<<ListboxSelect>>", self.show_shop_desc)
        for x in self.shoplist:
            self.shopitems.insert(END, x.name)

        self.shopsb["command"] = self.shopitems.yview

        self.playerdescbox = Text(self, font="fixedsys", wrap=WORD, width=28, height=6, state=DISABLED)
        self.playerdescbox.grid(row=5, column=1)

        self.shopdescbox = Text(self, font="fixedsys", wrap=WORD, width=28, height=6, state=DISABLED)
        self.shopdescbox.grid(row=5, column=3)

        self.leave = Button(self, text=" GO BACK ", font="fixedsys", command=self.go_back, bg="#8B4513", activebackground="#633310")
        self.leave.grid(row=3, column=2)

        self.money_display = Label(self, text=" ¢ " + str(self.player.money) + " ", font="fixedsys", bg="#ce9d0a", width=11, relief=SUNKEN)
        self.money_display.grid(row=1, column=2)

        self.trade_button = Button(self, text="  TRADE  ", font="fixedsys", command=self.trade, bg="#8B4513", activebackground="#633310")
        self.trade_button.grid(row=2, column=2)

        self.playerprice = Label(self, text="Price: " + str(self.player.inventory[0].price), font="fixedsys", bg="#cc7130")
        self.playerprice.grid(row=4, column=1)
        self.shopprice = Label(self, text="Price: " + str(self.shoplist[0].price), font="fixedsys", bg="#cc7130")
        self.shopprice.grid(row=4, column=3)

    def show_player_desc(self, event):
        w = event.widget
        try:
            index = int(w.curselection()[0])
            self.playerdescbox["state"] = NORMAL
            self.playerdescbox.delete(0.0, END)
            self.playerdescbox.insert(0.0, self.player.inventory[index].desc)
            self.playerdescbox["state"] = DISABLED
            self.playerprice = Label(self, text="Price: " + str(self.player.inventory[index].price), font="fixedsys", bg="#cc7130")
            self.playerprice.grid(row=4, column=1)
        except:
            pass

    def show_shop_desc(self, event):
        w = event.widget
        try:
            index = int(w.curselection()[0])
            self.shopdescbox["state"] = NORMAL
            self.shopdescbox.delete(0.0, END)
            self.shopdescbox.insert(0.0, self.shoplist[index].desc)
            self.shopdescbox["state"] = DISABLED
            self.shopprice = Label(self, text="Price: " + str(self.shoplist[index].price), font="fixedsys", bg="#cc7130")
            self.shopprice.grid(row=4, column=3)
        except:
            pass

    def trade(self):
        try:
            index = int(self.shopitems.curselection()[0])
            action = "buy"
        except:
            index = int(self.playeritems.curselection()[0])
            action = "sell"
        if action == "buy":
            if self.shoplist[index].price <= self.player.money:
                self.player.money -= self.shoplist[index].price
                self.player.inventory.append(self.shoplist[index])
                self.playeritems.destroy()
                self.playeritems = Listbox(self, width=28, height=10, yscrollcommand=self.playersb.set, font="fixedsys")
                self.playeritems.grid(row=1, column=1, rowspan=3)
                self.playeritems.bind("<<ListboxSelect>>", self.show_player_desc)
                for x in self.player.inventory:
                    self.playeritems.insert(END, x.name)
                del(self.shoplist[index])
                self.shopitems.destroy()
                self.shopitems = Listbox(self, width=28, height=10, yscrollcommand=self.shopsb.set, font="fixedsys")
                self.shopitems.grid(row=1, column=3, rowspan=3)
                for x in self.shoplist:
                    self.shopitems.insert(END, x.name)
                self.shopitems.bind("<<ListboxSelect>>", self.show_shop_desc)
        elif action == "sell":
            if self.player.inventory[index].type == "weapon" and self.player.inventory[index].id == self.player.equipped.id:
                q = 0
                for a in self.player.inventory:
                    if a.id == self.player.equipped.id:
                        q += 1
                if q > 1:
                    self.player.money += self.player.inventory[index].price
                    self.shoplist.append(self.player.inventory[index])
                    self.shopitems.destroy()
                    self.shopitems = Listbox(self, width=28, height=10, yscrollcommand=self.shopsb.set, font="fixedsys")
                    self.shopitems.grid(row=1, column=3, rowspan=3)
                    for x in self.shoplist:
                        self.shopitems.insert(END, x.name)
                    self.shopitems.bind("<<ListboxSelect>>", self.show_shop_desc)
                    del (self.player.inventory[index])
                    self.playeritems.destroy()
                    self.playeritems = Listbox(self, width=28, height=10, yscrollcommand=self.playersb.set,
                                               font="fixedsys")
                    self.playeritems.grid(row=1, column=1, rowspan=3)
                    self.playeritems.bind("<<ListboxSelect>>", self.show_player_desc)
                    for x in self.player.inventory:
                        self.playeritems.insert(END, x.name)
            else:
                self.player.money += self.player.inventory[index].price
                self.shoplist.append(self.player.inventory[index])
                self.shopitems.destroy()
                self.shopitems = Listbox(self, width=28, height=10, yscrollcommand=self.shopsb.set, font="fixedsys")
                self.shopitems.grid(row=1, column=3, rowspan=3)
                for x in self.shoplist:
                    self.shopitems.insert(END, x.name)
                self.shopitems.bind("<<ListboxSelect>>", self.show_shop_desc)
                del(self.player.inventory[index])
                self.playeritems.destroy()
                self.playeritems = Listbox(self, width=28, height=10, yscrollcommand=self.playersb.set, font="fixedsys")
                self.playeritems.grid(row=1, column=1, rowspan=3)
                self.playeritems.bind("<<ListboxSelect>>", self.show_player_desc)
                for x in self.player.inventory:
                    self.playeritems.insert(END, x.name)
        self.money_display["text"] = " ¢ " + str(self.player.money) + " "


    def go_back(self):
        self.back(self.level, self.player, self.player_x, self.player_y, self.floor, self.shoplist)