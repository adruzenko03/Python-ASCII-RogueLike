from tkinter import *
from dungeoncrawlergame import *
from itemcreator import *
from title_screen import *
from screen_win import *
from screen_battle import *
from screen_inventory import *
from screen_death import *

class Put_Everything_Together(object):
    def __init__(self):
        self.root = Tk()

    def pick_char(self):
        self.root.title("START GAME")
        self.load_title = TitleScreen(self.root, self.create_main_game)

    def create_main_game(self):
        self.ongame = True
        self.load_title.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_game, self.start_battle, self.open_inventory)
        self.itemlist = load_item_file("items.txt")
        for i in self.itemlist:
            if i.id == "hatchet":
                self.game.player.inventory.append(i)
                self.game.player.equipped = self.game.player.inventory[0]
            if i.id == "potion_min_heal":
                self.game.player.inventory.append(i)
        self.game.assemble_rooms()

    def resume_main_game(self, player, x, y, floor, enemy):
        self.ongame = True
        self.battle_scene.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_game, self.start_battle, self.open_inventory, player, x, y, floor)
        self.game.add_moneydrop(enemy)
        self.game.kill_nearby_enemies()
        self.game.print_screen()

    def open_inventory(self, player, x, y, floor):
        self.ongame = False
        self.game.destroy()
        self.root.title("INVENTORY")
        self.inv = Inventoryscreen(self.root, self.close_inventory, player, x, y, floor)

    def close_inventory(self, player, x, y, floor):
        self.ongame = True
        self.inv.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_game, self.start_battle, self.open_inventory, player, x, y, floor)
        self.game.print_screen()

    def end_game(self):
        self.ongame = False
        self.game.destroy()
        self.root.title("CONGRATULATIONS")
        self.enend = Winscreen(self.root, self.remake_main_game)

    def start_battle(self, player, x, y, floor):
        self.ongame = False
        self.game.destroy()
        self.root.title("BATTLE")
        self.battle_scene = Battlescreen(self.root, self.resume_main_game, self.game_over, player, x, y, floor)

    def game_over(self):
        self.ongame = False
        self.battle_scene.destroy()
        self.death_scene = Deathscreen(self.root)

    def remake_main_game(self):
        self.ongame = True
        self.enend.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_game, self.start_battle, self.open_inventory)
        self.game.assemble_rooms()

def up(event):
    if gme.ongame == True:
        gme.game.move_player("up")

def down(event):
    if gme.ongame == True:
        gme.game.move_player("down")

def left(event):
    if gme.ongame == True:
        gme.game.move_player("left")

def right(event):
    if gme.ongame == True:
        gme.game.move_player("right")

def openinventory(event):
    if gme.ongame == True:
        gme.game.open_inv_screen()

def closeinventory(event):
    if gme.ongame == False:
        gme.inv.goback()


gme = Put_Everything_Together()
gme.root.bind("<Up>", up)
gme.root.bind("<Down>", down)
gme.root.bind("<Left>", left)
gme.root.bind("<Right>", right)
gme.root.bind("<Key-z>", openinventory)
gme.root.bind("<Key-x>", closeinventory)
gme.pick_char()
gme.root.mainloop()