
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import adminlogin
import admindash




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

         # ==============variablezs====================
        # self.var_fname=StringVar()
        # self.var_lname=StringVar()
        # self.var_contact=StringVar()
        # self.var_email=StringVar()
        self.var_sec_q=StringVar()
        self.var_sec_a=StringVar()
        self.var_username=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        # self.var_role=StringVar()
        # self.is_admin_var=StringVar()

        # =================connect to mysql database=================
        self.conn=mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="Anu@17151431",
                                            database="jewellery"
        )
        self.cursor=self.conn.cursor()

        # ===============background image=============
        self.bg4=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\bg3.jpg")
        label_bg4=Label(self.root,image=self.bg4)
        label_bg4.place(x=0,y=0,relwidth=1,relheight=1)


        # ===============left image=============
        self.bg5=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\bgg.jpeg")
        label_bg5=Label(self.root,image=self.bg5)
        label_bg5.place(x=50,y=100,width=470,height=550)

        # =================frame=================
        frame=Frame(self.root,bg="goldenrod")
        frame.place(x=520,y=100,width=800,height=550)

        # =============regiser label=============
        register_label=Label(frame,text="ADMIN REGISTRATION",font=("times new roman",20,"bold"),fg="black",bg="goldenrod")
        register_label.place(x=20,y=20)

        # ==============label and entry=========
        # fname_label=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        # fname_label.place(x=20, y=70)

        # fnametxt=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        # fnametxt.place(x=20,y=100,width=250)

        # lname_label=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        # lname_label.place(x=370, y=70)

        # lnametxt=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        # lnametxt.place(x=370,y=100,width=250)

        # email_label=Label(frame,text="Email ID",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        # email_label.place(x=20, y=140)

        # emailtxt=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        # emailtxt.place(x=20,y=170,width=250)

        # contact_label=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        # contact_label.place(x=370, y=140)

        # contacttxt=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        # contacttxt.place(x=370,y=170,width=250)

        user_name=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        user_name.place(x=20, y=70)

        usernametxt=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15,"bold"))
        usernametxt.place(x=20,y=100,width=250)

        
        pass_label=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        pass_label.place(x=370, y=70)

        passtxt=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        passtxt.place(x=370,y=100,width=250)

        confirm_pass_label=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        confirm_pass_label.place(x=20, y=140)

        confirm_passtxt=ttk.Entry(frame,textvariable=self.var_conpass,font=("times new roman",15,"bold"))
        confirm_passtxt.place(x=20,y=170,width=250)


        security_label=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        security_label.place(x=370, y=140)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_sec_q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your birth place","Your pet name","Your favourite color")
        self.combo_security_q.place(x=370,y=170,width=250)
        self.combo_security_q.current(0)

        security_ans=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        security_ans.place(x=20, y=210)

        secu_anstxt=ttk.Entry(frame,textvariable=self.var_sec_a,font=("times new roman",15,"bold"))
        secu_anstxt.place(x=20,y=240,width=250)

        

        



        
        # role=Label(frame,text="Role",font=("times new roman",15,"bold"),fg="black",bg="goldenrod")
        # role.place(x=370, y=360)

        # self.combo_role=ttk.Combobox(frame,textvariable=self.var_role,font=("times new roman",15,"bold"),state="readonly")
        # self.combo_role["values"]=("Select","Admin","Employee")
        # self.combo_role.place(x=370,y=400,width=250)
        # self.combo_role.current(0)

        # ==========check button====================
        # self.var_ceck=IntVar()
        # checkbtn=Checkbutton(frame,variable=self.is_admin_var,text="Admin",font=("times new roman",12,"bold"),bg="goldenrod",onvalue=1,offvalue=0)
        # checkbtn.place(x=20,y=430)

        # ============Buttons=======================

        reg_button=Button(frame,text="Register",command=self.rgister_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="goldenrod",bg="black",cursor="hand2",activebackground="goldenrod")
        reg_button.place(x=110,y=350,width=120,height=50)

        bck_button=Button(frame,text="Go back...",command=self.backbuttn,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="goldenrod",bg="black",cursor="hand2",activebackground="goldenrod")
        bck_button.place(x=410,y=350,width=120,height=50)

    def backbuttn(self):
        self.new_window=Toplevel(self.root)

        self.back=admindash.dashboard(self.new_window)

        # ================initializing database connection==============
        self.initialize_database()

    def initialize_database(self):
            try:
                # =========mysql connector===========
                self.conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Anu@17151431",
                    database="jewellery"
                )
                self.cursor=self.conn.cursor()

                # ===========create table============
                create_table_register="""
                                        CREATE TABLE IF NOT EXISTS adminregister(
                                            user_id INT AUTO_INCREMENT PRIMARY KEY,
                                            user_name VARCHAR(255) NOT NULL,
                                            pass_word VARCHAR(255) NOT NULL,
                                            securityQ VARCHAR(255) NOT NULL,
                                            securityA VARCHAR(255) NOT NULL
                                            
                                        )"""
                self.cursor.execute(create_table_register)
                self.conn.commit()

            except mysql.connector.Error as e:
                messagebox.showerror("Database initialization error",f"Error: {e}")

    def rgister_data(self):
                # =========get user input===========
                # fname=self.var_fname.get()
                # lname=self.var_lname.get()
                # email=self.var_email.get()
                # contact=self.var_contact.get()
                securityQ=self.var_sec_q.get()
                securityA=self.var_sec_a.get()
                user_name=self.var_username.get()
                pass_word=self.var_pass.get()
                # role=self.var_role.get()
                # is_admin=self.is_admin_var.get() 

                # ===============validation==============
                # if not user_name or not pass_word and not securityQ or not securityA:
                #     messagebox.showerror("invalid","All fields required!")
                #     return
                # try:
                #     insert_qry="INSERT INTO adminregister (user_name,pass_word,securityQ,securityA) values (%s,%s,%s,%s)" 
                #     data=(user_name,pass_word,securityQ,securityA)
                #     self.cursor.execute(insert_qry,data)
                #     self.conn.commit()

                #     messagebox.showinfo("success","Registration Successfull") 
                #     root.destroy()
                #     self.login_admin()
                # except mysql.connector.Error as e:
                #     messagebox.showerror("Registration Failed",f"Error: {e}")
                if  user_name=="" and securityQ=="" or securityA=="":
                    messagebox.showerror("Invalid","All fields required!")
                    return
                try:
                    self.cursor.execute("SELECT * FROM adminregister WHERE user_name=%s",(user_name,))
                    existing_user=self.cursor.fetchone()
                    if existing_user:
                        messagebox.showerror("Error","User already exists")
                        return
                    else:
                # ===============SQL command to add employee======
                        if pass_word==self.var_conpass.get():
                            add_qury="INSERT INTO adminregister (user_name,pass_word,securityQ,securityA) VALUES (%s,%s,%s,%s)"
                            add_det=(user_name,pass_word,securityQ,securityA)
                            self.cursor.execute(add_qury,add_det)
                            self.conn.commit()

                            messagebox.showinfo("Success","Admin Added Successfully")
                        else:
                            messagebox.showerror("Error","Password and Confirm Password must match!")

                except mysql.connector.Error as e:
                    messagebox.showerror("Error",f"Database error:{e}")
    


    def login_admin(self):
         user_name=self.var_username.get()
         pass_word=self.var_pass.get()

         if not user_name or not pass_word:
              messagebox.showwarning("Warning","All fields required!")
              return
         try:
              self.cursor.execute("SELECT * FROM adminregister WHERE user_name=%s AND pass_word=%s",(user_name,pass_word))
              result=self.cursor.fetchone()

              if result:
                   messagebox.showinfo("Success","Login Successfull")
                   self.new_window=Toplevel(self.root)

                   self.log_in=adminlogin.login_window(self.new_window)
            
              else:
                   messagebox.showerror("Eror","Inavlid username or password")
         except Exception as e:
              messagebox.showerror("Error",f"Login failed: {str(e)}")
        
              
               





if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()    
