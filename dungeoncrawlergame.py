from tkinter import *
from roomcreator import *
from random import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=465, height=337, bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=4, rowspan=5)

        self.playarea = Text(self, width=50, height=13, font="consolas 12 bold")
        self.playarea["state"]=DISABLED
        self.print_screen()
        self.playarea.grid(row=0, column=0, columnspan=4)

        self.upb = Button(self, text=" ▲ ", bg="#8B4513", activebackground="#633310", command = self.move_up(self.current_room))
        self.upb.grid(row=2, column=1)
        self.leftb = Button(self, text=" ◀ ", bg="#8B4513", activebackground="#633310", command = self.move_left(self.current_room))
        self.leftb.grid(row=3, column=0, sticky=E)
        self.rightb = Button(self, text=" ▶ ", bg="#8B4513", activebackground="#633310", command = self.move_right(self.current_room))
        self.rightb.grid(row=3, column=2, sticky=W)
        self.downb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", command = self.move_down(self.current_room))
        self.downb.grid(row=4, column=1)
        self.centerb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", fg="#8B4513", activeforeground="#633310")
        self.centerb.grid(row=3, column=1)

        # this is a load-bearing label, please do NOT edit this.
        Label(self, text="", bg="#cc7130", width=52).grid(row=3, column=3)
    def move_up(self, room):
        if room.layout[self.xc][self.yc+1] == " ":
            room.layout[self.xc][self.yc] = " "
            self.yc += 1
            room.layout[self.xc][self.yc] = "Ü"
    def move_down(self,room):
        if room.layout[self.xc][self.yc] == " ":
            room.layout[self.xc][self.yc] = " "
            self.yc -= 1
            room.layout[self.xc][self.yc] = "Ü"
    def move_left(self,room):
        if room.layout[self.xc][self.yc] == " ":
            room.layout[self.xc][self.yc] = " "
            self.xc += 1
            room.layout[self.xc][self.yc] = "Ü"
    def move_right(self,room):
        if room.layout[self.xc][self.yc] == " ":
            room.layout[self.xc][self.yc] = " "
            self.xc -= 1
            room.layout[self.xc][self.yc] = "Ü"
    def move_player(self):
        # can't do that yet since I need to finish the gui oops
        print("this line is here so that the code will work")

    def print_screen(self):

        # Just edit this number for the room
        cr = randint(0, 2)

        s = ""
        r = load_room_file("testroom.txt")
        self.current_room = r[cr]
        self.spawn_character(self.current_room)

        h = ""
        for x in range(1, r[cr].xl+3):
            h += "#"

        s += h + "\n"
        for a in r[cr].layout:
            s += "#"
            for b in a:
                s += b
            s += "#\n"
        s += h

        self.playarea["state"] = NORMAL
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED

    def spawn_character(self, room):

        while 1==1:
            self.xc = randint(0, room.xl-1)
            self.yc = randint(0, room.yl-1)
            if room.layout[self.xc][self.yc] == " ":
                room.layout[self.xc][self.yc] = "Ü"
                return room

root = Tk()
root.title("GOI")
root.geometry("465x400")
root.configure(bg="#cc7130")

app = Application(root)
root.mainloop()