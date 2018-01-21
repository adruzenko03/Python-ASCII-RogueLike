from tkinter import *
from enemycreator import *
from copy import *

class Battlescreen(Frame):

    def __init__(self, master, next, player, x, y, floor):
        super().__init__(master)
        self.resume = next
        self.player = player
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        enemylist = load_enemy_file("enemies.txt")
        self.enemy = deepcopy(get_random_enemy(enemylist))

        self.go_back = Button(self, text="Go Back", font="fixedsys", command=self.go_back)
        self.go_back.grid(row=3, column=0, columnspan=2)
        self.playername = Label(self, text="Bup", font="fixedsys")
        self.playername.grid(row=1, column=0)
        self.enemyname = Label(self, text=self.enemy.name, font="fixedsys")
        self.enemyname.grid(row=1, column=1)
        self.playerhp = Label(self, text=self.player.hp, font="fixedsys")
        self.playerhp.grid(row=2, column=0)
        self.enemyhp = Label(self, text=self.enemy.maxhp, font="fixedsys")
        self.enemyhp.grid(row=2, column=1)

        Label(self, text="", font="fixedsys", width=30).grid(row=0, column=0, columnspan=2)

    def go_back(self):
        self.resume(self.player, self.player_x, self.player_y, self.floor)