from tkinter import *
from roomcreator import *
from random import *
from copy import *


class Player(object):

    def __init__(self, maxhealth, money=0):
        self.hp = maxhealth
        self.money = money


class Mainscreen(Frame):

    def __init__(self, master, endo, bat, openinv, player=None, x=None, y=None, floor=None):
        super().__init__(master)
        self.grid()
        if player == None:
            self.player = Player(100)
        else:
            self.player = player
        self.level = 1
        self.player_x = x
        self.player_y = y
        self.floor = floor
        self.openinv = openinv
        self.create_widgets()
        self.endo = endo
        self.bat = bat


    def create_widgets(self):

        # Background
        Canvas(self, bg="#cc7130", width=480, height=575, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=6, rowspan=8)

        # Screen
        self.playarea = Text(self, width=49, height=13, font="consolas 12 bold")
        self.playarea["state"]=DISABLED
        self.playarea.grid(row=0, column=0, columnspan=6)

        # Movement Buttons
        self.upb = Button(self, text=" ▲ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("up"))
        self.upb.grid(row=2, column=1)
        self.leftb = Button(self, text=" ◀ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("left"))
        self.leftb.grid(row=3, column=0, sticky=E)
        self.rightb = Button(self, text=" ▶ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("right"))
        self.rightb.grid(row=3, column=2, sticky=W)
        self.downb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", command=lambda: self.move_player("down"))
        self.downb.grid(row=4, column=1)
        self.centerb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", fg="#8B4513", command=self.open_inv_screen, activeforeground="#633310")
        self.centerb.grid(row=3, column=1)

        # Message Log
        self.message_log_sb = Scrollbar(self)
        self.message_log_sb.grid(row=2, column=5, rowspan=6, sticky=NS)
        self.message_log = Text(self, width=25, height=17, wrap=WORD, yscrollcommand=self.message_log_sb.set)
        self.message_log.grid(row=2, column=4, rowspan=6)
        self.message_log_sb["command"] = self.message_log.yview

        # Displays
        self.health_display = Label(self, text=" ❤ "+str(self.player.hp)+" ", font="fixedsys", bg="#960c0c", width=11, relief=SUNKEN)
        self.health_display.grid(row=5, column=0, columnspan=3)
        self.money_display = Label(self, text=" ¢ " + str(self.player.money) + " ", font="fixedsys", bg="#ce9d0a", width=11, relief=SUNKEN)
        self.money_display.grid(row=6, column=0, columnspan=3)

        # Load-Bearing Labels (Do not edit)
        Label(self, text="", bg="#cc7130", height=1).grid(row=1, column=1)
        Label(self, text="", bg="#cc7130", width=18, height=2).grid(row=3, column=3)
        Label(self, text="", bg="#cc7130", height=11).grid(row=7, column=0)

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
            elif self.floor[self.player_x - 1][self.player_y] == "□":
                self.floor[self.player_x - 2][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x -= 2
                self.message_leg("up")
            elif self.floor[self.player_x - 1][self.player_y] == "X":
                self.end_gme()

        if direction == "down":

            if self.floor[self.player_x + 1][self.player_y] == " ":
                self.floor[self.player_x + 1][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x += 1
                self.message_leg("down")
            elif self.floor[self.player_x + 1][self.player_y] == "□":
                self.floor[self.player_x + 2][self.player_y] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_x += 2
                self.message_leg("down")
            elif self.floor[self.player_x + 1][self.player_y] == "X":
                self.end_gme()

        if direction == "left":

            if self.floor[self.player_x][self.player_y - 1] == " ":
                self.floor[self.player_x][self.player_y - 1] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y -= 1
                self.message_leg("left")
            elif self.floor[self.player_x][self.player_y - 1] == "□":
                self.floor[self.player_x][self.player_y - 2] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y -= 2
                self.message_leg("left")
            elif self.floor[self.player_x][self.player_y - 1] == "X":
                self.end_gme()

        if direction == "right":

            if self.floor[self.player_x][self.player_y + 1] == " ":
                self.floor[self.player_x][self.player_y + 1] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y += 1
                self.message_leg("right")
            elif self.floor[self.player_x][self.player_y + 1] == "□":
                self.floor[self.player_x][self.player_y + 2] = "Ü"
                self.floor[self.player_x][self.player_y] = " "
                self.player_y += 2
                self.message_leg("right")
            elif self.floor[self.player_x][self.player_y + 1] == "X":
                self.end_gme()

        for a in self.floor:
            for b in a:
                s += b
            s += "\n"

        self.print_screen()

        if self.floor[self.player_x - 1][self.player_y] == "Ö" or self.floor[self.player_x + 1][self.player_y] == "Ö" or self.floor[self.player_x][self.player_y - 1] == "Ö" or self.floor[self.player_x][self.player_y + 1]== "Ö":
            self.destroy()
            self.do_battle()

        """ self.playarea["state"] = NORMAL
        self.playarea.delete(0.0, END)
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED """

    def assemble_rooms(self):

        # Loads room file and gets the starting room from that file
        roomfile = load_room_file("testroom.txt")
        base = [deepcopy(roomfile[randint(1, len(roomfile)-1)]), 0, 0]
        # !!!! roomgrid.delete(0.0, END)!!!!
        # Adds the start room to the list
        roomgrid = [base]
        # Maximum number of room is that number plus 1
        maxrooms = 8

        # Runs until all the rooms are made
        while maxrooms > 1:

            # Selects a room and a direction
            condition = True
            selectedroom = choice(roomgrid)
            direction = randint(1, 4)

            # Based on the direction, it will place a room in that direction of the selected room
            if direction == 1:
                # Runs for each room in the list to make sure the room won't overlay another room
                for x in roomgrid:
                    if selectedroom[1] == x[1] and selectedroom[2]-1 == x[2]:
                        condition = False
                # If there isn't a room there, it makes a room there
                if condition == True:
                    roomgrid.append([deepcopy(roomfile[randint(1, len(roomfile)-1)]), selectedroom[1], selectedroom[2] - 1])

            if direction == 2:
                for x in roomgrid:
                    if selectedroom[1] == x[1] and selectedroom[2]+1 == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([deepcopy(roomfile[randint(1, len(roomfile)-1)]), selectedroom[1], selectedroom[2]+1])

            if direction == 3:
                for x in roomgrid:
                    if selectedroom[1]-1 == x[1] and selectedroom[2] == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([deepcopy(roomfile[randint(1, len(roomfile)-1)]), selectedroom[1]-1, selectedroom[2]])

            if direction == 4:
                for x in roomgrid:
                    if selectedroom[1]+1 == x[1] and selectedroom[2] == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([deepcopy(roomfile[randint(1, len(roomfile)-1)]), selectedroom[1]+1, selectedroom[2]])

            if condition == True:
                maxrooms -= 1

        while maxrooms == 1:
            # Selects a room and a direction
            condition = True
            selectedroom = choice(roomgrid)
            direction = randint(1, 4)

            # Based on the direction, it will place a room in that direction of the selected room
            if direction == 1:
                # Runs for each room in the list to make sure the room won't overlay another room
                for x in roomgrid:
                    if selectedroom[1] == x[1] and selectedroom[2] - 1 == x[2]:
                        condition = False
                # If there isn't a room there, it makes a room there
                if condition == True:
                    roomgrid.append([roomfile[0], selectedroom[1], selectedroom[2] - 1])

            if direction == 2:
                for x in roomgrid:
                    if selectedroom[1] == x[1] and selectedroom[2] + 1 == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[0], selectedroom[1], selectedroom[2] + 1])

            if direction == 3:
                for x in roomgrid:
                    if selectedroom[1] - 1 == x[1] and selectedroom[2] == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[0], selectedroom[1] - 1, selectedroom[2]])

            if direction == 4:
                for x in roomgrid:
                    if selectedroom[1] + 1 == x[1] and selectedroom[2] == x[2]:
                        condition = False
                if condition == True:
                    roomgrid.append([roomfile[0], selectedroom[1] + 1, selectedroom[2]])

            if condition == True:
                break

        # Creates the lowest number for the coordinates and the maximum number for the coordinates
        lowx = 0
        lowy = 0
        maxx = 0
        maxy = 0

        # Finds if any rooms are negative
        for x in roomgrid:
            if x[1] < 0 and x[1] < lowx:
                lowx = x[1]
            if x[2] < 0 and x[2] < lowy:
                lowy = x[2]
            if x[1] > 0 and x[1] > maxx:
                maxx = x[1]
            if x[2] > 0 and x[2] > maxy:
                maxy = x[2]

        # Adjusts the max to fit the negative numbers
        maxx -= lowx
        maxy -= lowy
        for x in roomgrid:
            x[1] -= lowx
            x[2] -= lowy

        # Creates enemies
        numofenemies = 2 + self.level

        availablerooms = deepcopy(roomgrid)

        for a in range(0, numofenemies):
            while 1 == 1:
                r = randint(0, len(roomgrid)-2)
                if availablerooms[r][0] != "used":
                    break
            while 1 == 1:
                rx = randint(0, 14)
                ry = randint(0, 14)
                if roomgrid[r][0].layout[rx][ry] == " ":
                    roomgrid[r][0].layout[rx][ry] = "Ö"
                    break
            availablerooms[r][0] = "used"

        # Creates the top row of blocks
        s = ""
        for x in range(0, ((maxx+1)*15)+maxx+2):
            s += "#"
        s += "\n"

        templist = []

        # Runs for each line
        for a in range(0, maxy+1):
            # Runs for each thing in the line
            for b in range(0, maxx+1):
                # Finds if there is a room
                con = False
                for c in roomgrid:
                    if c[1] == b and c[2] == a:
                        con = True
                        break
                # Adds room
                if con == True:
                    templist.append(c)
                # Adds a blank
                else:
                    templist.append("blank")
            # Starts assembling rooms
            for d in range(0, 15):
                s += "#"
                # Runs for each thing in the list
                for e in templist:
                    # Adds a row of blanks if there is no room
                    if e == "blank":
                        s += "###############"
                    # Adds a row for the room
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

        for a in roomgrid:
            for b in roomgrid:
                if a[1]+1 == b[1] and a[2] == b[2]:
                    while 1== 1:
                        dp = randint(0, 14)
                        if self.floor[16*(a[2])+dp][16*(a[1]+1)+1] == " " and self.floor[16*(a[2])+dp][16*(a[1]+1)-1] == " ":
                            self.floor[16*(a[2])+dp][16*(a[1]+1)] = "□"
                            break
                if a[1] == b[1] and a[2]+1 == b[2]:
                    while 1 == 1:
                        dp = randint(0, 14)
                        if self.floor[16*(a[2]+1)+1][16*(a[1])+dp] == " " and self.floor[16*(a[2]+1)-1][16*(a[1])+dp] == " ":
                            self.floor[16*(a[2]+1)][16*(a[1])+dp] = "□"
                            break

        self.spawn_character(self.floor, len(self.floor), len(self.floor[0]))

        for a in self.floor:
            for b in a:
                i += b
            i += "\n"

        self.print_screen()

    def print_screen(self):

        s = ""

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

        s = s[:-1]

        self.playarea["state"] = NORMAL
        self.playarea.delete(0.0, END)
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED

    def kill_nearby_enemies(self):

        if self.floor[self.player_x - 1][self.player_y] == "Ö":
            self.floor[self.player_x - 1][self.player_y] = " "

        if self.floor[self.player_x + 1][self.player_y] == "Ö":
            self.floor[self.player_x + 1][self.player_y] = " "

        if self.floor[self.player_x][self.player_y - 1] == "Ö":
            self.floor[self.player_x][self.player_y - 1] = " "

        if self.floor[self.player_x][self.player_y + 1] == "Ö":
            self.floor[self.player_x][self.player_y + 1] = " "

    def spawn_character(self, room, xl, yl):

        while 1==1:
            xc = randint(0, xl-1)
            yc = randint(0, yl-1)
            if room[xc][yc] == " ":
                room[xc][yc] = "Ü"
                self.player_x = xc
                self.player_y = yc
                return room

    def add_moneydrop(self, enemy):
        money = randint(int(enemy.moneydrop[0]), int(enemy.moneydrop[1]))
        self.player.money += money
        self.money_display["text"] = " ¢ " + str(self.player.money) + " "
        self.message_log.insert(0.0, "-Bup got " + str(money) + " gold for killing the " + enemy.name + "!")

    def end_gme(self):
        self.endo()

    def do_battle(self):
        self.bat(self.player, self.player_x, self.player_y, self.floor)

    def open_inv_screen(self):
        self.openinv(self.player, self.player_x, self.player_y, self.floor)


# root = Tk()
# root.title("GOI")
# root.geometry("485x568")
# root.configure(bg="#cc7130")

# mainscreen = Mainscreen(root)
# root.mainloop()
