from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text=":D").grid(row=0, column=0, sticky=W)
        upb = Button(self, text=" ↑ ")
        upb.grid(row=1, column=1)
        leftb = Button(self, text=" ← ")
        leftb.grid(row=2, column=0)
        rightb = Button(self, text=" → ")
        rightb.grid(row=2, column=2)
        downb = Button(self, text=" ↓ ")
        downb.grid(row=3, column=1)

root = Tk()
root.title("GOI")
root.geometry("900x600")

app = Application(root)
root.mainloop()