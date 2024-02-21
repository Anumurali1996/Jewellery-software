from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from sqlite3 import Row  
import regform   
from PIL import ImageTk  
import settings

class employeees:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Profile")
        self.root.geometry("1500x800+0+0") 
        self.root.resizable(False,False)     

        self.bg4=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\bg3.jpg")
        label_bg4=Label(self.root,image=self.bg4)
        label_bg4.place(x=0,y=0,relwidth=1,relheight=1)
  


        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sec_q=StringVar()
        self.var_sec_a=StringVar()
        self.var_username=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        # self.var_role=StringVar()
        # self.is_admin_var=StringVar()










        tableframe2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Employee Details",font=("time new roman",12,"bold"),padx=2)
        tableframe2.place(x=50,y=50,width=1000,height=490)

        labelsearchby= Label(tableframe2,font=("arial",12,"bold"),text="Search By:",bg="black",fg="goldenrod")
        labelsearchby.grid(row=0,column=0,sticky=W)

        combo_Search=ttk.Combobox(tableframe2,font=("arial",12,"bold"),width=28,state="randomly")
        combo_Search["value"]=("User Id","user_name","fname")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        txtSearch=ttk.Entry(tableframe2,font=("arial",12,"bold"),width=29)
        txtSearch.grid(row=0,column=2)


        

        button_search = Button(tableframe2,text="Search",font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_search.grid(row=0,column=3)

        button_showall = Button(tableframe2,text="Show All",font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_showall.grid(row=0,column=4)


        # btn_add = Button(tableframe2,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        # btn_add.grid(row=0,column=0)

        # btn_update = Button(tableframe2,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        # btn_update.grid(row=5,column=1)

        # btn_delete = Button(self.root,text="Delete",command=self.del_employee,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        # btn_delete.place(x=1100,y=400,width=120,height=50)

        # btn_reset = Button(tableframe2,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        # btn_reset.grid(row=0,column=3)

        bck_button=Button(self.root,text="Go back..",command=self.backbuttn,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="goldenrod",bg="black",cursor="hand2",activebackground="goldenrod")
        bck_button.place(x=1100,y=500,width=120,height=50)

    


        #========================Show Data Table=======================================

        details_table2=Frame(tableframe2,bd=2,relief=RIDGE)
        details_table2.place(x=0,y=50,width=995,height=417)

        scroll_x2=ttk.Scrollbar(details_table2,orient=HORIZONTAL)
        scroll_y2=ttk.Scrollbar(details_table2,orient=VERTICAL)

        self.empdetailstable=ttk.Treeview(details_table2,column=("userid","fname","lname","email","contact","securityq","securitya","user_name"),xscrollcommand=scroll_x2.set)

        
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)

        scroll_x2.config(command=self.empdetailstable.xview)
        scroll_y2.config(command=self.empdetailstable.yview)

        self.empdetailstable.heading("userid",text='User Id')
        self.empdetailstable.heading("fname",text="First Name")
        self.empdetailstable.heading("lname",text="Last Name")
        self.empdetailstable.heading("email",text="Email")
        self.empdetailstable.heading("contact",text="Contact Details")
        self.empdetailstable.heading("securityq",text="Security Qstn")
        self.empdetailstable.heading("securitya",text="Security Ans")
        self.empdetailstable.heading("user_name",text="Username")
        # self.Sale_Details_Table.heading("quantity",text="Quantity")
        # self.Sale_Details_Table.heading("totalamount",text="Total Amount")
        # self.Sale_Details_Table.heading("billview",text="Bill View")
        

        self.empdetailstable["show"]="headings"

        self.empdetailstable.column("userid",width=100)
        self.empdetailstable.column("fname",width=100)
        self.empdetailstable.column("lname",width=100)
        self.empdetailstable.column("email",width=100)
        self.empdetailstable.column("contact",width=100)
        self.empdetailstable.column("securityq",width=100)
        self.empdetailstable.column("securitya",width=100)
        self.empdetailstable.column("user_name",width=100)
        # self.Sale_Details_Table.column("quantity",width=100)
        # self.Sale_Details_Table.column("totalamount",width=100)
        # self.Sale_Details_Table.column("billview",width=100)
        
         
    
        self.empdetailstable.pack(fill=BOTH,expand=1)
        self.empdetailstable.bind("<ButtonRelease-1>"),self.get_cursor
        self.fetch_data()

        # ==============delete button=================
        self.del_label = Label(self.root, text="Delete Employee", font=("times new roman", 15, "bold"))
        self.del_label.place(x=1100, y=70)
        self.user_name_del = Label(self.root, text="Employee Username", font=("times new roman", 15, "bold"))
        self.user_name_del.place(x=1100, y=120)
        self.user_name_deltxt = ttk.Entry(self.root, textvariable=self.var_username)
        self.user_name_deltxt.place(x=1100, y=180, width=250, height=50)
        self.btn_del = Button(self.root, command=self.del_employee, text="Delete")
        self.btn_del.place(x=1100, y=250, width=120, height=50)

    def backbuttn(self):

        

        self.new_window=Toplevel(self.root)

        self.bck=settings.officemanagement(self.new_window)



    def fetch_data(self):
          conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
          my_cursor=conn.cursor()
          my_cursor.execute("select * from empregister")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
                self.empdetailstable.delete(*self.empdetailstable.get_children())
                for i in rows:
                      self.empdetailstable.insert("",END,values=i)
                conn.commit()
                conn.close()
    def get_cursor(self,event=""):
          cursor_row=self.empdetailstable.focus()
          content=self.empdetailstable.item(cursor_row)
          row=content["values"]

          self.var_fname.set(row[0]),
          self.var_lname.set(row[1]),
          self.var_email.set(row[2]),
          self.var_contact.set(row[3]),
          self.var_sec_q.set(row[4]),
          self.var_sec_a.set(row[5]),
          self.var_username.set(row[6])

    def update(self):
          if self.var_contact.get()=="":
                messagebox.showerror("Error","Please enter contact number",parent=self.root)
          else:
                conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
                my_cursor=conn.cursor()
                my_cursor.execute("update empregister set fname=%s,lname=%s,email=%s,contact=%s,securityQ=%s,securityA=%s where user_name=%s",(
                                                                        self.var_fname.get(),
                                                                        self.var_lname.get(),
                                                                        self.var_email.get(),
                                                                        self.var_contact.get(),
                                                                        self.var_sec_q.get(),
                                                                        self.var_sec_a.get(),
                                                                        self.var_username.get()




                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Employee details has been updated successfully",parent=self.root)

    def del_employee(self):
        username = self.var_username.get()

        del_employee = messagebox.askyesno("Employee management", "Do you want to delete this employee details?")
        if del_employee > 0:
            conn = mysql.connector.connect(host='localhost', username='root', password='Anu@17151431',
                                           database='jewellery')
            my_cursor = conn.cursor()
            #  ===========sql command to delete an employee========
            delet_qury = "DELETE FROM empregister WHERE user_name=%s"
            my_cursor.execute(delet_qury, (username,))
            conn.commit()

            messagebox.showinfo("Success", "Employee deleted successfully")

        else:

            messagebox.showerror("Error", f"Database error")

    def reset_data(self):

        self.var_fname.set(""),
        self.var_lname.set(""),
        self.var_email.set(""),
        self.var_contact.set(""),
        self.var_username.set("")














if __name__== "__main__":
    root =Tk()
    obj=employeees(root)
    root.mainloop()