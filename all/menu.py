from tkinter import *
from PIL import ImageTk, Image

class Menu:
    def __init__(self,master):
        self.root8=master
        self.root8.config(bg="black")
        self.root8.title("Menu")
        self.root8.state('zoomed')
        self.my_canvas = Canvas(self.root8)
        self.my_canvas.pack(fill="both", expand=True)
        self.back1 = ImageTk.PhotoImage(Image.open(f'burger_background.jpg'))
        self.my_canvas.create_image(0, 0, image=self.back1, anchor="nw")
        self.root8.mainloop()

Menu(Tk())

