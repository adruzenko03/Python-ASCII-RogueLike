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
        self.load_title.destroy()
        self.root.title("JESSSSSSSUUUUUUUSSSS")
        self.game = Mainscreen(self.root, self.end_game)

    def end_game(self):
        self.game.destroy()
        self.root.title("This is importante")
        self.enend = Winscreen(self.root)

gme = Put_Everything_Together()
gme.pick_char()
gme.root.mainloop()