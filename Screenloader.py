from tkinter import *
from dungeoncrawlergame import *
from itemcreator import *
from title_screen import *
from screen_win import *
from screen_battle import *
from screen_inventory import *
from screen_shop import *
from screen_death import *

class Put_Everything_Together(object):
    def __init__(self):
        self.root = Tk()

    def pick_char(self):
        self.root.title("START GAME")
        self.load_title = TitleScreen(self.root, self.start_cutscene)

    def start_cutscene(self):
        self.cs = "begin"
        self.load_title.destroy()
        self.root.title("BEGIN")
        self.sc = Winscreen(self.root, self.create_main_game, 1, None)

    def create_main_game(self):
        self.cs = "game"
        self.sc.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_level, self.start_battle, self.open_inventory, self.open_shop)
        self.itemlist = load_item_file("items.txt")
        for i in self.itemlist:
            if i.id == "hatchet":
                self.game.player.inventory.append(i)
                self.game.player.equipped = self.game.player.inventory[0]
            if i.id == "potion_min_heal":
                self.game.player.inventory.append(i)
        self.game.assemble_rooms()
        self.game.create_enemy_movement()

    def resume_main_game(self, level, player, x, y, floor, enemy):
        self.cs = "game"
        self.battle_scene.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_level, self.start_battle, self.open_inventory, self.open_shop, level, player, x, y, floor)
        self.game.add_moneydrop(enemy)
        self.game.kill_nearby_enemies()
        self.game.create_enemy_movement()
        self.game.print_screen()

    def open_inventory(self, level, player, x, y, floor):
        self.cs = "inventory"
        self.game.destroy()
        self.root.title("INVENTORY")
        self.inv = Inventoryscreen(self.root, self.close_inventory, level, player, x, y, floor)

    def close_inventory(self, level, player, x, y, floor):
        self.cs = "game"
        self.inv.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_level, self.start_battle, self.open_inventory, self.open_shop, level, player, x, y, floor)
        self.game.create_enemy_movement()
        self.game.print_screen()

    def open_shop(self, level, player, x, y, floor):
        self.cs = "shop"
        self.game.destroy()
        self.root.title("SHOP")
        self.shop = Shopscreen(self.root, self.close_shop, level, player, x, y, floor)

    def close_shop(self, level, player, x, y, floor):
        self.cs = "game"
        self.shop.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_level, self.start_battle, self.open_inventory, self.open_shop, level, player, x, y, floor)
        self.game.create_enemy_movement()
        self.game.print_screen()

    def end_level(self, level, player):
        self.cs = "end"
        self.game.destroy()
        self.root.title("CONGRATULATIONS")
        level += 1
        player.maxhealth += 5
        player.hp += 5
        self.enend = Winscreen(self.root, self.next_level, level, player)

    def start_battle(self, level, player, x, y, floor):
        self.cs = "battle"
        self.game.destroy()
        self.root.title("BATTLE")
        self.battle_scene = Battlescreen(self.root, self.resume_main_game, self.game_over, level, player, x, y, floor)

    def game_over(self):
        self.cs = "death"
        self.battle_scene.destroy()
        self.death_scene = Deathscreen(self.root)

    def next_level(self, level, player):
        self.cs = "game"
        self.enend.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_level, self.start_battle, self.open_inventory, self.open_shop, level, player)
        self.game.assemble_rooms()
        self.game.create_enemy_movement()

def up(event):
    if gme.cs == "game":
        gme.game.move_player("up")

def down(event):
    if gme.cs == "game":
        gme.game.move_player("down")

def left(event):
    if gme.cs == "game":
        gme.game.move_player("left")

def right(event):
    if gme.cs == "game":
        gme.game.move_player("right")

def pressz(event):
    if gme.cs == "inventory":
        gme.inv.use_item()

def pressx(event):
    if gme.cs == "inventory":
        gme.inv.equip_item()

def pressc(event):
    if gme.cs == "game":
        gme.game.open_inv_screen()
    elif gme.cs == "inventory":
        gme.inv.go_back()

gme = Put_Everything_Together()
gme.root.bind("<Up>", up)
gme.root.bind("<Down>", down)
gme.root.bind("<Left>", left)
gme.root.bind("<Right>", right)
gme.root.bind("<Key-z>", pressz)
gme.root.bind("<Key-x>", pressx)
gme.root.bind("<Key-c>", pressc)
gme.pick_char()
gme.root.mainloop()