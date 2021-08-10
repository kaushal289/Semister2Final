from tkinter import *
from PIL import ImageTk, Image
class Change_image:
    def __init__(self,):
        # create a tkinter window
        self.t = Tk()
        # Create a size for tkinter window
        self.t.geometry("300x200")  # here use alphabet 'x' not '*' this one
        # now set an image for moving
        self.img1 = ImageTk.PhotoImage(Image.open("details.png"))  # make sure that you have a photo
        # in you current folder that you are working with
        self.img2 = ImageTk.PhotoImage(Image.open("details_change.png"))
        self.img3 = ImageTk.PhotoImage(Image.open("information.png"))
        self.img4 = ImageTk.PhotoImage(Image.open("information_change.png"))
        # Create a label
        self.l = Label(self.t, font="bold")
        self.l.pack()
        # take a variable
        self.x = 1
        self.move()
        self.t.mainloop()
        # create a function for moving a picture
    def move(self):
        if self.x == 5:
            self.x = 1
        if self.x == 1:
            self.l.config(image=self.img1)  # by writing this line first picture will appear
        elif self.x == 2:
            self.l.config(image=self.img2)
        elif self.x == 3:
            self.l.config(image=self.img3)
        elif self.x == 4:
            self.l.config(image=self.img4)
        # you can do it for thousands of images
        # now increase the count by one
        self.x += 1
        # set images to work automatically by "after" feature in tkinter
        self.t.after(500, self.move)
c=Change_image()
