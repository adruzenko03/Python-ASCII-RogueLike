from tkinter import *
from roomcreator import *

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

        self.upb = Button(self, text=" ▲ ", bg="#8B4513", activebackground="#633310")
        self.upb.grid(row=2, column=1)
        self.leftb = Button(self, text=" ◀ ", bg="#8B4513", activebackground="#633310")
        self.leftb.grid(row=3, column=0, sticky=E)
        self.rightb = Button(self, text=" ▶ ", bg="#8B4513", activebackground="#633310")
        self.rightb.grid(row=3, column=2, sticky=W)
        self.downb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310")
        self.downb.grid(row=4, column=1)
        self.centerb = Button(self, text=" ▼ ", bg="#8B4513", activebackground="#633310", fg="#8B4513", activeforeground="#633310")
        self.centerb.grid(row=3, column=1)

        # this is a load-bearing label, please do NOT edit this.
        Label(self, text="", bg="#cc7130", width=52).grid(row=3, column=3)

    def move_player(self):
        # can't do that yet since I need to finish the gui oops
        print("this line is here so that the code will work")

    def print_screen(self):

        s = ""
        r = load_room_file_v2("testroom.txt")

        h = ""
        for x in range(1, r[0].xl+3):
            h += "#"

        s += h + "\n"
        for a in r[0].layout:
            s += "#"
            for b in a:
                s += b
            s += "#\n"
        s += h

        self.playarea["state"] = NORMAL
        self.playarea.insert(0.0, s)
        self.playarea["state"] = DISABLED


root = Tk()
root.title("GOI")
root.geometry("465x400")
root.configure(bg="#cc7130")

app = Application(root)
root.mainloop()