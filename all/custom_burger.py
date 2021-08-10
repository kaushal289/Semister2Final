from tkinter import *
from tkinter.constants import DISABLED, NORMAL
from time import sleep
from PIL import ImageTk, Image

class CustomBurger:
    def __init__(self):
        self.root=Tk()
        self.root.config(bg="black")
        self.root.title("Custom Loader")
        self.root.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.a = 450
        self.b = 230
        self.back1 = ImageTk.PhotoImage(Image.open(f'burger_background.jpg'))
        self.btn_img = ImageTk.PhotoImage(Image.open(f'btn_img.png'))
        self.btn_img_small = ImageTk.PhotoImage(Image.open(f'btn_img_small.png'))
        self.img_box =Image.open('burgar_box.png')
        self.img_box = self.img_box.resize((600,80), Image.ANTIALIAS)
        self.box_img = ImageTk.PhotoImage(self.img_box)
        self.my_canvas = Canvas(self.root)
        self.my_canvas.pack(fill="both", expand=True)
        self.my_canvas.create_image(0, 0, image=self.back1, anchor="nw")
        self.my_canvas.create_line(1030, 280, 1030, 500, width=5, fill="brown")
        self.my_canvas.create_image(420, 85, image=self.box_img, anchor="nw")
        self.my_canvas.create_text(700, 130, text="CUSTOM BURGER", font=("Algerian", 35, 'bold'), fill="black")
        self.my_canvas.create_text(900, 300, text="Vage", font=("Algerian", 30, 'bold'), fill="black")
        self.my_canvas.create_text(1150, 300, text="Non-vage", font=("Algerian", 30, 'bold'), fill="black")
        # setting background image in canvas.
        self.btn_top=Button(self.root,text="Lets Get Started",cursor="hand2",overrelief="sunken",
                           font=("Algerian", 20, 'bold'),compound=CENTER,fg="white",
                           image=self.btn_img,borderwidth=0,command=self.burger_buttom).place(x=870,y=200)
        self.btn_buttom = Button(self.root, text="Finish",image=self.btn_img_small,
                     compound=CENTER,font=("Algerian", 20, 'bold'),fg="white",
                     command=self.burger_top).place(x=800, y=550)
        self.btn_tomato = Button(self.root, text="Tomato", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="white",
                                 command=self.burger_tomato).place(x=800, y=330)
        self.btn_pickle = Button(self.root, text="Pickle", image=self.btn_img_small,
                                  compound=CENTER, font=("Algerian", 20, 'bold'), fg="white",
                                  command=self.burger_pickel).place(x=800, y=390)
        self.btn_chees = Button(self.root, text="Cheese", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="white",
                                 command=self.burger_chees).place(x=800, y=450)
        self.btn_chicken = Button(self.root, text="Chicken", image=self.btn_img_small,
                                compound=CENTER, font=("Algerian", 20, 'bold'), fg="white",
                                command=self.burger_chicken).place(x=1050, y=450)
        self.btn_reset = Button(self.root, text="Reset", image=self.btn_img_small,compound=CENTER,
                                font=("Algerian", 20, 'bold'), fg="white",command=self.reset)
        self.btn_reset.place(x=1050, y=550)
        self.root.update()
        self.root.mainloop()

    def reset(self):
        del globals()[self.burger_buttom()]
    def burger_buttom(self):
        for i in range(1, 7):
            self.login1 = ImageTk.PhotoImage(Image.open(f'bunbutton_img/{i}.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login1, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()

    def burger_top(self):
        self.a = self.a - 50
        for i in range(1, 7):
            self.login = ImageTk.PhotoImage(Image.open(f'buntop_img/{i}.png'))
            self.my_canvas.create_image(self.b,self.a, image=self.login, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()

    def burger_tomato(self):
        self.a = self.a - 30
        for i in range(1, 7):
            self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/{i}.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login2, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()
    def burger_pickel(self):
        self.a = self.a - 30
        for i in range(1, 7):
            self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/{i}.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login3, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()
    def burger_chees(self):
        self.a = self.a - 20
        for i in range(1, 7):
            self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/{i}.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login4, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()
    def burger_chicken(self):
        self.a = self.a - 40
        for i in range(1, 7):
            self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/{i}.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login5, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()



CustomBurger()
