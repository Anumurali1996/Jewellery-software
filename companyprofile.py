from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image,ImageTk,ImageFilter
import mysql.connector
from tkinter import messagebox


class company_det :
    def __init__(self,root) :
        self.root=root
        self.root.title("Company Profile")
        self.root.geometry("1200x550+230+220")
        self.root.resizable(False,False)

        # =================variable================

        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_website=StringVar()
        self.var_address=StringVar()
        




        # =========title========

        p1_title=Label(self.root,text="Company Profile",font=("time new roman",18,"bold"),bg="goldenrod",fg="black",bd=4)
        p1_title.place(x=0,y=0,width=1295,height=50)

        # =================LABEL FRAME=================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ADD COMPANY DETAILS",font=("time new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        # ==================LABEL AND ENTRIES===============
        
        # ============company name==================
        cname = Label(labelframeleft,font=("arial",12,"bold"),text="Company Name",padx=2,pady=6)
        cname.grid(row=0,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("arial",12,"bold"),width=29)
        txtcname.grid(row=0,column=1,pady=2)

        contact = Label(labelframeleft,font=("arial",12,"bold"),text="Contact",padx=2,pady=6)
        contact.grid(row=1,column=0,sticky=W)
        txtcontact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",12,"bold"),width=29)
        txtcontact.grid(row=1,column=1,pady=2)

        email = Label(labelframeleft,font=("arial",12,"bold"),text="Email",padx=2,pady=6)
        email.grid(row=2,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",12,"bold"),width=29)
        txtemail.grid(row=2,column=1)

        website = Label(labelframeleft,font=("arial",12,"bold"),text="Website",padx=2,pady=6)
        website.grid(row=3,column=0,sticky=W)
        txtweb=ttk.Entry(labelframeleft,textvariable=self.var_website,font=("arial",12,"bold"),width=29)
        txtweb.grid(row=3,column=1)

        address = Label(labelframeleft,font=("arial",12,"bold"),text="Address",padx=2,pady=6)
        address.grid(row=4,column=0,sticky=W)
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",12,"bold"),width=29)
        txtadd.grid(row=4,column=1)


         #========== btns ========

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=412,height=40)


        btn_add = Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_add.grid(row=0,column=0)

        btn_update = Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_update.grid(row=0,column=1)

        btn_delete = Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_delete.grid(row=0,column=2)

        btn_reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_reset.grid(row=0,column=3)

        # =========table frame===============
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="COMPANY LIST",font=("time new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

        #======btn frame ====
        

      #   btnsearch=ttk.Entry(Table_frame,font=("arial",12,"bold"),width=29)
      #   btnsearch.grid(row=1,column=2,padx=1)

        # btn_add = Button(btnsearch,text="Search",font=("arial",11,"bold"),bg="black",fg="goldenrod",width=7)
        # btn_add.grid(row=0,column=0,padx=2)

        # btn_add = Button(btnsearch,text="Show all",font=("arial",11,"bold"),bg="black",fg="goldenrod",width=7)
        # btn_add.grid(row=0,column=3)

         #======= show data table =======

        cp_table=Frame(Table_frame,bd=2,relief=RIDGE)
        cp_table.place(x=0,y=50,width=860,height=350)

        scroll_x2=ttk.Scrollbar(cp_table,orient=HORIZONTAL)
        scroll_y2=ttk.Scrollbar(cp_table,orient=VERTICAL)

        self.company_table=ttk.Treeview(cp_table,columns=("name","contact","email","website","address"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)
        

        scroll_x2.config(command=self.company_table.xview)
        scroll_y2.config(command=self.company_table.yview)

        self.company_table.heading("name", text="Company Name")
        self.company_table.heading("contact", text="Contact")
        self.company_table.heading("email", text="Email")
        self.company_table.heading("website", text="Website")
        self.company_table.heading("address", text="Address")


        self.company_table["show"]="headings"
        

        self.company_table.column("name", width=100)
        self.company_table.column("contact", width=100)
        self.company_table.column("email", width=100)
        self.company_table.column("website", width=100)
        self.company_table.column("address", width=100)

        self.company_table.pack(fill=BOTH,expand=1)

        self.company_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

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
                self.my_cursor=self.conn.cursor()

                # ===========create table============
                create_table_cmpny="""
                                        CREATE TABLE IF NOT EXISTS company (
                                            name VARCHAR(255)NOT NULL PRIMARY KEY,
                                            contact VARCHAR(255) NOT NULL,
                                            email VARCHAR(255) NOT NULL,
                                            website VARCHAR(255) NOT NULL,
                                            address VARCHAR(255) NOT NULL
                                            
                                        )"""
                self.my_cursor.execute(create_table_cmpny)
                self.conn.commit()

            except mysql.connector.Error as e:
                messagebox.showerror("Database initialization error",f"Error: {e}")


    def add_data(self):
        if self.var_contact.get()==""or self.var_name.get()=="":
                messagebox.showerror("error","All fields are required")
        else:
                try:
                        conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into company values(%s,%s,%s,%s,%s)",(
                                                                        self.var_name.get(),
                                                                        self.var_contact.get(),
                                                                        self.var_email.get(),
                                                                        self.var_website.get(),
                                                                        self.var_address.get()                                                                                
                ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("info","Company has been added successfully..",parent=self.root)
                except Exception as es:
                      messagebox.showwarning("warning","something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
          conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
          my_cursor=conn.cursor()
          my_cursor.execute("select * from company")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
                self.company_table.delete(*self.company_table.get_children())
                for i in rows:
                      self.company_table.insert("",END,values=i)
                conn.commit()
                conn.close()
    def get_cursor(self,event=""):
          cursor_row=self.company_table.focus()
          content=self.company_table.item(cursor_row)
          row=content["values"]

          self.var_name.set(row[0]),
          self.var_contact.set(row[1]),
          self.var_email.set(row[2]),
          self.var_website.set(row[3]),
          self.var_address.set(row[4])

    def update(self):
          if self.var_contact.get()=="":
                messagebox.showerror("Error","Please enter contact number",parent=self.root)
          else:
                conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
                my_cursor=conn.cursor()
                my_cursor.execute("update company set contact=%s,email=%s,website=%s,address=%s where name=%s",(
                                                                         
                                                                        self.var_contact.get(),
                                                                        self.var_email.get(),
                                                                        self.var_website.get(),
                                                                        self.var_address.get(),
                                                                        self.var_name.get()
                                                                        
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","company details has been updated successfully",parent=self.root)
    def delete(self):
        delete=messagebox.askyesno("Jewellery managemnt system","do you want to delete this company details", parent=self.root)
        
        if delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
            my_cursor=conn.cursor()
            query="delete from company where name=%s"
            value=(self.var_name.get(),)
            my_cursor.execute(query,value)

        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset_data(self):
      
        self.var_name.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_website.set(""),
        self.var_address.set("")
      
              
                      
                










if __name__== "__main__":
    root =Tk()
    obj=company_det(root)
    root.mainloop()

