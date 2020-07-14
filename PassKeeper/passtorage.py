from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys

global username
# Splash screen
class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("Password storage")
        self.master.geometry("800x800")
        self.master.iconbitmap("images/password.ico")
        self.font = ("Courier New", "14", "bold")
        Label(self.master, text="WELCOME TO THE PASSWORD STORAGE",
              font=self.font, justify=CENTER).pack(pady=100)
        self.img = ImageTk.PhotoImage(Image.open("images/pass.jpg"))
        Label(self.master, image=self.img).pack()
        ttk.Button(self.master, text="ABOUT",
                   command=self.about).pack(padx=10, pady=10)
        ttk.Button(self.master, text="SIGN UP",
                   command=self.sign).pack(padx=10, pady=10)
        ttk.Button(self.master, text="LOGIN",
                   command=self.login).pack(padx=10, pady=10)
        ttk.Button(self.master, text="EXIT",
                   command=self.exit).pack(padx=10, pady=10)
        
    def about(self):
        abt = Toplevel()
        abt.title("About")
        abt.geometry("550x200")
        abt.iconbitmap("images/password.ico")
        Label(abt,text="ABOUT PASSWORD STORAGE",font=self.font).pack(pady=5)
        Label(abt,text='''This is a password storage account that enables
        you to store your various accounts and the 
        corresponding passwords. Ever got into a situation
        where you have forgotten your password? Well, this
        is the solution to your problem. No need of 
        remembering passwords anymore!!''',font=("Courier New",10),justify=CENTER).pack()
        Label(abt,text="Version 1.0.0").pack(side=BOTTOM)
        Label(abt,text=u'\u00A9'+ " Immanuel Kituku 2020").pack(side=BOTTOM)
        abt.lift()

    def sign(self):
        '''switch to the sign up window from splashscreen'''
        
        self.master.withdraw()
        top = Toplevel()
        sign = SignUp(top)
        top.lift()

    def login(self):
        '''switch to the login window from splashscreen'''
        
        self.master.withdraw()
        top = Toplevel()
        sign = Login(top)
        top.lift()
    
    def exit(self):
        sys.exit()

#Sign up Window
class SignUp(Main):
    def __init__(self, window):
        super().__init__(master=root)
        self.window = window
        self.window.title("Signup Form")
        self.window.geometry("800x800")
        self.window.iconbitmap("images/password.ico")
        self.font = ("Courier New", "14", "bold")
        self.sign_up_lbl = Label(self.window, text="SIGN UP", font=self.font)
        self.sign_up_lbl.pack(side=TOP, padx=10, pady=30)
        self.img = ImageTk.PhotoImage(Image.open("images/form.jpg"))
        Label(self.window, image=self.img).pack(pady=10)
        self.sign_lbl()
        ttk.Button(self.window,text="SUBMIT",command=self.submit).pack(pady=5)
        ttk.Button(self.window,text="BACK",command=self.back).pack(pady=5)

    def sign_lbl(self):
        '''Creates the sign up form'''
        
        Label(self.window, text="Firstname", fg="black").pack(pady=5)
        self.first_name = ttk.Entry(self.window, width=40)
        self.first_name.pack(pady=5)
        Label(self.window, text="Lastname", fg="black").pack(pady=5)
        self.last_name = ttk.Entry(self.window, width=40)
        self.last_name.pack(pady=5)
        Label(self.window, text="Email", fg="black").pack(pady=5)
        self.email = ttk.Entry(self.window, width=40)
        self.email.pack(pady=5)
        Label(self.window, text="Username", fg="black").pack(pady=5)
        self.user_name = ttk.Entry(self.window, width=40)
        self.user_name.pack(pady=5)
        Label(self.window, text="Password", fg="black").pack(pady=5)
        self.password = ttk.Entry(self.window, width=40,show="*")
        self.password.pack(pady=5)
        Label(self.window, text="Re-enter password", fg="black").pack(pady=5)
        self.re_password = ttk.Entry(self.window, width=40,show="*")
        self.re_password.pack(pady=5)
        
    def submit(self):
        #Connection to database
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        #Checks whether password matches
        if self.password.get() != self.re_password.get():
            messagebox.showwarning("Password Error","Password Not Matching!!")
            self.master.lower()
        
        # Inserts details to the users table in database 
        if self.first_name or self.last_name or self.email or self.user_name or self.password or self.re_password != '':
            self.c.execute("INSERT INTO users VALUES(:first_name,:last_name,:email,:user_name,:password)",
                        {
                            'first_name':self.first_name.get(),
                            'last_name':self.last_name.get(),
                            'email':self.email.get(),
                            'user_name':self.user_name.get(),
                            'password':self.password.get()
                        })
            messagebox.showinfo("Add Record","Successfully created account")
            self.master.lower()
            
        self.conn.commit()
        
    def back(self):
        '''Go back to Main Menu'''
        
        self.master.deiconify()
        self.window.withdraw()
        
class Login(Main):
    def __init__(self, window):
        super().__init__(master=root)
        self.window = window
        self.window.title("Login Form")
        self.window.geometry("800x800")
        self.window.iconbitmap("images/password.ico")
        self.font = ("Courier New", "14", "bold")
        self.sign_up_lbl = Label(self.window, text="LOGIN", font=self.font)
        self.sign_up_lbl.pack(side=TOP, padx=10, pady=30)
        self.img = ImageTk.PhotoImage(Image.open("images/form.jpg"))
        Label(self.window, image=self.img).pack(pady=10)
        self.log_lbl()
        ttk.Button(self.window,text="LOGIN",command=self.log).pack(pady=10)
        ttk.Button(self.window,text="BACK",command=self.back).pack(pady=10)

    def log_lbl(self):
        '''Creates the login form'''
        Label(self.window, text="Username", fg="black").pack(pady=5)
        self.user = ttk.Entry(self.window, width=40)
        self.user.pack(pady=5)
        Label(self.window, text="Password", fg="black").pack(pady=5)
        self.passwd = ttk.Entry(self.window, width=40,show="*")
        self.passwd.pack(pady=5)
        
    def log(self):
        global username
        #Connection to database
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT user_name,password FROM users")
        users = self.c.fetchall()
        username = self.user.get()
        log_details = (self.user.get(),self.passwd.get())
        if log_details in users:
            self.master.withdraw()
            messagebox.showinfo("Login Info","Login successful")
            self.window.withdraw()
            toppass = Toplevel()
            Password(toppass)
        elif self.user.get() not in users:
            self.master.withdraw()
            messagebox.showwarning("Login Info","Login Failed!! Try again")
            self.window.lift()
            self.master.deiconify()
            self.master.lower()
        
    def back(self):
        '''Go back to Main Menu'''
        self.master.deiconify()
        self.window.withdraw()
        
class Password(Login):
    def __init__(self, window):
        self.window = window
        self.window.title("PASS MENU")
        self.window.geometry("800x800")
        self.window.iconbitmap("images/password.ico")
        self.font = ("Courier New", "14", "bold")
        self.username = username
        self.sign_up_lbl = Label(self.window, text=f"WELCOME {username.upper()} TO YOUR PASSWORD STORAGE ACCOUNT", font=self.font)
        self.sign_up_lbl.pack(side=TOP, padx=10, pady=30)
        self.tree = Frame(self.window,bg="white")
        self.findf = Frame(self.window,width=100)
        self.btns = Frame(self.window,width=100)
        self.ex = Frame(self.window,width=100)
        #Search section
        self.q = StringVar()
        Label(self.findf,text="Search: ").pack(side=LEFT,padx=5,pady=10)
        self.ent_search = ttk.Entry(self.findf,textvariable=self.q)
        self.ent_search.pack(side=LEFT,padx=5,pady=10)
        ttk.Button(self.findf,text="Search",command=self.search).pack(side=LEFT,padx=10,pady=5,ipadx=5)
        self.findf.pack(side=TOP,padx=5,pady=20)
        #Insert, Update, Delete and View Buttons
        ttk.Button(self.btns,text="Insert",command=self.insert_win).pack(side=LEFT,padx=10,pady=5,ipadx=5,ipady=5)
        ttk.Button(self.btns,text="Update", command=self.update_win).pack(side=LEFT,padx=10,pady=5,ipadx=5,ipady=5)
        ttk.Button(self.btns,text="Delete", command=self.delete_win).pack(side=LEFT,padx=10,pady=5,ipadx=5,ipady=5)
        ttk.Button(self.btns,text="View Details", command=self.view_details).pack(side=LEFT,padx=10,pady=5,ipadx=5,ipady=5)
        ttk.Button(self.ex,text="Exit", command=self.exit).pack(side=LEFT,padx=10,pady=5,ipadx=5,ipady=5)
        self.ex.pack(side=BOTTOM,padx=5,pady=10)
        self.btns.pack(side=BOTTOM,padx=5,pady=10)
        self.tv = ttk.Treeview(self.tree, columns=(1,2,3), show="headings",height="12")
        self.tv.pack()
        self.tv.heading(1, text="ID")
        self.tv.heading(2, text="Name_Of_Website/Platform")
        self.tv.heading(3, text="Password")
        self.tree.pack(side=TOP,padx=5,pady=10)
    
    def search(self):
        x  = self.tv.get_children()
        for items in x:
            self.tv.delete(items)
        q2 = self.q.get()
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        query = find_user = ("SELECT oid,Name_of_platform,Pass FROM passwords WHERE Name_of_platform=?")
        self.c.execute(query,[(q2)])   
        records = self.c.fetchall()
        
        for record in records:
            self.tv.insert('','end',values=record)
            
        self.conn.commit()
    
    def insert_win(self):
        #Connection to database
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        self.ins = Toplevel()
        self.ins.title("Insert Data")
        self.ins.geometry("300x150")
        self.ins.iconbitmap("images/password.ico")
        Label(self.ins,text="Name of Platform: ").grid(row=0,column=0,padx=10,pady=5)
        self.ent_plat = ttk.Entry(self.ins,width=20)
        self.ent_plat.grid(row=0,column=1,padx=5,pady=5)
        Label(self.ins,text="Password To Insert: ").grid(row=1,column=0,padx=10,pady=5)
        self.ent_pass = ttk.Entry(self.ins,width=20,show="*")
        self.ent_pass.grid(row=1,column=1,padx=5,pady=5)
        self.submit = ttk.Button(self.ins,text="SUBMIT",command=self.insert_data).grid(row=2,column=0,columnspan=2,padx=10,pady=5)
        
    def insert_data(self):
        self.c.execute("INSERT INTO passwords VALUES(:user_name,:platform,:passwd)",
                       {
                           'user_name':username,
                           'platform':self.ent_plat.get(),
                           'passwd':self.ent_pass.get()
                       })
        
        self.conn.commit()
        self.ent_plat.delete(0,END)
        self.ent_pass.delete(0,END)
        messagebox.showinfo("Insert","Inserted successfully!!!")
        self.ins.withdraw()
            
    def update_win(self):
        #Connection to database
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        self.upd = Toplevel()
        self.upd.title("Update Data")
        self.upd.geometry("300x150")
        self.upd.iconbitmap("images/password.ico")
        self.upd_frame = Frame(self.upd)
        Label(self.upd_frame,text="ID: ").grid(row=0,column=0,padx=10,pady=5)
        self.iden = ttk.Entry(self.upd_frame,width=10)
        self.iden.grid(row=0,column=1,padx=5,pady=5)
        self.ok = ttk.Button(self.upd_frame,text="OK",command=self.okay_btn).grid(row=2,column=0,padx=10,pady=5)
        self.upd_frame.pack()
        
    def okay_btn(self):
        global record_id
        global plat
        global passd
        record_id = self.iden.get()
        self.c.execute("SELECT Name_of_platform,Pass FROM passwords WHERE oid="+ record_id)
        records = self.c.fetchall()
       
        for widget in self.upd_frame.winfo_children():
            widget.destroy()
        Label(self.upd_frame,text="Name of Platform: ").grid(row=0,column=0,padx=10,pady=5)
        plat = ttk.Entry(self.upd_frame,width=20)
        plat.grid(row=0,column=1,padx=5,pady=5)
        Label(self.upd_frame,text="Password: ").grid(row=1,column=0,padx=10,pady=5)
        passd = ttk.Entry(self.upd_frame,width=20)
        passd.grid(row=1,column=1,padx=5,pady=5)
        self.submit = ttk.Button(self.upd_frame,text="UPDATE",command=self.update_data).grid(row=2,column=0,columnspan=2,padx=10,pady=5)
        self.upd_frame.pack()
        for record in records:
            plat.insert(0, record[0])
            passd.insert(0, record[1])
        self.conn.commit()
        
        
            
    def update_data(self):
        #Connection to database
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        self.c.execute("UPDATE passwords SET Name_of_platform = ?, Pass = ? WHERE oid=?",(plat.get(),passd.get(),record_id))
        self.conn.commit()
        messagebox.showinfo("Update","Data Updated Successfully")
        self.upd.withdraw()
            
    
    def delete_win(self):
        #Connection to database
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        self.delete = Toplevel()
        self.delete.title("Delete Data")
        self.delete.geometry("300x170")
        self.delete.iconbitmap("images/password.ico")
        Label(self.delete,text="ID: ").grid(row=0,column=0,padx=10,pady=5)
        self.id = ttk.Entry(self.delete,width=10)
        self.id.grid(row=0,column=1,padx=5,pady=5)
        self.submit = ttk.Button(self.delete,text="DELETE",command=self.delete_data).grid(row=2,column=0,columnspan=2,padx=10,pady=5)
        
    def delete_data(self):
        messagebox.showwarning("Delete","Do you want to continue!!!")
        self.c.execute("DELETE FROM passwords WHERE oid="+self.id.get())
        self.conn.commit()
        messagebox.showinfo("Delete","Deleted successfully!!!")
        self.delete.withdraw()
        
    def view_details(self):
        #Clear Frame
        #Connection to database
        global username
        x  = self.tv.get_children()
        for items in x:
            self.tv.delete(items)
            
        self.conn = sqlite3.connect("password.db")
        self.c = self.conn.cursor()
        find_user = ("SELECT oid,Name_of_platform,Pass FROM passwords WHERE user_name=?")
        self.c.execute(find_user,[(username)])   
        records = self.c.fetchall()
        
        for record in records:
            self.tv.insert('','end',values=record)
            
        self.conn.commit()
           
root = Tk()
main = Main(root)
root.mainloop()
