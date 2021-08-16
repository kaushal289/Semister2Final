from tkinter import *
from PIL import ImageTk, Image


class MainPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main")
        self.root.state('zoomed')
        self.my_canvas = Canvas(self.root)
        self.my_canvas.pack(fill="both", expand=True)
        self.background = ImageTk.PhotoImage(Image.open('background.png'))
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")

        self.ace_images()
        self.buttons()

        self.menu_main_frame()




        self.root.mainloop()
    def ace_images(self):
        # now set an image for moving
        self.img1 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace.png"))  # make sure that you have a photo
        # in you current folder that you are working with
        self.img2 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace1.png"))
        self.img3 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace2.png"))
        self.img4 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace3.png"))
        # Create a label
        self.l = Label(self.root, font="bold")
        self.l.place(x=20, y=0)
        # take a variable
        self.x = 1
        self.ace_move()


    def ace_move(self):
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
        self.root.after(500, self.ace_move)



    def buttons(self):
        self.menu_img = ImageTk.PhotoImage(Image.open('menu.png'))
        self.menu_change_img = ImageTk.PhotoImage(Image.open('menu_change.png'))
        self.details_img= ImageTk.PhotoImage(Image.open('details.png'))
        self.details_change_img = ImageTk.PhotoImage(Image.open('details_change.png'))
        self.about_img = ImageTk.PhotoImage(Image.open('information.png'))
        self.about_change_img = ImageTk.PhotoImage(Image.open('information_change.png'))
        self.profile_img = ImageTk.PhotoImage(Image.open('profile.png'))
        self.profile_change_img = ImageTk.PhotoImage(Image.open('profile_change.png'))
        self.setting_img = ImageTk.PhotoImage(Image.open('setting.png'))
        self.setting_change_img = ImageTk.PhotoImage(Image.open('setting_change.png'))


        self.menu_btn= Button(self.root, text="      MENU", fg="white",image=self.menu_change_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.menu_main_frame)
        self.menu_btn.place(x=30,y=150)
        self.details_btn = Button(self.root, text="   DETAILS", fg="white", image=self.details_img,
                               font=("Rockwell nova", 20, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER, command=self.fn_details)
        self.details_btn.place(x=30, y=250)


        self.about_btn = Button(self.root, text="ABOUT US", fg="white", image=self.about_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_about())
        self.about_btn.place(x=30, y=350)

        self.profile_btn = Button(self.root, text="PROFILE", fg="white", image=self.profile_img,
                                  font=("Rockwell nova", 20,'bold'),
                                  cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_profile())
        self.profile_btn.place(x=30, y=450)

        self.setting_btn = Button(self.root, text="   SETTING", fg="white", image=self.setting_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_setting())
        self.setting_btn.place(x=30, y=550)


    def menu_main_frame(self):
        self.a = 0

        self.frame_main = LabelFrame(self.root, height=550, width=1040, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)
        self.frame_room = LabelFrame(self.frame_main, height=530, width=340, borderwidth=10)
        self.frame_room.place(x=0, y=0)
        self.frame_food = LabelFrame(self.frame_main, height=530, width=340, borderwidth=10)
        self.frame_food.place(x=340, y=0)
        self.frame_cab = LabelFrame(self.frame_main, height=530, width=340, borderwidth=10)
        self.frame_cab.place(x=680, y=0)


        self.img11 = ImageTk.PhotoImage(Image.open(f"room/room1.png"))

        self.image_close = Label(self.frame_room, image=self.img11)
        self.image_close.place(x=70, y=280)

        self.img22 = ImageTk.PhotoImage(Image.open(f"room/room2.png"))
        self.img33 = ImageTk.PhotoImage(Image.open(f"room/room3.png"))
        self.img44 = ImageTk.PhotoImage(Image.open(f"room/room4.png"))

        self.l_room = Label(self.frame_room, font="bold")
        self.l_room.place(x=70, y=280)
        self.topic_room = Label(self.frame_room, text='ROOM', font=("Algerian", 40, 'bold'))
        self.topic_room.place(x=90, y=5)




        self.imgf1 = ImageTk.PhotoImage(Image.open(f"food/food.png"))
        self.imgf2 = ImageTk.PhotoImage(Image.open(f"food/food1.png"))
        self.imgf3 = ImageTk.PhotoImage(Image.open(f"food/food2.png"))
        self.imgf4 = ImageTk.PhotoImage(Image.open(f"food/food3.png"))
        self.imgf5 = ImageTk.PhotoImage(Image.open(f"food/food4.png"))




        self.l_food = Label(self.frame_food, font="bold")
        self.l_food.place(x=0, y=50)
        self.x2=1
        self.x1 = 1

        self.frame_room.bind("<Enter>", self.change)
        print(self.a)
        if self.a == 0:
            self.l_food.place_forget()


    def change(self,e):
        self.a=1

        self.room_move()

    def room_move(self):
        if self.x1 == 0:
            self.x1 = 1
        if self.x1 == 1:
            self.l_room.config(image=self.img11)
            self.menu_btn.config(image=self.menu_change_img, fg='green')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')


        elif self.x1 == 2:
            self.l_room.config(image=self.img22)
        elif self.x1 == 3:
            self.l_room.config(image=self.img33)
        elif self.x1 == 4:
            self.l_room.config(image=self.img44)

        # you can do it for thousands of images
        # now increase the count by one
        self.x1 += 1
        # set images to work automatically by "after" feature in tkinter
        self.root.after(500, self.room_move)
    def food_move(self):
        if self.x2 == 0:
            self.x2 = 1
        if self.x2 == 1:
            self.l_food.config(image=self.imgf1)
            self.menu_btn.config(image=self.menu_change_img, fg='green')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')

        elif self.x2 == 2:
            self.l_food.config(image=self.imgf2)
        elif self.x2 == 3:
            self.l_food.config(image=self.imgf3)
        elif self.x2 == 4:
            self.l_food.config(image=self.imgf4)
        elif self.x2 == 5:
            self.l_food.config(image=self.imgf5)


        # you can do it for thousands of images
        # now increase the count by one
        self.x2 += 1
        # set images to work automatically by "after" feature in tkinter
        self.root.after(500, self.food_move)



    def fn_details(self):
        self.frame_details = LabelFrame(self.root, height=550, width=1050, borderwidth=10)
        self.frame_details.place(x=300, y=130)
        self.topic=Label(self.frame_details,text='DETAILS',font=("Rockwell nova", 30,'bold'))
        self.topic.place(x=420,y=30)
        self.frame_main.pack_propagate(False)
        self.name_fn='details'
        self.frame_main.place_forget()

        self.img_change()
    def fn_about(self):
        self.frame_about = LabelFrame(self.root, height=550, width=1050, borderwidth=10)
        self.frame_about.place(x=300, y=130)
        self.topic = Label(self.frame_about, text='ABOUT US', font=("Rockwell nova", 30, 'bold'))
        self.topic.place(x=420, y=30)
        self.name_fn='about'

        self.img_change()
    def fn_profile(self):
        self.frame_profile = LabelFrame(self.root, height=550, width=1050, borderwidth=10)
        self.frame_profile.place(x=300, y=130)
        self.topic = Label(self.frame_profile, text='YOUR PROFILE', font=("Rockwell nova", 30, 'bold'))
        self.topic.place(x=420, y=30)
        self.name_fn='profile'
        self.img_change()
    def fn_setting(self):
        self.frame_setting = LabelFrame(self.root, height=550, width=1050, borderwidth=10)
        self.frame_setting.place(x=300, y=130)
        self.topic = Label(self.frame_setting, text='SETTING', font=("Rockwell nova", 30, 'bold'))
        self.topic.place(x=420, y=30)
        self.name_fn = 'setting'
        self.img_change()

    def img_change(self):
        if self.name_fn=='menu':
            self.menu_btn.config(image=self.menu_change_img, fg='green')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')




        elif self.name_fn=='details':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_change_img,fg='green')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')



        elif self.name_fn=='about':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img,fg='white')
            self.about_btn.config(image=self.about_change_img, fg='green')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')

            self.frame_main.place_forget()
        elif self.name_fn=='profile':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img,fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_change_img, fg='green')
            self.setting_btn.config(image=self.setting_img, fg='white')

            self.frame_main.place_forget()
        else:
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_change_img, fg='green')

            self.frame_main.place_forget()

MainPage()