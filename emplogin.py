from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import admindash
from admin import Register
from tkinter import messagebox
import mysql.connector
import product
import adminlogin


class emplogin_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # ===============background image=============
        self.bg3=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\bg3.jpg")
        label_bg3=Label(self.root,image=self.bg3)
        label_bg3.place(x=0,y=0,relwidth=1,relheight=1)

        # ====================frame====================
        frame=Frame(self.root,bg="goldenrod")
        frame.place(x=510,y=170,width=340,height=450)

        # =============image icon===========================
        img1=Image.open(r"C:\Users\DELL\Downloads\icon.png")
        img1=img1.resize((50,50))
        self.photoimage1=ImageTk.PhotoImage(img1)
        image_label1=Label(image=self.photoimage1,bg='goldenrod',borderwidth=0)
        image_label1.place(x=656,y=175,width=50,height=50)


        # =================title============================
        get_str=Label(frame,text="Login",font=("times new roman",20,"bold"),fg="black",bg="goldenrod")
        get_str.place(x=130,y=60)

        # ===============label=============================
        username_label=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        username_label.place(x=50,y=100)

        self.txtusername=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtusername.place(x=50,y=130)

        password_label=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        password_label.place(x=50,y=170)

        self.txtpassword=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpassword.place(x=50,y=200)

        # ================login button=====================
        log_btn=Button(frame,text="LOGIN",command=self.login_win,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="goldenrod",bg="black",cursor="hand2",activebackground="goldenrod")
        log_btn.place(x=110,y=280,width=120,height=50)

        adm_btn=Button(frame,text="Login as Admin",command=self.adm_login,font=("times new roman",12,"bold"),borderwidth=0,fg="black",bg="goldenrod",cursor="hand2",activebackground="goldenrod")
        adm_btn.place(x=50,y=350)

        # =================register button===================

        # reg_btn=Button(frame,text="New user?Register here!",command=self.register_page,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="goldenrod",cursor="hand2",activebackground="goldenrod")
        # reg_btn.place(x=50,y=350)

        # ===============forgot button=======================

        for_btn=Button(frame,text="Forgot Password?",command=self.for_pass_win,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="goldenrod",cursor="hand2",activebackground="goldenrod")
        for_btn.place(x=50,y=390)

        # ==============initializing user details============
        # self.username=None
        # self.is_admin=False

    def adm_login(self):
        root.withdraw()
        self.new_window=Toplevel(self.root)

        self.admlog=adminlogin.login_window(self.new_window)

       



    # def register_page(self):
        # self.new_window=Toplevel(self.root)

        # self.register_win=Register(self.new_window)




    def login_win(self):
        # username= self.txtusername.get()
        # password= self.txtpassword.get()

        # try:
        #     conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
        #     my_cursor=conn.cursor()
        #     qury="SELECT * FROM register WHERE username=%s AND password=%s"
        #     my_cursor.execute(qury,(username,password))
        #     row=my_cursor.fetchone()

        #     if row:
        #         self.username = row
        #         if self.username=="admin":
        #             messagebox.showinfo("Login successful","Welcome Admin")
        #             self.new_window=Toplevel(self.root)

        #             self.dash=dash.dashboard(self.new_window)
        #         else:
        #             messagebox.showinfo("Login successful","Welcome Employee")
        #             self.new_window=Toplevel(self.root)

        #             self.product=product.product_det(self.new_window)

        #     else:
        #         messagebox.showerror("invalid","Login Failed")
            
        # except mysql.connector.Error as e:
        #     messagebox.showerror("Database error")

        # finally:
        #     if conn:
        #         # conn.commit()
        #         conn.close()


        if self.txtusername.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All fields trequired")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from empregister where user_name=%s and pass_word=%s",(
                                                                                        self.txtusername.get(),
                                                                                        self.txtpassword.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only for employee")
            
                if open_main>0:

                   root.withdraw()
                
                   self.root2=Toplevel(bg="goldenrod")
                   self.root2.geometry("1500x800+0+0")

                   self.dash=product.product_det(self.root2)

                    # root.login_window.destroy()
                    
                else:
                    if not open_main:
                        return
                    
                conn.commit()
                conn.close()

    # ===============reset password====================
    def reset_password(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security Question ")
        elif self.secu_anstxt.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.newpasstxt.get()=="":
            messagebox.showerror("error","Please enter new password")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
            my_cursor=conn.cursor()
            qury=("select * from empregister where user_name=%s and securityQ=%s and securityA=%s")
            value=(self.txtusername.get(),self.combo_security_q.get(),self.secu_anstxt.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("error","Please enter the valid Answer")
            else:
                query=("update empregister set pass_word=%s where user_name=%s")
                value=(self.newpasstxt.get(),self.txtusername.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("info","Your password has been reset successfully, Please login again")


    # ===============forgot password window=============
    def for_pass_win(self):
        if self.txtusername.get()=="":
            messagebox.showerror("Error","Please enter the username")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
            my_cursor=conn.cursor()
            query=("select * from empregister where user_name=%s")
            value=(self.txtusername.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel(bg="goldenrod")
                self.root2.title("Forgot password")
                self.root2.geometry("340x470+400+150")
                

                lbl=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="goldenrod")
                lbl.place(x=0,y=10,relwidth=1)

                self.security_label=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
                self.security_label.place(x=20, y=80)

                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("Select","Your birth place","Your pet name","Your favourite color")
                self.combo_security_q.place(x=20,y=110,width=250)
                self.combo_security_q.current(0)

                self.security_ans=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
                self.security_ans.place(x=20, y=150)

                self.secu_anstxt=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.secu_anstxt.place(x=20,y=180,width=250)

                self.new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
                self.new_password.place(x=20, y=220)

                self.newpasstxt=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.newpasstxt.place(x=20,y=250,width=250)

                btn_newpass=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="goldenrod",bg="black")
                btn_newpass.place(x=130,y=290)

    

                

if __name__=="__main__":
    root=Tk()
    app=emplogin_window(root)
    root.mainloop()