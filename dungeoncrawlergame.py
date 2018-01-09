from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Canvas(self, bg="#cc7130", width=465, height=350, bd=0, highlightthickness=0).grid(row=0, rowspan=17, column=0, columnspan=4)

        self.playarea = Text(self, width=50, height=13, font="consolas")
        self.playarea.insert(0.0, "###■########□###\n"
                                  "#              #\n"
                                  "#          ◙   #\n"
                                  "#              #\n"
                                  "#        Ü     #\n"
                                  "#              #\n"
                                  "#              #\n"
                                  "#              #\n"
                                  "#              #\n"
                                  "#              #\n"
                                  "###■########□###")
        self.playarea["state"]=DISABLED
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

    def movePlayer(self):
        # can't do that yet since I need to finish the gui oops
        print("this line is here so that the code will work")

root = Tk()
root.title("GOI")
root.geometry("465x400")
root.configure(bg="#cc7130")

app = Application(root)
root.mainloop()