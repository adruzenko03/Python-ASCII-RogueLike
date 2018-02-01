from tkinter import *
from enemycreator import *
from itemcreator import *
from copy import *
from time import *

class Battlescreen(Frame):

    def __init__(self, master, next, causedeath, level, player, x, y, floor, shopitems):
        super().__init__(master)
        self.resume = next
        self.die = causedeath
        self.level = level
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.shopitems = shopitems
        self.pmh = self.player.maxhealth
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        Canvas(self, bg="#cc7130", width=420, height=300).grid(row=0, column=0, rowspan=10, columnspan=5)

        enemylist = load_enemy_file("enemies.txt")
        self.enemy = deepcopy(get_random_enemy(enemylist, self.level))

        itemfile = load_item_file("items.txt")
        self.enemy.get_random_weapon()

        self.emh = self.enemy.maxhp

        self.playername = Label(self, text="Bup", font="fixedsys", bg="#cc7130")
        self.playername.grid(row=1, column=0, sticky=S)
        self.enemyname = Label(self, text=self.enemy.name, font="fixedsys", bg="#cc7130")
        self.enemyname.grid(row=5, column=0, sticky=S)

        self.playerweaponname = Label(self, text=self.player.equipped.name, font="fixedsys", bg="#cc7130")
        self.playerweaponname.grid(row=2, column=0)
        self.enemyweaponname = Label(self, text=self.enemy.weapon.name, font="fixedsys", bg="#cc7130")
        self.enemyweaponname.grid(row=6, column=0)

        self.playerhp = Label(self, text=str(self.player.hp) + "/" + str(self.pmh), font="fixedsys", bg="#cc7130")
        self.playerhp.grid(row=3, column=0, sticky=N)
        self.enemyhp = Label(self, text=str(self.enemy.maxhp) + "/" + str(self.emh), font="fixedsys", bg="#cc7130")
        self.enemyhp.grid(row=7, column=0, sticky=N)

        self.sb1 = Scrollbar(self)
        self.sb1.grid(row=1, column=1, rowspan=3, sticky=NS)
        self.items = Listbox(self, width=28, height=6, yscrollcommand=self.sb1.set, font="fixedsys")
        self.items.grid(row=1, column=2, columnspan=2, rowspan=3)
        for x in self.player.inventory:
            self.items.insert(END, x.name)
        self.sb1["command"] = self.items.yview

        self.combatlog = Text(self, width=28, height=6, font="fixedsys", wrap=WORD)
        self.combatlog.grid(row=5, column=2, columnspan=2, rowspan=3)

        self.useb = Button(self, text=" USE ", font="fixedsys", command=self.use)
        self.useb.grid(row=4, column=2)
        self.equipb = Button(self, text="EQUIP", font="fixedsys", command=self.equip)
        self.equipb.grid(row=4, column=3)

        Label(self, text="", font="fixedsys", width=18, bg="#cc7130").grid(row=0, column=0)
        Label(self, text="", font="fixedsys", width=18, bg="#cc7130").grid(row=0, column=1, columnspan=2)
        Label(self, text="", font="fixedsys", width=18, bg="#cc7130").grid(row=8, column=0)
        Label(self, text="", font="fixedsys", width=18, bg="#cc7130").grid(row=8, column=1, columnspan=2)

    def enemyattack(self):

        enemydamage = randint(self.enemy.weapon.output[0], self.enemy.weapon.output[1]) + self.enemy.strength
        self.player.hp -= enemydamage
        if self.player.hp <= 0:
            self.player.hp = 0
            self.useb.destroy()
            self.equipb.destroy()
            if self.enemy.maxhp == 0:
                self.go_backb.destroy()
                self.combatlog.insert(INSERT, "-The " + self.enemy.name + " attacks with their " + self.enemy.weapon.name + " and slays Bup!")
            self.dieb = Button(self, text="GAME OVER", font="fixedsys", command=self.player_die)
            self.dieb.grid(row=4, column=2, columnspan=2)
        else:
            if self.enemy.weapon.name == "Unarmed Attack":
                self.combatlog.insert(INSERT, "-The " + self.enemy.name + " attacks and deals " + str(enemydamage) + " damage!")
            else:
                self.combatlog.insert(INSERT, "-The " + self.enemy.name + " attacks with their " + self.enemy.weapon.name + " and deals " + str(enemydamage) + " damage!")
        self.playerhp["text"] = str(self.player.hp) + "/" + str(self.pmh)

    def use(self):

        try:

            index = int(self.items.curselection()[0])

            if self.player.inventory[index].type == "potion":
                self.player.hp += self.player.inventory[index].output
                if self.player.hp >= self.pmh:
                    regain = self.player.inventory[index].output - (self.player.hp - self.pmh)
                    self.player.hp = self.pmh
                else:
                    regain = self.player.inventory[index].output
                self.combatlog.delete(0.0, END)
                self.combatlog.insert(INSERT, "-Bup used the " + self.player.inventory[index].name + " and regained " + str(regain) + " health!\n")
                del (self.player.inventory[index])
                self.items.destroy()
                self.items = Listbox(self, width=28, height=6, yscrollcommand=self.sb1.set, font="fixedsys")
                self.items.grid(row=1, column=2, columnspan=2, rowspan=3)
                for x in self.player.inventory:
                    self.items.insert(END, x.name)
                self.sb1["command"] = self.items.yview
                self.playerhp["text"] = str(self.player.hp) + "/" + str(self.pmh)
                self.enemyattack()

            elif self.player.inventory[index].type == "weapon":
                playerdamage = randint(self.player.equipped.output[0], self.player.equipped.output[1])
                self.enemy.maxhp -= playerdamage
                if self.enemy.maxhp <= 0:
                    self.enemy.maxhp = 0
                    self.useb.destroy()
                    self.equipb.destroy()
                    if self.enemy.weapon.id != "attack":
                        self.player.inventory.append(self.enemy.weapon)
                    self.enemy.get_random_drops(self.player)
                    self.go_backb = Button(self, text="Go Back", font="fixedsys", command=self.go_back)
                    self.go_backb.grid(row=4, column=2, columnspan=2)
                    self.enemyhp["text"] = str(self.enemy.maxhp)+"/"+self.emh
                    self.combatlog.delete(0.0, END)
                    self.combatlog.insert(INSERT, "-Bup attacked with the " + self.player.equipped.name + " and slayed the " + self.enemy.name + "!\n")
                else:
                    self.enemyhp["text"] = str(self.enemy.maxhp)+"/"+self.emh
                    self.combatlog.delete(0.0, END)
                    self.combatlog.insert(INSERT, "-Bup attacked with the " + self.player.equipped.name + " and dealt " + str(playerdamage) + " damage!\n")
                    self.enemyattack()

        except:

            playerdamage = randint(self.player.equipped.output[0], self.player.equipped.output[1])
            self.enemy.maxhp -= playerdamage
            if self.enemy.maxhp <= 0:
                self.enemy.maxhp = 0
                self.useb.destroy()
                self.equipb.destroy()
                if self.enemy.weapon.id != "attack":
                    self.player.inventory.append(self.enemy.weapon)
                self.enemy.get_random_drops(self.player)
                self.go_backb = Button(self, text="Go Back", font="fixedsys", command=self.go_back)
                self.go_backb.grid(row=4, column=2, columnspan=2)
                self.enemyhp["text"] = str(self.enemy.maxhp) + "/" + str(self.emh)
                self.combatlog.delete(0.0, END)
                self.combatlog.insert(INSERT, "-Bup attacked with the " + self.player.equipped.name + " and slayed the " + self.enemy.name + "!\n")
            else:
                self.enemyhp["text"] = str(self.enemy.maxhp) + "/" + str(self.emh)
                self.combatlog.delete(0.0, END)
                self.combatlog.insert(INSERT, "-Bup attacked with the " + self.player.equipped.name + " and dealt " + str(playerdamage) + " damage!\n")
                self.enemyattack()

    def equip(self):

        try:

            index = int(self.items.curselection()[0])

            if self.player.inventory[index].type == "weapon":
                self.player.equipped = self.player.inventory[index]
                self.playerweaponname["text"] = self.player.equipped.name

        except:

            return None

    def go_back(self):
        self.resume(self.level, self.player, self.player_x, self.player_y, self.floor, self.shopitems, self.enemy)

    def player_die(self):
        self.die()