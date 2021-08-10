from tkinter import *
from time import sleep
from PIL import ImageTk, Image
class CustomBurger:
    def __init__(self):
        self.root=Tk()
        self.root.config(bg="black")
        self.root.title("Custom Loader")
        self.root.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.my_canvas = Canvas(self.root)
        self.my_canvas.pack(fill="both", expand=True)
        # setting background image in canvas.
        self.root.update()
        btn=Button(self.root,text="click",command=lambda:self.burger_animation(0,0,"buntop_img",1))
        btn.place(x=500,y=500)
        btn1 = Button(self.root, text="click",command=lambda:self.burger_animation(0,100,"chicken_img",2))
        btn1.place(x=600, y=600)
        self.root.mainloop()

    def burger_animation(self,x,y,name,num):
        self.names=['self.c','self.d','self.e']
        for i in range(1, 7):
            print(self.names)
            self.names[num]= ImageTk.PhotoImage(Image.open(f'{name}/{i}.png'))
            self.my_canvas.create_image(x, y, image=self.names[num], anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()

CustomBurger()
