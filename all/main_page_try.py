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
        self.images('ace_logo','ace','ace1','ace2','ace3',10,10)
        self.images('room','room1', 'room2', 'room3', 'room4', 200, 10)
        self.buttons()
        self.menu_main_frame()
        self.root.mainloop()
    def images(self,file_name,img1,img2,img3,img4,x,y):
        # now set an image for moving
        self.img1 = ImageTk.PhotoImage(Image.open(f"{file_name}/{img1}.png"))  # make sure that you have a photo
        # in you current folder that you are working with
        self.img2 = ImageTk.PhotoImage(Image.open(f"{file_name}/{img2}.png"))
        self.img3 = ImageTk.PhotoImage(Image.open(f"{file_name}/{img3}.png"))
        self.img4 = ImageTk.PhotoImage(Image.open(f"{file_name}/{img4}.png"))
        # Create a label
        self.l = Label(self.root, font="bold")
        self.l.place(x=x, y=y)
        # take a variable
        self.x = 1
        self.move()

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
        self.root.after(2000, self.move)
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
        self.name_fn='menu'
        self.frame_main = LabelFrame(self.root, height=550, width=1050, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)
        self.menu_sub_frame(0, 0, 0)
        self.inside_menu_sub_frame(0)
        self.menu_sub_frame(345, 0, 1)
        self.inside_menu_sub_frame(1)
        self.menu_sub_frame(690, 0, 2)
        self.inside_menu_sub_frame(2)
        self.img_change()

    def menu_sub_frame(self,x,y,num):
        self.frame=['self.frame1','self.frame2','self.frame3']
        self.frame[num] = LabelFrame(self.frame_main, height=530, width=340,borderwidth=10)
        self.frame[num].place(x=x,y=y)
        self.frame[num].pack_propagate(False)
    def inside_menu_sub_frame(self,num):
        self.my_canvas1 = Canvas(self.frame[num])
        self.my_canvas1.pack(fill="both", expand=True)
        if num==0:
            self.my_canvas1.create_text(150,30,text='ROOM',font=("Algerian", 40,'bold'))
        elif num==1:
            self.my_canvas1.create_text(150, 30, text='FOOD',font=("Algerian", 40,'bold'))
        else:
            self.my_canvas1.create_text(150, 30, text='PICK UP',font=("Algerian", 40,'bold'))
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
        elif self.name_fn=='profile':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img,fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_change_img, fg='green')
            self.setting_btn.config(image=self.setting_img, fg='white')
        else:
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_change_img, fg='green')

MainPage()