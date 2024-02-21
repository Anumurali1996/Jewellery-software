from tkinter import *
from PIL import ImageTk, Image
from product import product_det
from companyprofile import company_det
import adminlogin
import settings






class dashboard:
    def __init__(self, root):
        self.root=root
        self.root.title("Jewellery Management System")
        self.root.geometry("1500x800+0+0")

        

# ===================backgroung image1============
        bg1=Image.open(r"C:\Users\DELL\Downloads\bg2.jpg")
        bg1=bg1.resize((1550,140))
        self.bgimage1=ImageTk.PhotoImage(bg1)

        bg1label=Label(self.root,image=self.bgimage1)
        bg1label.place(x=0,y=0,width=1550,height=140)

# ================logo============================
        logo=Image.open(r"C:\Users\DELL\Documents\logo.png")
        logo=logo.resize((150,140))
        self.logoimage=ImageTk.PhotoImage(logo)

        logolabel=Label(self.root,image=self.logoimage)
        logolabel.place(x=0,y=0,width=150,height=140)

# =================title=========================
        labeltitle=Label(self.root,text="JEWELLERY MANAGEMENT",font=("times new roman",40,"bold"),bg="black",fg="goldenrod")
        labeltitle.place(x=0,y=140,width=1550,height=50)


# ==================main frame===================
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg="goldenrod")
        main_frame.place(x=0,y=190,width=1550,height=620)
# ==================dashboard frame==============
        dash_frame=Frame(self.root,bd=2,relief=RIDGE,bg="Gold")
        dash_frame.place(x=230,y=190,width=1200,height=550)





        

# ==================menu=========================
        labelmenu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="goldenrod")
        labelmenu.place(x=0,y=0,width=230)

# ==============button frame====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=230,height=280)

# =============button==============================
        btn1=Button(btn_frame,text="Dashboard", width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn1.grid(row=0,column=0,pady=1)

        btn2=Button(btn_frame,text="Company Profile",command=self.company_profile
                    , width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn2.grid(row=1,column=0,pady=1)

        btn3=Button(btn_frame,text="Product Management",command=self.pro_duct,width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn3.grid(row=2,column=0,pady=1)

        btn4=Button(btn_frame,text="Purchase", width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn4.grid(row=3,column=0,pady=1)        

        # btn5=Button(btn_frame,text="Stock", width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        # btn5.grid(row=4,column=0,pady=1)        

        btn6=Button(btn_frame,text="Sale", width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn6.grid(row=4,column=0,pady=1)    

        btn7=Button(btn_frame,text="Report", width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn7.grid(row=5,column=0,pady=1)    

        btn8=Button(btn_frame,text="Settings",command=self.setting_page, width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn8.grid(row=6,column=0,pady=1)        

        btn9=Button(btn_frame,text="Log Out",command=self.log_out, width=25,font=("times new roman",12,"bold"),bg="black",fg="goldenrod",cursor="hand2")
        btn9.grid(row=7,column=0,pady=1)        

# ==============product page=================
    def pro_duct(self):
        self.new_window=Toplevel(self.root)

        self.prdt=product_det(self.new_window)
        

# ==============company profile page===========
    def company_profile(self):
        self.new_window=Toplevel(self.root)

        self.cprofile=company_det(self.new_window)

       
        # =============log out=================
    def log_out(self):
        self.root3=Toplevel()

        self.logout=adminlogin.login_window(self.root3)

        root.destroy()

        self.open_new()

        
        

    def open_new(self):
        self.new_w=Toplevel()
        
        self.logg=adminlogin.login_window(self.new_w)


        # ===============settings===============

    def setting_page(self):
        self.new_window=Toplevel(self.root)

        self.sett=settings.officemanagement(self.new_window)

        root.withdraw()
        

        




if __name__=="__main__":
    root=Tk()
    obj=dashboard(root)

    root.mainloop()