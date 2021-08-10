from tkinter import *
from PIL import ImageTk, Image

class Registration:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.state('zoomed')
        self.my_canvas = Canvas(self.root)
        self.my_canvas.pack(fill="both", expand=True)
        self.background = PhotoImage(file='registration.png')
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")
        self.fn_frame()
        self.root.mainloop()
    def fn_frame(self):
        self.frame= LabelFrame(self.root, height=500, width=300, borderwidth=10,bg='purple')
        self.frame.place(x=300, y=130)
        self.frame.pack_propagate(False)
        self.buttons()

    def buttons(self):
        register_name = Label(self.frame, text="Registration", font=('Times New Roman', 20, "bold"), bg="white")
        register_name.place(x=0, y=140)
        offer = Label(self.frame, text="(Register and get exciting offer)", font=('Times New Roman', 12), bg="white")
        offer.place(x=625, y=175)

        user_name_label = Label(self.frame, text="User Name", font=('Times New Roman', 13), bg="white")
        user_name_label.place(x=600, y=198)

        gender_label = Label(self.frame, text="Gender", font=('Times New Roman', 13), bg="white")
        gender_label.place(x=600, y=228)

        district_label = Label(self.frame, text="District", font=('Times New Roman', 13), bg="white")
        district_label.place(x=600, y=258)

        address_label = Label(self.frame, text="Address", font=('Times New Roman', 13), bg="white")
        address_label.place(x=600, y=288)

        email_label = Label(self.frame, text="Email", font=('Times New Roman', 13), bg="white")
        email_label.place(x=600, y=318)

        password_label = Label(self.frame, text="Set password", font=('Times New Roman', 13), bg="white")
        password_label.place(x=600, y=348)

        # create text box

        user_name = Entry(self.frame, text="", width=16, font=('Times New Roman', 13))
        user_name.place(x=695, y=198)

        var = StringVar()
        var.set("4")
        radio1 = Radiobutton(self.frame, text="Male", variable=var, value="1", bg="white").place(x=670, y=228)
        radio2 = Radiobutton(self.frame, text="Female", variable=var, value="2", bg="white").place(x=725, y=228)
        radio3 = Radiobutton(self.frame, text="Other", variable=var, value="3", bg="white").place(x=790, y=228)

        district_list = ['Kathmandu', 'Pokhara', 'Biratnagar', 'Kavre', 'Dhankuta', 'other']
        car = StringVar()
        car.set('Select District')
        droplist = OptionMenu(self.frame, car, *district_list)
        droplist.config(width=15, bg="white", font=('Times New Roman', 11), borderwidth=0)

        droplist.place(x=695, y=258)

        address = Entry(self.frame, width=16, font=('Times New Roman', 13))
        address.place(x=695, y=288)

        email = Entry(self.frame, width=16, font=('Times New Roman', 13))
        email.place(x=695, y=318)

        password = Entry(self.frame, width=16, font=('Times New Roman', 13), show="*")
        password.place(x=695, y=348)

        var123 = StringVar()
        agreement = Checkbutton(self.frame, text="I agree the terms and conditions.", font=('Times New Roman', 12, "bold"),
                                variable=var123, onvalue="on", offvalue="off", bg="white")
        agreement.deselect()
        agreement.place(x=600, y=370)
        # create submit button

        submit_btn = Button(self.frame, text="Register", bg="white", font=('Times New Roman', 15, "bold"),
                     compound=CENTER, borderwidth=0)
        submit_btn.place(x=660, y=395)
Registration()