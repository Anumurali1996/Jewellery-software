from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from PIL import ImageTk
import settings
import tkinter as tk

class Employee_management:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Management")
        self.root.geometry("1500x800+0+0")
        # self.root.resizable(False,False)

        # ===========background image===============================
        self.bg3=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\bg3.jpg")
        label_bg3=Label(self.root,image=self.bg3)
        label_bg3.place(x=0,y=0,relwidth=1,relheight=1)

        # =================connect to mysql database=================
        self.conn=mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="Anu@17151431",
                                            database="jewellery"
        )
        self.cursor=self.conn.cursor()

        # ==============variables to store employee data==============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sec_q=StringVar()
        self.var_sec_a=StringVar()
        self.var_username=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()

        # =================frame=================
        frame=Frame(self.root,bg="gold")
        frame.place(x=0,y=0,width=1500,height=1500)

        # =============regiser label=============
        register_label=Label(frame,text="REGISTER EMPLOYEE HERE..",font=("times new roman",20,"bold"),fg="black",bg="goldenrod")
        register_label.place(x=20,y=20)

        # ==============label and entry=========
        fname_label=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        fname_label.place(x=20, y=50)

        fnametxt=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fnametxt.place(x=20,y=80,width=250)

        lname_label=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        lname_label.place(x=20, y=110)

        lnametxt=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lnametxt.place(x=20,y=140,width=250)

        email_label=Label(frame,text="Email ID",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        email_label.place(x=20, y=170)

        emailtxt=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        emailtxt.place(x=20,y=200,width=250)

        contact_label=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        contact_label.place(x=20, y=230)

        contacttxt=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contacttxt.place(x=20,y=260,width=250)

        security_label=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        security_label.place(x=20, y=290)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_sec_q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your birth place","Your pet name","Your favourite color")
        self.combo_security_q.place(x=20,y=320,width=250)
        self.combo_security_q.current(0)

        security_ans=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        security_ans.place(x=20, y=350)

        secu_anstxt=ttk.Entry(frame,textvariable=self.var_sec_a,font=("times new roman",15,"bold"))
        secu_anstxt.place(x=20,y=380,width=250)

        user_name=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        user_name.place(x=20, y=410)

        usernametxt=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15,"bold"))
        usernametxt.place(x=20,y=440,width=250)


        pass_label=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        pass_label.place(x=20, y=470)

        passtxt=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        passtxt.place(x=20,y=500,width=250)

        confirm_pass_label=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        confirm_pass_label.place(x=20, y=530)

        confirm_passtxt=ttk.Entry(frame,textvariable=self.var_conpass,font=("times new roman",15,"bold"))
        confirm_passtxt.place(x=20,y=560,width=250)

        # ==============add button====================
        self.add_btn=Button(frame,text="Add Employee",command=self.add_emp,font=("times new roman",15,"bold"))
        self.add_btn.place(x=20,y=600)

        bck_button=Button(frame,text="Go back..",command=self.backbuttn,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="goldenrod",bg="black",cursor="hand2",activebackground="goldenrod")
        bck_button.place(x=500,y=500,width=120,height=50)


        # ==============delete button=================
        # self.del_label=Label(frame,text="Delete Employee",font=("times new roman",15,"bold"))
        # self.del_label.place(x=500,y=70)
        # self.user_name_del=Label(frame,text="Employee Username",font=("times new roman",15,"bold"))
        # self.user_name_del.place(x=500,y=120)
        # self.user_name_deltxt=ttk.Entry(frame,textvariable=self.var_username)
        # self.user_name_deltxt.place(x=500,y=180,width=250,height=50)
        # self.btn_del=Button(frame,command=self.del_employee,text="Delete")
        # self.btn_del.place(x=500,y=250,width=120,height=50)


    def add_emp(self):
        # ===============initializing variables================
        fname=self.var_fname.get()
        lname=self.var_lname.get()
        email=self.var_email.get()
        contact=self.var_contact.get()
        securityQ=self.var_sec_q.get()
        securityA=self.var_sec_a.get()
        user_name=self.var_username.get()
        pass_word=self.var_pass.get()

        if fname=="" or user_name=="" and securityQ=="" or securityA=="":
            messagebox.showerror("Invalid","All fields required!")
            return
        try:
            self.cursor.execute("SELECT * FROM empregister WHERE user_name=%s",(user_name,))
            existing_user=self.cursor.fetchone()
            if existing_user:
                         messagebox.showerror("Error","User already exists")
                         return
            else:
                # ===============SQL command to add employee======
                if pass_word==self.var_conpass.get():
                    add_qury="INSERT INTO empregister (fname,lname,email,contact,securityQ,securityA,user_name,pass_word) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    add_det=(fname,lname,email,contact,securityQ,securityA,user_name,pass_word)
                    self.cursor.execute(add_qury,add_det)
                    self.conn.commit()

                    messagebox.showinfo("Success","Employee Added Successfully")
                else:
                     messagebox.showerror("Error","Password and Confirm Password must match!")

        except mysql.connector.Error as e:
                messagebox.showerror("Error",f"Database error:{e}")

 #    def del_employee(self):
 #         username=self.var_username.get()
 #
 #         del_employee=messagebox.askyesno("Employee management","Do you want to delete this employee details?")
 #         if del_employee>0:
 # #  ===========sql command to delete an employee========
 #              delet_qury="DELETE FROM empregister WHERE user_name=%s"
 #              self.cursor.execute(delet_qury,(username,))
 #              self.conn.commit()
 #
 #              messagebox.showinfo("Success","Employee deleted successfully")
 #
 #         else :
 #
 #            messagebox.showerror("Error", f"Database error")
   
                
    def backbuttn(self):

     
        self.new_window=Toplevel(self.root)

        self.bck=settings.officemanagement(self.new_window)





if __name__ == "__main__":
    root = Tk()
    obj = Employee_management(root)
    root.mainloop()
