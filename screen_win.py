from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self,
              text = "You Won!",
              font = ("Fixedsys", 50),
              ). grid(row=0, column=3, sticky=W)
        Button(self,
               text = "Play Again",
               font = ("Fixedsys", 20),
               bg = "Red",
               command = self.play_again
               ).grid(row=2,column=1,sticky=W)
        Button(self,
               text="Return To Title Screen",
               font=("Fixedsys", 20),
               bg="Blue",
               command = self.title
               ).grid(row=2, column=3, sticky=W)
        Button(self,
               text="Exit",
               font=("Fixedsys", 20),
               bg="Green",
               command = self.exit
               ).grid(row=2, column=5, sticky=W)
        Label(self
              ).grid(row=0, column=2, sticky=W)
        Label(self
              ).grid(row=0, column=4, sticky=W)
    def play_again(self):
        print(" ")
    def title(self):
        print(" ")
    def exit(self):
        exit()
root = Tk()
root.title("Win Screen")
app = Application(root)
root.mainloop()