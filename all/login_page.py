from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image

class Login:
    def __init__(self):
        self.root = Tk()
        self.tip=Balloon(self.root)
        self.tip.config(bg="red",bd=5)
        self.tip.message.config(font=("times new roman",14),fg="blue")
        self.root.title("Login")
        self.root.state('zoomed')
        self.my_canvas = Canvas(self.root)
        self.my_canvas.pack(fill="both", expand=True)
        self.login1 = ImageTk.PhotoImage(Image.open(f'login.png'))
        self.img=Image.open('user.png')
        self.img=self.img.resize((55,45),Image.ANTIALIAS)
        self.user_img=ImageTk.PhotoImage(self.img)
        self.login_btn_img = PhotoImage(file='in.png')
        self.imgpass = Image.open('padlock.png')
        self.imgpass = self.imgpass.resize((55, 45), Image.ANTIALIAS)
        self.user_pass_img = ImageTk.PhotoImage(self.imgpass)
        self.my_canvas.create_image(0, 0, image=self.login1, anchor="nw")
        self.my_canvas.create_image(610, 345, image=self.user_img, anchor="nw")
        self.my_canvas.create_image(610, 417, image=self.user_pass_img, anchor="nw")
        self.my_canvas.create_rectangle(1070, 600, 600, 90,outline = '#05035b',width=10)
        self.my_canvas.create_line(600, 225, 1070, 225,width=10,fill="#05035b")
        self.my_canvas.create_text(835, 130, text="REGISTER HERE", font=("Algerian", 40, 'bold'), fill="gold")
        self.register_btn = Button(self.root, text="New user registration", bg="green", fg="white",
                                   font=("Rockwell nova", 18),
                                   cursor="hand2",
                                   border='0', overrelief="sunken")
        self.tip.bind_widget(self.register_btn, balloonmsg="If you are a new user \n press here.")
        self.register_btn.place(x=720, y=160)
        self.my_canvas.create_text(850, 270, text="LOGIN HERE", font=("Algerian", 40, 'bold'), fill="gold")
        self.var=IntVar()
        self.var.set(1)
        Radiobutton(self.root, text="USER", font=('times new roman', 16,'bold'),width=5, bg="royalblue2", variable=self.var, value=1).place(x=750,y=300)
        Radiobutton(self.root, text="ADMIN", font=('times new roman', 16,'bold'), bg="royalblue2", variable=self.var,value=2).place(x=850, y=300)

        self.username_entry = Entry(self.root, width=24, font=("Times New roman", 22, "bold"),justify='center', borderwidth=0,
                                    bg="snow3", fg="#05035b")
        self.username_entry.place(x=680, y=355)

        self.password_entry = Entry(self.root, width=24,justify='center', font=("Times New roman", 22, "bold"), borderwidth=0,
                                    bg="snow3", fg="#05035b")
        self.my_canvas.create_window(680, 420, anchor="nw", window=self.password_entry)
        self.forget_btn = Button(self.root, text="Forgot password",bg="red",fg="white",font=("Rockwell nova", 15), cursor="hand2",
                               border='0',overrelief="sunken")
        self.forget_btn.place(x=770, y=480)

        self.tip.bind_widget(self.forget_btn,balloonmsg="If you have forgotten password \n then press here.")
        self.login_btn=Button(self.root,text="",font=("Rockwell nova", 25),image=self.login_btn_img,command=self.radio,cursor="hand2",borderwidth=0)
        self.login_btn.place(x=750,y=530)
        self.rounded_rect(self.my_canvas, 675, 350, 370, 42, 10)
        self.rounded_rect(self.my_canvas, 675, 415, 370, 42, 10)
        self.login_btn.bind("<Enter>",self.change)
        self.login_btn.bind("<Leave>", self.change_back)
        self.username_entry.bind("<FocusIn>",self.on_enter)
        self.username_entry.bind("<FocusOut>", self.on_leave)
        self.username_entry.insert(0,"Enter Username Here")
        self.password_entry.bind("<FocusIn>", self.on_enter1)
        self.password_entry.bind("<FocusOut>", self.on_leave1)
        self.password_entry.insert(0, "Enter Password Here")
        self.root.mainloop()
    def on_enter(self,c):
        if self.username_entry.get() == "Enter Username Here":
            self.username_entry.delete(0,'end')

    def on_leave(self,c):
        if self.username_entry.get()=="":
            self.username_entry.insert(0,"Enter Username Here")
    def on_enter1(self,d):
        if self.password_entry.get() == "Enter Password Here":
            self.password_entry.delete(0,'end')
            self.password_entry.config(show="*")
    def on_leave1(self,d):
        if self.password_entry.get()=="":
            self.password_entry.config(show="")
            self.password_entry.insert(0,"Enter Password Here")


    def change(self,e):
        self.login_btn_img1=PhotoImage(file='out.png')
        self.login_btn.config(image=self.login_btn_img1,borderwidth=0)
        self.login_btn.image=self.login_btn_img1
    def change_back(self,e):
        self.login_btn_img1=PhotoImage(file='in.png')
        self.login_btn.config(image=self.login_btn_img1,borderwidth=0)
        self.login_btn.image=self.login_btn_img1

    def rounded_rect(self, my_canvas, x, y, w, h, c):
        self.my_canvas.create_arc(x, y, x + 2 * c, y + 2 * c, start=90, extent=90, style="arc", width=10)
        self.my_canvas.create_arc(x + w - 2 * c, y + h - 2 * c, x + w, y + h, start=270, extent=90, style="arc",
                                  width=10)
        self.my_canvas.create_arc(x + w - 2 * c, y, x + w, y + 2 * c, start=0, extent=90, style="arc", width=10)
        self.my_canvas.create_arc(x, y + h - 2 * c, x + 2 * c, y + h, start=180, extent=90, style="arc", width=10)
        self.my_canvas.create_line(x + c, y, x + w - c, y, fill="black", width=10)
        self.my_canvas.create_line(x + c, y + h, x + w - c, y + h, fill="black", width=10)
        self.my_canvas.create_line(x, y + c, x, y + h - c, fill="black", width=10)
        self.my_canvas.create_line(x + w, y + c, x + w, y + h - c, fill="black", width=10)
    def radio(self):
        print(self.var.get())
C=Login()