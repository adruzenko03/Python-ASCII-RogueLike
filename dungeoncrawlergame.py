from tkinter import *
from roomcreator import *
from random import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=480, height=560, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=6, rowspan=6)

        self.playarea = Text(self, width=49, height=13, font="consolas 12 bold")
        self.playarea["state"]=DISABLED
        self.assemble_rooms()
        self.playarea.grid(row=0, column=0, columnspan=6)

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
        self.message_log_sb = Scrollbar(self)
        self.message_log_sb.grid(row=2, column=5, rowspan=4, sticky=NS)
        self.message_log = Text(self, width=25, height=17, wrap=WORD, yscrollcommand=self.message_log_sb.set)
        self.message_log.grid(row=2, column=4, rowspan=4)
        self.message_log_sb["command"] = self.message_log.yview

        # these are load-bearing labels, please do NOT edit these.
        Label(self, text="", bg="#cc7130", height=1).grid(row=1, column=1)
        Label(self, text="", bg="#cc7130", width=18).grid(row=3, column=3)
        Label(self, text="", bg="#cc7130", height=12).grid(row=5, column=0)

    def message_leg(self, direction):

        if direction == "up":
            self.message_log.insert(0.0, "You moved up\n")
        if direction == "left":
            self.message_log.insert(0.0, "You moved left\n")
        if direction == "right":
            self.message_log.insert(0.0, "You moved right\n")
        if direction == "down":
            self.message_log.insert(0.0, "You moved down\n")

    def move_player(self, direction):

        s = ""

        if direction == "up":

            if self.floor[self.player_x - 1][self.player_y] == " ":

                self.floor[self.player_x - 1][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x -= 1
                self.message_leg("up")

        if direction == "down":

            if self.floor[self.player_x + 1][self.player_y] == " ":
                self.floor[self.player_x + 1][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x += 1
                self.message_leg("down")

        if direction == "left":

            if self.floor[self.player_x][self.player_y - 1] == " ":
                self.floor[self.player_x][self.player_y - 1] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y -= 1
                self.message_leg("left")

        if direction == "right":

            if self.floor[self.player_x][self.player_y + 1] == " ":
                self.floor[self.player_x][self.player_y + 1] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y += 1
                self.message_leg("right")

        for a in self.floor:
            for b in a:
                s += b
            s += "\n"

        self.print_screen()

        """ self.playarea["state"] = NORMAL
        self.playarea.delete(0.0, END)
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED """

    def assemble_rooms(self):

        roomfile = load_room_file("testroom.txt")
        base = [roomfile[randint(0, 11)], 0, 0]

        roomgrid = [base]

        maxrooms = 8

        while maxrooms > 0:

            condition = True
            selectedroom = choice(roomgrid)
            direction = randint(1, 4)

            if direction == 1:
                for x in roomgrid:
                    if selectedroom[1] == x[1] and selectedroom[2]-1 == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[randint(0, 11)], selectedroom[1], selectedroom[2] - 1])

            if direction == 2:
                for x in roomgrid:
                    if selectedroom[1] == x[1] and selectedroom[2]+1 == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[randint(0, 11)], selectedroom[1], selectedroom[2]+1])

            if direction == 3:
                for x in roomgrid:
                    if selectedroom[1]-1 == x[1] and selectedroom[2] == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[randint(0, 11)], selectedroom[1]-1, selectedroom[2]])

            if direction == 4:
                for x in roomgrid:
                    if selectedroom[1]+1 == x[1] and selectedroom[2] == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[randint(0, 11)], selectedroom[1]+1, selectedroom[2]])

            if condition == True:
                maxrooms -= 1

        lowx = 0
        lowy = 0
        maxx = 0
        maxy = 0

        for x in roomgrid:
            if x[1] < 0 and x[1] < lowx:
                lowx = x[1]
            if x[2] < 0 and x[2] < lowy:
                lowy = x[2]
            if x[1] > 0 and x[1] > maxx:
                maxx = x[1]
            if x[2] > 0 and x[2] > maxy:
                maxy = x[2]

        maxx -= lowx
        maxy -= lowy
        for x in roomgrid:
            x[1] -= lowx
            x[2] -= lowy

        s = ""
        for x in range(0, ((maxx+1)*15)+maxx+2):
            s += "#"
        s += "\n"

        templist = []

        for a in range(0, maxy+1):
            for b in range(0, maxx+1):
                con = False
                for c in roomgrid:
                    if c[1] == b and c[2] == a:
                        con = True
                        break
                if con == True:
                    templist.append(c)
                else:
                    templist.append("blank")
            for d in range(0, 15):
                s += "#"
                for e in templist:
                    if e == "blank":
                        s += "###############"
                    else:
                        for f in range(0, 15):
                            s += e[0].layout[d][f]
                    s += "#"
                s += "\n"
            for x in range(0, ((maxx + 1) * 15) + maxx + 2):
                s += "#"
            s += "\n"
            templist = []

        print(s)

        i = ""

        self.floor = [[]]
        for t in range(0, len(s)):
            if s[t] == "\n":
                self.floor.append([])
            elif s[t] != "#":
                self.floor[-1].append(s[t])
            else:
                self.floor[-1].append("█")
            if t == "Ü":
                self.player_x = len(self.floor)-1
                self.player_y = len(self.floor[-1])-1

        self.spawn_character(self.floor, len(self.floor), len(self.floor[0]))

        for a in self.floor:
            for b in a:
                i += b
            i += "\n"

        self.print_screen()


    def print_screen(self):

        s = ""

        """ for a in range(0, len(self.floor)-1):
            if len(self.floor[0]) < 50:
                for b in self.floor[a]:
                    s += b[a]
            elif self.player_x < 25:
                for b in range(0, 49):
                    s += self.floor[a][b]
            elif self.player_x > len(self.floor)-24:
                for b in range(len(self.floor)-49, len(self.floor)):
                    s += self.floor[a][b]
            else:
                for b in range(self.player_x-24, self.player_x+25):
                    s += self.floor[a][b] """

        if self.player_x <= 7:
            for a in range(0, 13):
                if len(self.floor[0]) <= 49:
                    for b in self.floor[a]:
                        s += b
                    s += "\n"
                elif self.player_y <= 25:
                    for b in range(0, 49):
                        s += self.floor[a][b]
                    s += "\n"
                elif self.player_y >= len(self.floor[0])-25:
                    for b in range(len(self.floor[0])-49, len(self.floor[0])):
                        s += self.floor[a][b]
                    s += "\n"
                else:
                    for b in range(self.player_y-24, self.player_y+25):
                        s += self.floor[a][b]
                    s += "\n"

                """ for b in self.floor[a]:
                    s += b
                s += "\n" """

        elif self.player_x >= len(self.floor)-7:
            for a in range(len(self.floor)-13, len(self.floor)-1):
                if len(self.floor[0]) <= 49:
                    for b in self.floor[a]:
                        s += b
                    s += "\n"
                elif self.player_y <= 25:
                    for b in range(0, 49):
                        s += self.floor[a][b]
                    s += "\n"
                elif self.player_y >= len(self.floor[0])-25:
                    for b in range(len(self.floor[0])-49, len(self.floor[0])):
                        s += self.floor[a][b]
                    s += "\n"
                else:
                    for b in range(self.player_y-24, self.player_y+25):
                        s += self.floor[a][b]
                    s += "\n"

        else:
            for a in range(self.player_x-6, self.player_x+7):
                if len(self.floor[0]) <= 49:
                    for b in self.floor[a]:
                        s += b
                    s += "\n"
                elif self.player_y <= 25:
                    for b in range(0, 49):
                        s += self.floor[a][b]
                    s += "\n"
                elif self.player_y >= len(self.floor[0])-25:
                    for b in range(len(self.floor[0])-49, len(self.floor[0])):
                        s += self.floor[a][b]
                    s += "\n"
                else:
                    for b in range(self.player_y-24, self.player_y+25):
                        s += self.floor[a][b]
                    s += "\n"

        self.playarea["state"] = NORMAL
        self.playarea.delete(0.0, END)
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED

    def spawn_character(self, room, xl, yl):

        while 1==1:
            xc = randint(0, xl-1)
            yc = randint(0, yl-1)
            if room[xc][yc] == " ":
                room[xc][yc] = "Ü"
                self.player_x = xc
                self.player_y = yc
                return room


root = Tk()
root.title("GOI")
root.geometry("485x568")
root.configure(bg="#cc7130")

app = Application(root)
root.mainloop()
