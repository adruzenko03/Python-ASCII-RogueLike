from tkinter import *
from dungeoncrawlergame import *
from title_screen import *
from screen_win import *
from screen_battle import *
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
        self.game = Mainscreen(self.root, self.end_game, self.start_battle)
        self.game.assemble_rooms()

    def resume_main_game(self, player, x, y, floor):
        self.ongame = True
        self.battle_scene.destroy()
        self.root.title("DUNGEON")
        self.game = Mainscreen(self.root, self.end_game, self.start_battle, player, x, y, floor)
        self.game.kill_nearby_enemies()
        self.game.print_screen()

    def end_game(self):
        self.ongame = False
        self.game.destroy()
        self.root.title("CONGRATULATIONS")
        self.enend = Winscreen(self.root)

    def start_battle(self, player, x, y, floor):
        self.ongame = False
        self.game.destroy()
        self.root.title("BATTLE")
        self.battle_scene = Battlescreen(self.root, self.resume_main_game, self.game_over, player, x, y, floor)

    def game_over(self):
        self.ongame = False
        self.battle_scene.destroy()
        self.death_scene = Deathscreen(self.root)

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


gme = Put_Everything_Together()
gme.root.bind("<Up>", up)
gme.root.bind("<Down>", down)
gme.root.bind("<Left>", left)
gme.root.bind("<Right>", right)
gme.pick_char()
gme.root.mainloop()