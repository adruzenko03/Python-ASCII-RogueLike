from tkinter import *
class Put_Everything_Together(object):
    def __init__(self):
        self.root = Tk()

    def pick_char(self):
        self.root.title("BAAAACCCOOOOOOOOON!!!")
        self.load_title = title_screen(self.root, self.main_game)

    def main_game(self):
        self.load_title.destroy()
        self.root.title("JESSSSSSSUUUUUUUSSSS")
        self.game = dungeoncrawlergame(self.root, self.end)

    def end(self):
        self.game.destroy()
        self.root.title("This is importante")
        self.enend = fljngeojvdfn(self.root)

def main()
    gme = Put_Everything_Together()
    gme.pick_char()
    gme.root.mainloop()

main()