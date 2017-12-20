from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="*insert game here*").grid(row=0, column=0, sticky=W)

root = Tk()
root.title("Dungeon Crawler")
root.geometry("405x300")

app = Application(root)
root.mainloop()