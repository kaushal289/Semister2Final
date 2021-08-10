from PIL import ImageTk, Image
from tkinter import *

class img_change:
    def change(self,e):
        self.login_btn_img1 = PhotoImage(file='out.png')
        self.btn.config(image=self.login_btn_img1, borderwidth=0)
        self.btn.image = self.login_btn_img1
    def change_back(self, e):
        self.login_btn_img1 = PhotoImage(file='in.png')
        self.btn.config(image=self.login_btn_img1, borderwidth=0)
        self.btn.image = self.login_btn_img1
