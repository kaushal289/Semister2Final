from tkinter import *

from time import sleep
from PIL import ImageTk, Image

class CustomBurger:
    def __init__(self):
        self.root=Tk()
        self.root.config(bg="black")
        self.root.title("Custom Loader")
        self.root.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.back1 = ImageTk.PhotoImage(Image.open(f'burger_background.jpg'))
        self.btn_img = ImageTk.PhotoImage(Image.open(f'btn_img.png'))
        self.btn_img_small = ImageTk.PhotoImage(Image.open(f'btn_img_small.png'))
        self.img_box =Image.open('burgar_box.png')
        self.img_box = self.img_box.resize((600,80), Image.ANTIALIAS)
        self.box_img = ImageTk.PhotoImage(self.img_box)
        self.my_canvas = Canvas(self.root)
        self.my_canvas.pack(fill="both", expand=True)
        self.my_canvas.create_image(0, 0, image=self.back1, anchor="nw")

        self.my_canvas.create_image(420, 85, image=self.box_img, anchor="nw")
        self.my_canvas.create_text(700, 130, text="CUSTOM BURGER", font=("Algerian", 35, 'bold'), fill="black")

        # setting background image in canvas.
        self.btn_top=Button(self.root,text="Start making",cursor="hand2",overrelief="sunken",
                           font=("Algerian", 40, 'bold'),compound=CENTER,fg="white",bg='brown2',borderwidth=0,command=self.burger_buttom)
        self.btn_top.place(x=870,y=350)


        self.a=550
        self.b=230
        self.count=0
        self.count_pi=0
        self.count_fi=0
        self.count_ch=0
        self.count_ce=0
        self.count_to=0
        self.count_sp = 0

        self.root.update()
        self.root.mainloop()
    def reset(self):
        self.a = 450
        self.b = 230
        self.login2 = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login2, anchor="nw")
        self.login3 = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login3, anchor="nw")
        self.login4 = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login4, anchor="nw")
        self.login5 = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login5, anchor="nw")
        self.login = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login, anchor="nw")
        self.login6 = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login6, anchor="nw")
        self.login7 = ImageTk.PhotoImage(Image.open(f'remove.png'))
        self.my_canvas.create_image(self.b, self.a, image=self.login7, anchor="nw")

        self.btn_tomato.config(text="Tomato:No", bg="black",fg="red4")
        self.btn_chicken.config(text="Chicken:No", bg="black",fg="red4")
        self.btn_chees.config(text="Cheese:No", bg="black",fg="red4")
        self.btn_pickle.config(text="Pickle:No", bg="black",fg="red4")
        self.btn_fish.config(text="Fish:No", bg="black",fg="red4")
        self.btn_spinach.config(text="Spinach:No", bg="black", fg="red4")




    def burger_buttom(self):
        self.btn_top.place_forget()

        self.my_canvas.create_line(1030, 280, 1030, 500, width=5, fill="brown")
        self.my_canvas.create_text(900, 250, text="Vage", font=("Algerian", 30, 'bold'), fill="black")
        self.my_canvas.create_text(1150, 250, text="Non-vage", font=("Algerian", 30, 'bold'), fill="black")
        self.btn_buttom = Button(self.root, text="Finish", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="white",
                                 command=self.burger_top).place(x=800, y=550)
        self.btn_tomato = Button(self.root, text="Tomato:No", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                 command=self.burger_tomato)
        self.btn_tomato.place(x=800, y=330)

        self.btn_pickle = Button(self.root, text="Pickle:No", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                 command=self.burger_pickel)
        self.btn_pickle.place(x=800, y=390)
        self.btn_chees = Button(self.root, text="Cheese:No", image=self.btn_img_small,
                                compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                command=self.burger_chees)
        self.btn_chees.place(x=800, y=450)
        self.btn_chicken = Button(self.root, text="Chicken:No", image=self.btn_img_small,
                                  compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                  command=self.burger_chicken)
        self.btn_chicken.place(x=1050, y=450)
        self.btn_fish = Button(self.root, text="Fish:No", image=self.btn_img_small,
                                  compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                  command=self.burger_fish)
        self.btn_fish.place(x=1050, y=390)
        self.btn_spinach = Button(self.root, text="Spinach:No", image=self.btn_img_small,
                               compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                               command=self.burger_spinach)
        self.btn_spinach.place(x=800, y=270)
        self.btn_reset = Button(self.root, text="Reset", image=self.btn_img_small,
                                compound=CENTER, command=self.reset,font=("Algerian", 20, 'bold'), fg="white").place(x=1050, y=550)
        self.btn_buttom = Button(self.root, text="Finish", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="white",
                                 command=self.burger_top)
        self.btn_buttom.place(x=800, y=550)
        for i in range(1, 7):
            self.login1 = ImageTk.PhotoImage(Image.open(f'bunbutton_img/{i}.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login1, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()

    def burger_top(self):
        for i in range(1, 7):
            self.login = ImageTk.PhotoImage(Image.open(f'buntop_img/{i}.png'))
            self.my_canvas.create_image(self.b,self.a-50, image=self.login, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()

    def burger_tomato(self):
        if self.btn_tomato.cget('text') == 'Tomato:No':
            self.a = self.a - 50
            self.pos_to=self.a
            self.btn_tomato.config(text="Tomato:Yes", bg="black",fg="green")
            self.count=self.count+1
            self.count_to=self.count
            print("to"+str(self.count))
            print("to" + str(self.count_to))
            for i in range(1, 7):
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/{i}.png'))
                self.my_canvas.create_image(self.b, self.a, image=self.login2, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            print("to" + str(self.count))
            print("to" + str(self.count_to))
            print("pi" + str(self.count))
            print("pi" + str(self.count_pi))
            if self.count_to <= self.count_pi:
                self.count_pi=self.count_pi-1
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_to < self.count_ch:
                self.count_ch=self.count_ch-1
                print(self.a)
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")

            if self.count_to < self.count_ce:
                self.count_ce = self.count_ce - 1
                print("ce")
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")
            if self.count_to < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'))
                self.my_canvas.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_to < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50
            self.count = self.count - 1
            self.count_to = 0
            print("tor" + str(self.count))
            print("tor" + str(self.count_to))
            self.btn_tomato.config(text="Tomato:No", bg="black",fg="red4")
            self.login2 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login2, anchor="nw")

    def burger_pickel(self):
        if self.btn_pickle.cget('text') == 'Pickle:No':
            self.a = self.a - 50
            self.pos_pi = self.a
            self.btn_pickle.config(text="Pickle:Yes", bg="black",fg="green")
            self.count=self.count+1
            self.count_pi = self.count
            print("pi" + str(self.count))
            print("pi" + str(self.count_pi))
            for i in range(1, 7):
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/{i}.png'))
                self.my_canvas.create_image(self.b, self.a, image=self.login3, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            if self.count_pi <= self.count_to:
                self.count_to = self.count_to - 1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_pi, image=self.login2, anchor="nw")
            if self.count_pi < self.count_ch:
                self.count_ch = self.count_ch - 1
                print(self.a)
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")

            if self.count_pi < self.count_ce:
                self.count_ce = self.count_ce - 1
                print("ce")
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")
            if self.count_pi < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'))
                self.my_canvas.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_pi < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")


            self.a = self.a +50
            self.count = self.count - 1
            self.count_pi = 0
            print("tor" + str(self.count))
            print("tor" + str(self.count_to))
            self.btn_pickle.config(text="Pickle:No", bg="black",fg="red4")
            self.login3 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login3, anchor="nw")



    def burger_chees(self):
        if self.btn_chees.cget('text') == 'Cheese:No':
            self.a = self.a - 50
            self.pos_ce = self.a
            self.btn_chees.config(text="Cheese:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_ce = self.count
            print("ce" + str(self.count))
            print("ce" + str(self.count_ce))
            for i in range(1, 7):
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/{i}.png'))
                self.my_canvas.create_image(self.b, self.a, image=self.login4, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            if self.count_ce <= self.count_to:
                self.count_to = self.count_to - 1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_ce < self.count_ch:
                self.count_ch = self.count_ch - 1
                print(self.a)
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")

            if self.count_ce < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_ce < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'))
                self.my_canvas.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_ce < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50
            self.count = self.count - 1
            self.count_ce = 0
            self.btn_chees.config(text="Cheese:No", bg="black",fg="red4")
            self.login4 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login4, anchor="nw")


    def burger_chicken(self):
        if self.btn_chicken.cget('text') == 'Chicken:No':
            self.a = self.a - 50
            self.pos_ch = self.a
            self.btn_chicken.config(text="Chicken:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_ch = self.count
            for i in range(1, 7):
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/{i}.png'))
                self.my_canvas.create_image(self.b, self.a, image=self.login5, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            if self.count_ch <= self.count_to:
                self.count_to=self.count_to-1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_ch < self.count_ce:
                self.count_ce=self.count_ce-1
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")

            if self.count_ch < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_ch < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'))
                self.my_canvas.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_ch < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50

            self.count = self.count - 1
            self.count_ch = 0
            self.btn_chicken.config(text="Chicken:No", bg="black",fg="red4")
            self.login5 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login5, anchor="nw")

    def burger_fish(self):
        if self.btn_fish.cget('text') == 'Fish:No':
            self.a = self.a - 50
            self.pos_fi = self.a
            self.btn_fish.config(text="Fish:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_fi = self.count
            for i in range(1, 7):
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/{i}.png'))
                self.my_canvas.create_image(self.b, self.a, image=self.login6, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            if self.count_fi <= self.count_ch:
                self.count_ch=self.count_ch-1
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")
            if self.count_fi <= self.count_to:
                self.count_to=self.count_to-1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_fi < self.count_ce:
                self.count_ce=self.count_ce-1
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")

            if self.count_fi < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_fi < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50

            self.count = self.count - 1
            self.count_fi = 0
            self.btn_fish.config(text="Fish:No", bg="black",fg="red4")
            self.login6 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login6, anchor="nw")

    def burger_spinach(self):
        if self.btn_spinach.cget('text') == 'Spinach:No':
            self.a = self.a - 50
            self.pos_sp = self.a
            self.btn_spinach.config(text="Spinach:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_sp = self.count
            for i in range(1, 7):
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/{i}.png'))
                self.my_canvas.create_image(self.b, self.a, image=self.login7, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            if self.count_sp <= self.count_ch:
                self.count_ch=self.count_ch-1
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")
            if self.count_sp <= self.count_to:
                self.count_to=self.count_to-1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_sp < self.count_ce:
                self.count_ce=self.count_ce-1
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")

            if self.count_sp < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'))
                self.my_canvas.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_sp < self.count_fi:
                self.count_fi = self.count_fi - 1

                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'))
                self.my_canvas.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")


            self.a = self.a +50

            self.count = self.count - 1
            self.count_sp = 0
            self.btn_spinach.config(text="Spinach:No", bg="black",fg="red4")
            self.login7 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas.create_image(self.b, self.a, image=self.login7, anchor="nw")


CustomBurger()
