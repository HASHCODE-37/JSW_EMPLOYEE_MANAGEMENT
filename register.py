from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # ========== Variables ===============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ========== bg image =============
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Employee_management\images\regi.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ========== left Image ============
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Employee_management\images\crain.jpeg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="dark green", bg="white")
        register_lbl.place(x=20, y=20)

        # ============= label and entry =============

        # ================= Row 1 =================
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ================= Row 2 ===================
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ============== Row 3 ==================
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place?", "Your School Name?", "Your Bestfriends School?", "Your Pet Name?")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ============== Row 4 ================
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirn_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirn_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)


        # ======================= Check Button ============
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # ======================Button=====================
        img = Image.open(r"C:\Users\DELL\Desktop\Employee_management\images\regi2.png")
        img = img.resize((120, 60))
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), bg="white")
        b1.place(x=10, y=420, width=300)

        img1 = Image.open(r"C:\Users\DELL\Desktop\Employee_management\images\login-btn.png")
        img1 = img1.resize((120, 60))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), bg="white")
        b1.place(x=330, y=420, width=300)

    # ============= Function Declaration =====================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields are Required!")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Both Passwords must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please check the terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="harsh@123#", database="employee-mgmt")
                my_cursor = conn.cursor()
                
                query = "SELECT * FROM register WHERE email = %s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    insert_query = "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    insert_values = (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),  
                        self.var_securityA.get(),  
                        self.var_pass.get()
                    )

                    my_cursor.execute(insert_query, insert_values)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "User Registered Successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {str(e)}")

            







if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
