from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
# Title Frame size

    def __init__(self,root):
        self.root=root
        self.root.title("Student Management system")
        self.root.geometry("1350x700+0+0")

# Main Title With Colour

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        # ====================ALl Variables====================

        self.Roll_No_Var = StringVar()
        self.name_Var = StringVar()
        self.email_Var = StringVar()
        self.gender_Var = StringVar()
        self.contact_Var = StringVar()
        self.dob_Var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

# First Frame For All Details

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=590)

           #================== Student 1st Part================

        m_title=Label(Manage_Frame,text="Manage Student",bg="Crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

                        # =============ROLL NO===================

        lbl_roll=Label(Manage_Frame,text="Roll No",bg="Crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_Var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

                        #=============Name Details===================

        lbl_name = Label(Manage_Frame, text="Name", bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.name_Var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

                        # =============Email===================

        lbl_email = Label(Manage_Frame, text="Email ID", bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame,textvariable=self.email_Var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

                            # =============Gender===================

        lbl_gender = Label(Manage_Frame, text="Gender", bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_Var,font=("times new roman", 14, "bold"),state='readonly')
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

                          # =============CONTACT===================

        lbl_contact = Label(Manage_Frame, text="Contact", bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_Var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

                            # =============D.O.B===================

        lbl_dob = Label(Manage_Frame, text="D.O.B",bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame,textvariable=self.dob_Var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

                            # =============ADDRESS===================

        lbl_address = Label(Manage_Frame, text="Address", bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

                        # =============button Frame===================

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="Crimson")
        btn_Frame.place(x=15, y=520, width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_Frame, text="Update",width=10,command=self.update_data).grid(row=0, column=1,padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete",width=10,command=self.delete_data).grid(row=0, column=2,padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="clear",width=10,command=self.clear_data).grid(row=0, column=3,padx=10, pady=10)

# Second Frame For All Details

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="Crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=590)

                    # =============Search BY===================

        lbl_search = Label(Detail_Frame, text="Search By", bg="Crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        #================== entry Field And Text Button===============

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2, pady=10, padx=20, sticky="w")

                        # =============button Frame===================

        searchbtn = Button(Detail_Frame, text="search",width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showbtn = Button(Detail_Frame, text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        #======================== Table Frame ======================


        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","gender","email","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        # ========================= To Add Data =============================

    def add_students(self):
        if self.Roll_No_Var.get()=="" or self.name_Var.get()=="" or self.email_Var.get()=="" or self.gender_Var.get()=="" or self.contact_Var.get()=="" or self.dob_Var.get()=="" or self.txt_address.get('1.0')=="":
            messagebox.showerror("Error","All Fields Are Required!!!")
        else:
                con=pymysql.connect(host="localhost",user="root",password="root",database="stm")
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_Var.get(),
                                                                                 self.name_Var.get(),
                                                                                 self.email_Var.get(),
                                                                                 self.gender_Var.get(),
                                                                                 self.contact_Var.get(),
                                                                                 self.dob_Var.get(),
                                                                                 self.txt_address.get('1.0',END)
                                                                                 ))
                con.commit()
                self.fetch_data()
                self.clear_data()
                con.close()
                messagebox.showinfo("Success","Record Has Been Inserted Successfully!!!")

         # ========================= To fetch The All Data =============================

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root",database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear_data(self):
        self.Roll_No_Var.set("")
        self.name_Var.set("")
        self.email_Var.set("")
        self.gender_Var.set("")
        self.contact_Var.set("")
        self.dob_Var.set("")
        self.txt_address.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_Var.set(row[0])
        self.name_Var.set(row[1])
        self.email_Var.set(row[2])
        self.gender_Var.set(row[3])
        self.contact_Var.set(row[4])
        self.dob_Var.set(row[5])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root", database="stm")


        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                                self.name_Var.get(),
                                                                                                                self.email_Var.get(),
                                                                                                                self.gender_Var.get(),
                                                                                                                self.contact_Var.get(),
                                                                                                                self.dob_Var.get(),
                                                                                                                self.txt_address.get('1.0', END),
                                                                                                                self.Roll_No_Var.get()
                                                                                                                    ))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root",database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_Var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root",database="stm")
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()