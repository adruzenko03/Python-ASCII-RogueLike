from tkinter import *
from roomcreator import *
from random import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=460, height=560, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=5, rowspan=6)

        self.playarea = Text(self, width=50, height=13, font="consolas 12 bold")
        self.playarea["state"]=DISABLED
        self.print_screen()
        self.playarea.grid(row=0, column=0, columnspan=5)

        self.upb = Button(self, text=" ▲ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("up"))
        self.upb.grid(row=2, column=1)
        self.leftb = Button(self, text=" ◀ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("left"))
        self.leftb.grid(row=3, column=0, sticky=E)
        self.rightb = Button(self, text=" ▶ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("right"))
        self.rightb.grid(row=3, column=2, sticky=W)
        self.downb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("down"))
        self.downb.grid(row=4, column=1)
        self.centerb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", fg="#8B4513", activeforeground="#633310")
        self.centerb.grid(row=3, column=1)
        self.message_log = Text(self, width=25, height=15, wrap=WORD)
        self.message_log.grid(row=2, column=4, rowspan=4, sticky=N)

        # these are load-bearing labels, please do NOT edit these.
        Label(self, text="", bg="#cc7130", height=1).grid(row=1, column=1)
        Label(self, text="", bg="#cc7130", width=20).grid(row=3, column=3)
        Label(self, text="", bg="#cc7130", height=12).grid(row=5, column=0)

    def move_player(self, direction):

        s = ""

        if direction == "up":

            if self.floor[self.player_x - 1][self.player_y] == " ":

                self.floor[self.player_x - 1][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x -= 1

        if direction == "down":

            if self.floor[self.player_x + 1][self.player_y] == " ":
                self.floor[self.player_x + 1][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x += 1

        if direction == "left":

            if self.floor[self.player_x][self.player_y - 1] == " ":
                self.floor[self.player_x][self.player_y - 1] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y -= 1

        if direction == "right":

            if self.floor[self.player_x][self.player_y + 1] == " ":
                self.floor[self.player_x][self.player_y + 1] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y += 1

        for a in self.floor:
            for b in a:
                s += b
            s += "\n"

        self.playarea["state"] = NORMAL
        self.playarea.delete(0.0, END)
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED


    def print_screen(self):

        # Just edit this number for the room
        cr = randint(0, 5)

        s = ""
        r = load_room_file("testroom.txt")

        self.spawn_character(r[cr])

        h = ""
        for x in range(1, r[cr].xl+3):
            h += "█"

        s += h + "\n"
        for a in r[cr].layout:
            s += "█"
            for b in a:
                if b == "#":
                    s += "█"
                else:
                    s += b
            s += "█\n"
        s += h

        i = ""

        self.floor = [[]]
        for tile in s:
            if tile == "\n":
                self.floor.append([])
            elif tile != "n":
                self.floor[-1].append(tile)
            if tile == "Ü":
                self.player_x = len(self.floor)-1
                self.player_y = len(self.floor[-1])-1

        for a in self.floor:
            for b in a:
                i += b
            i += "\n"

        self.playarea["state"] = NORMAL
        self.playarea.insert(0.0, i)
        self.playarea["state"] = DISABLED

    def spawn_character(self, room):

        while 1==1:
            xc = randint(0, room.xl-1)
            yc = randint(0, room.yl-1)
            if room.layout[xc][yc] == " ":
                room.layout[xc][yc] = "Ü"
                return room

root = Tk()
root.title("GOI")
root.geometry("465x550")
root.configure(bg="#cc7130")

app = Application(root)
root.mainloop()
