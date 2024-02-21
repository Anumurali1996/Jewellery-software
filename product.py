from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import Image,ImageTk,ImageFilter
import mysql.connector 
import random

class product_det:
    def __init__(self,root) :
        self.root=root
        self.root.title("Product Detail")
        self.root.geometry("1255x550+230+220")
        self.root.resizable(False,False)

        #============ variables ========
        self.var_productid=StringVar()
        # x=random.randint(1,10000)
        # self.var_productid.set(str(x))

        self.var_name=StringVar()
        self.var_rate=StringVar()
        self.var_weight=StringVar()
        self.var_type=StringVar()
        self.var_quantity=StringVar()


        # =========title========

        p1_title=Label(self.root,text="Product Detail",font=("time new roman",18,"bold"),bg="goldenrod",fg="black",bd=4)
        p1_title.place(x=0,y=0,width=1295,height=50)


        #===========logo==========

        # img=Image.open(r"/home/more/Desktop/jewell/images/jewel.jpg")
        # img=img.resize((100,40),ImageFilter.ANTIALIAS)


        # self.photoimg=ImageTk.photoimg(img)

        # p1img=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        # p1img.place(x=5,y=2,width=100,height=40)


        #========= label frame========

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ADD PRODUCT DETAILS",font=("time new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #============== labels and entries======

        #prdct id

        pid = Label(labelframeleft,font=("arial",12,"bold"),text="Product Id",padx=2,pady=6)
        pid.grid(row=0,column=0,sticky=W)
        txtpid=ttk.Entry(labelframeleft,textvariable=self.var_productid,font=("arial",12,"bold"),width=29)
        txtpid.grid(row=0,column=1)

        #prdct name

        pname = Label(labelframeleft,font=("arial",12,"bold"),text="Product Name",padx=2,pady=6)
        pname.grid(row=1,column=0,sticky=W)
        txtpname=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("arial",12,"bold"),width=29)
        txtpname.grid(row=1,column=1)
        

        #weight

        pweight= Label(labelframeleft,font=("arial",12,"bold"),text="Product Weight",padx=2,pady=6)
        pweight.grid(row=2,column=0,sticky=W)
        txtpweight=ttk.Entry(labelframeleft,textvariable=self.var_weight,font=("arial",12,"bold"),width=29)
        txtpweight.grid(row=2,column=1)
        

        #Rate

        prate= Label(labelframeleft,font=("arial",12,"bold"),text="Product Rate",padx=2,pady=6)
        prate.grid(row=3,column=0,sticky=W)
        txtprate=ttk.Entry(labelframeleft,textvariable=self.var_rate,font=("arial",12,"bold"),width=29)
        txtprate.grid(row=3,column=1)

        # jewwllery type

        ptype= Label(labelframeleft,font=("arial",12,"bold"),text="Jewellery Type",padx=2,pady=6)
        ptype.grid(row=4,column=0,sticky=W)
        combo_ptype=ttk.Combobox(labelframeleft,textvariable=self.var_type,font=("arial",12,"bold"),width=28)
        combo_ptype["value"]=("Bangles","Ring","jumukas","Necklace")
        combo_ptype.current(0)
        combo_ptype.grid(row=4,column=1)


        #number of products

        pnum= Label(labelframeleft,font=("arial",12,"bold"),text="Number of Iteam",padx=2,pady=6)
        pnum.grid(row=5,column=0,sticky=W)
        txtpnum=ttk.Entry(labelframeleft,textvariable=self.var_quantity,font=("arial",12,"bold"),width=29)
        txtpnum.grid(row=5,column=1)

        #========== btns ========

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=338,width=412,height=40)


        btn_add = Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_add.grid(row=0,column=0)

        btn_update = Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_update.grid(row=0,column=1)

        btn_delete = Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_delete.grid(row=0,column=2)

        btn_reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        btn_reset.grid(row=0,column=3)


        #==========detail page========

        detail_page=LabelFrame(self.root,bd=2,relief=RIDGE,text="PRODUCT DETAILS & SEARCH",font=("time new roman",12,"bold"),padx=2)
        detail_page.place(x=435,y=50,width=860,height=490)

        combo_search=ttk.Combobox(detail_page,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("Bangles","Ring","jumukas","Necklace")
        combo_search.current(0)
        combo_search.grid(row=1,column=1)

        #======btn frame ====

        btnsearch=ttk.Entry(detail_page,font=("arial",12,"bold"),width=29)
        btnsearch.grid(row=1,column=2,padx=1)

        btn_add = Button(btnsearch,text="Search",font=("arial",11,"bold"),bg="black",fg="goldenrod",width=7)
        btn_add.grid(row=0,column=0,padx=2)

        btn_add = Button(btnsearch,text="Show all",font=("arial",11,"bold"),bg="black",fg="goldenrod",width=7)
        btn_add.grid(row=0,column=3)


        #======= show data table =======

        detail_table=Frame(detail_page,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(detail_table,orient=HORIZONTAL)

        self.product_det_table=ttk.Treeview(detail_table,columns=("id","name","rate","weight","type","quantity"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.product_det_table.xview)
        Scroll_y.config(command=self.product_det_table.yview)
        
        self.product_det_table.heading("id", text="Product Id")
        self.product_det_table.heading("name", text="Product Name")
        self.product_det_table.heading("rate", text="Product Rate")
        self.product_det_table.heading("weight", text="Product Weight")
        self.product_det_table.heading("type", text="Type of Product")
        self.product_det_table.heading("quantity", text="Quantity")


        self.product_det_table["show"]="headings"
        
        self.product_det_table.column("id", width=130 )
        self.product_det_table.column("name", width=130)
        self.product_det_table.column("rate", width=130)
        self.product_det_table.column("weight", width=130)
        self.product_det_table.column("type", width=130)
        self.product_det_table.column("quantity", width=130)

        self.product_det_table.pack(fill=BOTH,expand=1)
        self.product_det_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    

    def add_data(self):
        if self.var_name.get()=="" or self.var_quantity.get()=="":
           messagebox.showerror("error","All fields are requaired",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anu@17151431",database="jewellery")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into product Values(%s,%s,%s,%s,%s,%s)",(
                                                                       self.var_productid.get(),
                                                                        self.var_name.get(),
                                                                        self.var_rate.get(),
                                                                        self.var_weight.get(),
                                                                        self.var_type.get(),
                                                                        self.var_quantity.get()
                                                                                                                                                   
                                                                    ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("success","products has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from product")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.product_det_table.delete(*self.product_det_table.get_children())
            for i in rows:
                self.product_det_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.product_det_table.focus()
        content=self.product_det_table.item(cursor_row)
        row=content["values"]
        
        self.var_productid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_rate.set(row[2]),
        self.var_weight.set(row[3]),
        self.var_type.set(row[4]),
        self.var_quantity.set(row[5])

    def update(self):
        if self.var_quantity.get()=="":
            messagebox.showerror("Error","please enter number of item",parent=self.root)

        else:
           conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
           my_cursor=conn.cursor()
           my_cursor.execute("update product set name=%s,rate=%s,weight=%s,type=%s,quantity=%s where productid=%s",(
                                                                                                               self.var_name.get(),
                                                                                                               self.var_rate.get() ,
                                                                                                               self.var_weight.get(),
                                                                                                               self.var_type.get(),
                                                                                                               self.var_quantity.get(),
                                                                                                               self.var_productid.get()
                                                                                                               
                                                                                                               
                                                                                                            ))


           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("update"," product details are updated successfully",parent=self.root)     


    def delete(self):
        delete=messagebox.askyesno("Jewellery managemnt system","do you want to delete this product details", parent=self.root)
        
        if delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Anu@17151431',database='jewellery')
            my_cursor=conn.cursor()
            query="delete from product where productid=%s"
            value=(self.var_productid.get(),)
            my_cursor.execute(query,value)

        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_productid.set(""),
        self.var_name.set(""),
        self.var_rate.set(""),
        self.var_type.set(""),
        self.var_weight.set(""),
        self.var_quantity.set("")


      



if __name__== "__main__":
    root =Tk()
    obj=product_det(root)
    root.mainloop()