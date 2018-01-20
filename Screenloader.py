from tkinter import *
from dungeoncrawlergame import *
from title_screen import *
from screen_win import *

class Put_Everything_Together(object):
    def __init__(self):
        self.root = Tk()

    def pick_char(self):
        self.root.title("BAAAACCCOOOOOOOOON!!!")
        self.load_title = TitleScreen(self.root, self.main_game)

    def main_game(self):
        self.ongame = True
        self.load_title.destroy()
        self.root.title("JESSSSSSSUUUUUUUSSSS")
        self.game = Mainscreen(self.root, self.end_game)

    def end_game(self):
        self.ongame = False
        self.game.destroy()
        self.root.title("This is importante")
        self.enend = Winscreen(self.root)

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