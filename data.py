from tkinter import*
from tkinter import ttk
import pymysql


class Student():
    def __init__(self, name):
        self.name = name
        self.name.title("Student Mangement system")
        self.name.geometry("1525x780+0+0")

        title =Label(self.name,text="Student Mangement system",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
         #================================All variable==================
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.Email_var = StringVar()
        self.Expiry_var = StringVar()
        self.Manufacturing_var = StringVar()
        self.MRP_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        


        #================================MangeFrame==================
        Mange_Frame = Frame(self.name,)
        Mange_Frame = Frame(self.name, width=400, height=850, bg="blue",bd=4,relief=RIDGE)
        Mange_Frame.place(x=0,y=100)

        m_title = Label(Mange_Frame,text="Mange Student",bg="yellow",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0, columnspan=2,pady=20)


        lbl_roll =Label(Mange_Frame,text="Roll No",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0,pady=10,padx=10,sticky="w")
        txt_Roll = Entry( Mange_Frame,textvariable= self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1,pady=20,padx=10,sticky="w")

        lbl_name = Label(Mange_Frame,text="Name",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2, column=0,pady=10,padx=10,sticky="w")
        txt_name = Entry( Mange_Frame,textvariable= self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2, column=1,pady=20,padx=10,sticky="w")

        lbl_Email = Label(Mange_Frame,text="Email",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3, column=0,pady=10,padx=10,sticky="w")
        txt_Email = Entry( Mange_Frame,textvariable= self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3, column=1,pady=20,padx=10,sticky="w")

        lbl_Expiry = Label(Mange_Frame,text="Expiry Date",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Expiry.grid(row=4, column=0,pady=10,padx=10,sticky="w")
        txt_Expiry = Entry( Mange_Frame,textvariable= self.Expiry_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Expiry.grid(row=4, column=1,pady=20,padx=10,sticky="w")

        lbl_Manufacturing = Label(Mange_Frame,text="Manufacturing Date",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Manufacturing.grid(row=5, column=0,pady=10,padx=10,sticky="w")
        txt_Manufacturing = Entry( Mange_Frame,textvariable= self.Manufacturing_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Manufacturing.grid(row=5, column=1,pady=20,padx=10,sticky="w")

        lbl_MRP = Label(Mange_Frame,text="MRP",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_MRP.grid(row=6, column=0,pady=10,padx=10,sticky="w")
        txt_MRP = Entry( Mange_Frame,textvariable= self.MRP_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_MRP.grid(row=6, column=1,pady=20,padx=10,sticky="w")

        #=========btn frame=======
        btn_frame = Label(Mange_Frame,text="",bg="blue",fg="white",font=("times new roman",20,"bold"))
        btn_frame.grid(row=7, column=0,pady=10,padx=10,)

        Addbtn = Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=7,column=1,padx=10,pady=10)
        updatebtn = Button(btn_frame,text="update",width=10).grid(row=7,column=2,padx=10,pady=20)
        deletebtn = Button(btn_frame,text="Delet",width=10).grid(row=7,column=3,padx=10,pady=10)
        clearbtn = Button(btn_frame,text="Clear",width=10).grid(row=7,column=4,padx=10,pady=10)
        #======== Details Frame======

        Details_Frame = Frame(self.name,bd=4,relief=RIDGE,bg="blue")
        Details_Frame.place(x=700,y=100,width=820,height=680)

        lbl_search = Label(Details_Frame,text="Search By",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=10,)

        combo_search = ttk.Combobox( Details_Frame,textvariable= self.search_by,font=("times new roman",13,"bold"),width=10,state='readonly')
        combo_search['values'] = ("Roll.no","Name","Contact")
        combo_search.grid(row=0, column=1,padx=20,pady=10)
        txt_search= Entry(Details_Frame,textvariable= self.search_txt,font=("times new roman",10,"bold"),width=20, bd=5,relief=GROOVE)
        txt_search.grid(row=0, column=2,pady=10,padx=20,sticky="w")

        searchbtn = Button(Details_Frame,text="search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Details_Frame,text="show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

#========Table Frame========
        Table_Frame = Frame(Details_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=805,height=600)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("roll","name","Email","Expiry","Manufacturing","MRP"),xscrollcommand=scroll_y,yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Expiry",text="Expiry Date")
        self.Student_table.heading("Manufacturing",text="Manufacturing Date")
        self.Student_table.heading("MRP",text="M.R.P")


        self.Student_table['show']= 'headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Expiry",width=100)
        self.Student_table.column("Manufacturing",width=100)
        self.Student_table.column("MRP",width=100)


        self.Student_table.pack(fill=BOTH,expand=1)
    def add_students(self):
         con = pymysql.connect(host="localhost",user="name",password="",databasa="sms2")
         cur= con.cursor()
         cur.execte("insert into studerts-nitesh values (%s,%s,%s,%s,%s,%s,)",(self.Roll_No_var.get(),
                                                                                         self.name_var.get(),
                                                                                         self.Email_var.get(),
                                                                                         self.Expiry_var.get(),
                                                                                         self.Manufacturing_var.get(),
                                                                                         self.MRP_var.get('1.0',END)))
         con.commit()
         con.close()                                                                                 



       



class Student():
        pass
        root = Tk( )
        obj=Student(root)
        root.mainloop()
