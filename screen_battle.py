from tkinter import *
from enemycreator import *
from copy import *

class Battlescreen(Frame):

    def __init__(self, master, next, causedeath, player, x, y, floor):
        super().__init__(master)
        self.resume = next
        self.die = causedeath
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        enemylist = load_enemy_file("enemies.txt")
        self.enemy = deepcopy(get_random_enemy(enemylist))

        self.playername = Label(self, text="Bup", font="fixedsys")
        self.playername.grid(row=1, column=0)
        self.enemyname = Label(self, text=self.enemy.name, font="fixedsys")
        self.enemyname.grid(row=1, column=1)
        self.playerhp = Label(self, text=self.player.hp, font="fixedsys")
        self.playerhp.grid(row=2, column=0)
        self.enemyhp = Label(self, text=self.enemy.maxhp, font="fixedsys")
        self.enemyhp.grid(row=2, column=1)
        self.attackb = Button(self, text="ATTACK", font="fixedsys", command=self.attack)
        self.attackb.grid(row=4, column=0, columnspan=2)

        Label(self, text="", font="fixedsys", width=18).grid(row=0, column=0)
        Label(self, text="", font="fixedsys", width=18).grid(row=0, column=1)

    def attack(self):
        playerdamage = randint(1, 20)
        self.enemy.maxhp -= playerdamage
        if self.enemy.maxhp < 0:
            self.enemy.maxhp = 0
            self.attackb.destroy()
            self.go_backb = Button(self, text="Go Back", font="fixedsys", command=self.go_back)
            self.go_backb.grid(row=4, column=0, columnspan=2)
        enemydamage = randint(1, 10) + self.enemy.strength
        self.player.hp -= enemydamage
        if self.player.hp < 0:
            self.player.hp = 0
            self.attackb.destroy()
            if self.enemy.maxhp == 0:
                self.go_backb.destroy()
            self.dieb = Button(self, text="GAME OVER", font="fixedsys", command=self.player_die)
            self.dieb.grid(row=4, column=0, columnspan=2)
        self.enemyhp["text"] = self.enemy.maxhp
        self.playerhp["text"] = self.player.hp

    def go_back(self):
        self.resume(self.player, self.player_x, self.player_y, self.floor, self.enemy)

    def player_die(self):
        self.die()