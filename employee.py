from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        lbl_title = Label(self.root, text='JSW EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'),
                          fg="darkblue", bg="white")
        lbl_title.place(x=0, y=0, width=1530, height=50)

        #logo
        img_logo=Image.open('images/logo.jpg')
        img_logo=img_logo.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=200,y=0,width=50,height=50)

        # Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st
        img1=Image.open('images/emp1.jpg')
        img1=img1.resize((540,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(self.root,image=self.photo1)
        self.img_1.place(x=0,y=50,width=540,height=160)

        #  #2nd
        img_2=Image.open('images/emp4.jpeg')
        img_2=img_2.resize((540,160))
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #  #3rd
        img_3=Image.open('images/emp3.jpeg')
        img_3=img_3.resize((540,160))
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        # Main Frame

        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=220,width=1500,height=560)

        # upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg="red")
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department', 'HR', 'Information Technology', 'Safety', 'Training', 'Manager', 'Accounts', 'Administration', 'Auto Reconditioning Shop', 'Bar Mill', 'Billet Caster', 'Blast Furnace 1', 'Blast Furnace 2', 'Business Excellence', 'Business Planning & Costing', 'Captive Power Plant', 'Central Maintenance', 'Dept List', 'Central Mechanical Maintenance', 'Central Planning Team Central Repair Shop', 'Central Utilities', 'Centralized E & A', 'Civil', 'Civil & Structural', 'Civil, Structural & Infrastructure Maintenance', 'Coke Making', 'Coke Oven 1', 'Coke Oven 1 & 2 (Batt. A & B)', 'Coke Oven 2', 'Coke Oven 2- (Batt. C & D)', 'Coke Oven 2 (Batt. A & B)', 'Commercial', 'Compact Strip Production Caster', 'Compact Strip Production Caster & Mill', 'Compact Strip Production Mill', 'Concrete Lab', 'Condition Monitoring', 'Construction', 'Conveyor Maintenance', 'Corporate Accounts', 'Crane Electrical Maintenance Department', 'Crane Maintenance', 'Crane Phase 2', 'Credit Control', 'CSR General', 'Customer Service Department', 'Cut To Length', 'Digital Excellence', 'Dolvi Plant', 'Electrical', 'Electrical & Instrumentation', 'Energy Management Department', 'Environment', 'Environment, Health & Safety', 'Estimation & Budgeting', 'Finance & Accounts', 'Fire & Safety', 'Gas Insulated Substation Project', 'Health Services', 'Horticulture', 'Hospital & Township', 'Hot Strip Mill', 'Human Resource', 'Indirect Taxation', 'Industrial Paint - Sales Information Technology', 'Infrastructure Maintenance', 'Insurance', 'Internal Audit', 'Iron & Agglomeration Projects', 'Iron & Agglomeration Zone', 'Jetty', 'JMD Office Land & Estate', 'Legal', 'Lime Calcination Plant 1 to 4', 'Lime Calcination Plant 5 to 7', 'Loco & Track', 'Logistics', 'Logistics Phase 2', 'Maintenance', 'Management Services Cell', 'Manufacturing Excellence', 'Marine Operations', 'Material Planning & Prevention Group', 'Mechanical', 'Mould & Segment Shop', 'MSME-Plant Supply', 'Operations', 'Oxygen Plant', 'Packing Plant', 'Pellet Plant 1', 'Pellet Plant 2', 'Planning Cell', 'Power Distribution', 'Power Distribution Project', 'Power Plant Project', 'PPC Iron Zone', 'PPC Steel Zone', 'President Office', 'Process Control Cell Iron Zone', 'Process Control Cell Steel Zone', 'Product Development & Quality Control', 'Production & Process', 'Project', 'Project (Lime Calcination Plant) 5,6,7', 'Project HSM 2', 'Projects', 'Public Relations', 'Quality Assurance Iron Zone', 'Quality Assurance Steel Zone', 'Quality Control', 'Quality Control & Assurance', 'Raw Material Handling', 'Raw Material Planning', 'Re-Engineering & Drawing', 'Refractory', 'Research & Development', 'RMHS 10 MΤΡΑ', 'Sales Audit', 'Safety', 'Security', 'Sinter Plant 1', 'Sinter Plant 1 & 2', 'Sinter Plant 2', 'SMS 2', 'Sponge Iron Plant', 'Steel & Mills Zone', 'Steel Melting Shop 1', 'Steel Melting Shop 2', 'Stores', 'Structural', 'Technical Cell', 'Technology Excellence', 'Unit Head Office', 'Utility Electrical', 'Utility Project', 'Utility Projects', 'Utility Services', 'Vigilance')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Name
        lbl_Name=Label(upper_frame,font=("arial",12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #lbl_Designition
        lbl_Designition=Label(upper_frame,font=("arial",12,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=1,column=0,sticky=W,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Email
        lbl_email=Label(upper_frame,font=("arial",12,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_address=Label(upper_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        #Married
        lbl_married_status=Label(upper_frame,font=("arial",12,"bold"),text="Maritial Status:",bg="white")
        lbl_married_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_married['value']=("Select","Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # DOB
        lbl_dob=Label(upper_frame,font=("arial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # Doj
        lbl_doj=Label(upper_frame,font=("arial",12,"bold"),text="DOJ:",bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        # ID Proof

        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_proof['value']=("Select ID Proof","PAN CARD","AADHAR CARD", "DRIVING LICENSE","VOTING CARD")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        #gender
        lbl_gender=Label(upper_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Select Gender","Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7) 

        # Phone
        lbl_phone=Label(upper_frame,font=("arial",12,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,font=("arial",12,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # CTC
        lbl_ctc=Label(upper_frame,font=("arial",12,"bold"),text="Salary(CTC):",bg="white")
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        # Disp image

        img_disp=Image.open('images/disp.jpg')
        img_disp=img_disp.resize((220,200))
        self.photodisp=ImageTk.PhotoImage(img_disp)

        self.img_disp=Label(upper_frame,image=self.photodisp)
        self.img_disp.place(x=1000,y=0,width=220,height=220)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1290, y=20, width=170, height=210)

        btn_add = Button(button_frame, text="Save", command=self.add_data, font=("arial", 15, "bold"), width=13,
                         bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        # down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg="red")
        down_frame.place(x=10,y=280,width=1480,height=270)

        # Search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg="red")
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="White",bg="Red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # Search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Phone","id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5) 

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn__search = Button(search_frame, text="Search",command=self.search_data,font=("arial", 11, "bold"), width=13, bg='blue', fg='white')
        btn__search.grid(row=0, column=3, padx=5)


        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=13,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        slogan=Label(search_frame,text='Better Everyday',font=('Book Antiqua',18,'bold'),fg="red",bg="white")
        slogan.place(x=780,y=0,width=600,height=28)

        # slogan logo
        img_logo_slogan=Image.open('images/logo.jpg')
        img_logo_slogan=img_logo_slogan.resize((50,50))
        self.photo_logo_slogan=ImageTk.PhotoImage(img_logo_slogan)

        self.logo=Label(search_frame,image=self.photo_logo_slogan)
        self.logo.place(x=900,y=0,width=50,height=30)

        # ======================== Employee Table ======================

        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department') 
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("degi", text="Designition") 
        self.employee_table.heading("email", text="Email") 
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("married", text="Maratial Status")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("idproofcomb", text="ID Type")
        self.employee_table.heading("idproof", text="ID Proof")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("phone", text="Phone")
        self.employee_table.heading("country", text="Country")
        self.employee_table.heading("salary", text="Salary")

        self.employee_table['show']='headings'

        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    # **********************Function Declaration****************


    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='harsh@123#',
                                               database='employee-mgmt')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designition.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added!', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='harsh@123#', database='employee-mgmt')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from employee1')
        data = my_cursor.fetchall()  # Added parentheses () here
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this employee data')
                if update>0:
                
                    conn = mysql.connector.connect(host='localhost', username='root', password='harsh@123#',
                                                database='employee-mgmt')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Maratial_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(

                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_designition.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_married.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_doj.get(),
                                                                                                                                                                                                                                self.var_idproofcomb.get(),
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_country.get(),
                                                                                                                                                                                                                                self.var_salary.get(),
                                                                                                                                                                                                                                self.var_idproof.get()

                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Employee Successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error',"All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure to delete this employee',parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='harsh@123#',
                                                database='employee-mgmt')
                    my_cursor = conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Employee Successfully deleted!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    # Reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Select")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    # Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='harsh@123#',
                                                database='employee-mgmt')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee1 where ' + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = my_cursor.fetchall()  
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                else:
                    messagebox.showinfo('Info', 'No data found!', parent=self.root)  # Notify if no data found
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)



    





if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
