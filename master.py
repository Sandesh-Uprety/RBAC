# import modules
# from tkinter import *   ## notice lowercase 't' in tkinter here
from tkinter import *
import sqlite3
import tkinter.messagebox
import os, sys, webbrowser
from PIL import Image, ImageTk

conn = sqlite3.connect('database.db')
c = conn.cursor()


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1060x540")
        self.master.title("Access Control in EMR")
        self.master.resizable(False, False)
        self.master.config(bg="skyblue")
        self.master.iconphoto(False, PhotoImage(file="resources/icon.png"))

        # menu bar
        Chooser = Menu()  # object of class menu

        Chooser.add_command(label='About', command=self.aboutMaster)
        Chooser.add_command(label='Help')
        Chooser.add_command(label='Exit', command=lambda: exitRoot(root))

        root.config(menu=Chooser)

        self.frame1_left = Frame(self.master, bg='grey')
        self.frame1_left.place(x=10, y=10, width=380, height=500, )

        self.frame2_right = Frame(self.master, bg='grey')
        self.frame2_right.place(x=400, y=10, width=650, height=500)

        self.loginLabel = Label(self.frame1_left, text="\nEnter login credentials\n", font=('arial 14 bold'),
                                fg='black')
        self.loginLabel.grid(row=0, column=0, padx=8, pady=50)

        # login ID
        self.login_id = Label(self.frame1_left, text="Login ID*", font=('arial 12'), fg='black')
        self.login_id.grid(row=1, column=0, padx=8, pady=5)

        # password
        self.password = Label(self.frame1_left, text="Password*", font=('arial 12'), fg='black')
        self.password.grid(row=2, column=0, padx=8, pady=5)

        # entries for labels
        self.login_id_ent = Entry(self.frame1_left, width=20)
        self.login_id_ent.grid(row=1, column=1, padx=8, pady=5)

        self.password_ent = Entry(self.frame1_left, width=20, show='*')
        self.password_ent.grid(row=2, column=1, padx=8, pady=5)

        # button to login
        self.loginShield = PhotoImage(file="resources/user-shield-100.png")
        self.buttonImage = self.loginShield.subsample(3, 3)
        self.submit = Button(self.frame1_left, text='Login', image=self.buttonImage, compound=LEFT, width=120,
                             height=40, bg='steelblue', command=self.login1)
        self.submit.grid(row=3, column=1, padx=8, pady=50)

        self.bg = ImageTk.PhotoImage(file="resources/Hospital.png")
        self.bg_image = Label(self.frame2_right, image=self.bg)
        self.bg_image.place(x=10, y=10, relwidth=1, relheight=1)
        self.hosLabel = Label(self.frame2_right, text="\nHospital Access Control System\n", font=('arial 14 bold'),
                              fg='black')
        self.hosLabel.place(x=180, y=10)

    # function to login
    def login(self, event):  # function for pressing enter
        # self.db_pass = ""
        self.id = self.login_id_ent.get()
        print(type(self.id))
        self.password = self.password_ent.get()

        if self.id == "" or self.password == "":  # condition for empty fields
            tkinter.messagebox.showwarning("All credentials required",
                                           "Please enter all fields. Fields marked (*) are required.")
        else:
            self.login_id_ent.delete(0, END)
            self.password_ent.delete(0, END)
            sql = "SELECT * FROM credentials WHERE name=? and pass=?"
            # self.input = self.id
            self.res = c.execute(sql, (self.id, self.password))
            row = self.res.fetchone()
            # for row in self.res:
            #     self.db_name = row[1]
            #     self.db_pass = row[2]
            #     self.db_designation = row[3]

            self.db_name = row[1]
            self.db_pass = row[2]
            self.db_designation = row[3]

            if self.db_pass == self.password:
                tkinter.messagebox.showinfo("Login Successful",
                                            "Hello " + self.db_name + "! You have successfully logged in as " + self.db_designation)
                self.drawWin()  # function call to create new window
            else:
                tkinter.messagebox.showerror("Login Unsuccessful", "Invalid credentials! Please login again")

    def login1(self):  # function for clicking the button
        # self.db_pass = ""
        self.id = self.login_id_ent.get()
        print(type(self.id))
        self.password = self.password_ent.get()

        if self.id == "" or self.password == "":
            tkinter.messagebox.showwarning("All credentials required",
                                           "Please enter all fields. Fields marked (*) are required.")
        else:
            self.login_id_ent.delete(0, END)
            self.password_ent.delete(0, END)
            sql = "SELECT * FROM credentials WHERE name =? and pass =?"
            # self.input = self.id
            self.res = c.execute(sql, (self.id, self.password))
            row = self.res.fetchone()
            # for row in self.res:
            #     self.db_name = row[1]
            #     self.db_pass = row[2]
            #     self.db_designation = row[3]

            self.db_name = row[1]
            self.db_pass = row[2]
            self.db_designation = row[3]

            if self.db_pass == self.password:
                tkinter.messagebox.showinfo("Login Successful",
                                            "Hello " + self.db_name + "! You have successfully logged in as " + self.db_designation)
                self.drawWin()
            else:
                tkinter.messagebox.showerror("Login Unsuccessful", "Invalid credentials! Please login again")

    # function to draw toplevel window
    def drawWin(self):
        # hiding root window
        hide_root()

        # drawing toplevel window
        top = Toplevel()
        top.geometry("1060x540")
        top.title("Welcome to the system")
        top.resizable(False, False)
        top.config(bg="skyblue")
        top.iconphoto(False, PhotoImage(file="resources/icon.png"))

        Chooser = Menu()  # horizontal menu
        itemone = Menu()  # vertical menu for file

        self.frame1_left = Frame(top, bg='grey')
        self.frame1_left.place(x=10, y=10, width=380, height=500)

        self.frame2_right = Frame(top, bg='grey')
        self.frame2_right.place(x=400, y=10, width=650, height=500)

        if self.db_designation == 'System Administrator' or self.db_designation == 'Doctor':
            itemone.add_command(label='Add Appointment', command=self.appointment)
            itemone.add_command(label='Edit Appointment', command=self.update)
            itemone.add_command(label='Delete Appointment', command=self.update)

        itemone.add_command(label='View Appointment', command=self.display)
        itemone.add_separator()

        if self.db_designation == 'System Administrator':
            itemone.add_command(label='Add user', command=self.user)

        itemone.add_command(label='Logout', command=lambda: self.logout(top))

        Chooser.add_cascade(label='File', menu=itemone)  # because it has inside cascaded manu
        Chooser.add_command(label='View Appointment', command=self.display)
        Chooser.add_command(label='Logout', command=lambda: self.logout(top))

        top.config(menu=Chooser)
        top.iconphoto(False, PhotoImage(
            file="resources/icon.png"))  # if default is true,it is applied to all future top levels

        self.right = Frame(self.frame2_right, width=630, height=200)
        self.right.place(x=10, y=10)
        if self.db_designation == 'System Administrator':
            self.bg = ImageTk.PhotoImage(file="resources/Admin.png")
            self.bg_image = Label(self.frame1_left, image=self.bg)
            self.bg_image.place(relwidth=1, relheight=1)

            self.fg = ImageTk.PhotoImage(file="resources/aa.jpg")
            self.fg_image = Label(self.frame2_right, image=self.fg)
            self.fg_image.place(x=80, y=230)


        elif self.db_designation == 'Doctor':
            self.bg = ImageTk.PhotoImage(file="resources/Doctor.png")
            self.bg_image = Label(self.frame1_left, image=self.bg)
            self.bg_image.place(relwidth=1, relheight=1)

            self.fg = ImageTk.PhotoImage(file="resources/da.jpg")
            self.fg_image = Label(self.frame2_right, image=self.fg)
            self.fg_image.place(x=80, y=230)

        self.userlogin = Label(self.right, text="You are logged in as:", font=('arial 20 bold'), fg='black')
        self.userlogin.place(x=10, y=20)

        self.Name = Label(self.right, text="Name: " + self.db_name, font=('arial 16'), fg='black')
        self.Name.place(x=10, y=80)

        self.Name = Label(self.right, text="Role:   " + self.db_designation, font=('arial 16'), fg='Red')
        self.Name.place(x=10, y=110)

    def destroyTop(self, top):
        top.destroy()

    # function to close the top window
    def logout(self, top):
        MsgBox = tkinter.messagebox.askquestion('Logout Application', 'Are you sure you want to logout?',
                                                icon='warning')
        if MsgBox == 'yes':
            # self.path = self.name + ".jpg"
            self.destroyTop(top)
            show_root()

    # function to open the appointment window    
    def appointment(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 appointment.py")
        elif sys.platform.startswith('win32'):
            # print(sys.platform)
            print("OS = win32")
            os.system("python appointment.py")

    # function to open the update window  
    def update(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 update.py")
        elif sys.platform.startswith('win32'):
            print("OS = win32")
            os.system("python update.py")

    def user(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 user.py")
        elif sys.platform.startswith('win32'):
            print("OS = win32")
            os.system("python user.py")

    # function to open the display window  
    def display(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 display.py")
        elif sys.platform.startswith('win32'):
            print("OS = win32")
            os.system("python display.py")

    def writeTofile(self):
        # Convert binary data to proper format and write it on Hard Disk
        print("writing")
        # with open(self.photoPath, 'wb') as file:
        # file.write(self.photo)

    def drawImage(self, top):
        # function takes image from database and saves it to disk. Then, it draws it on toplevel window
        sql_fetch_blob_query = "SELECT * from credentials where name = ?"
        c.execute(sql_fetch_blob_query, (self.id,))
        self.record = c.fetchall()
        for row in self.record:
            # print("Id = ", row[0], "Name = ", row[1])
            self.name = row[1]
            self.photo = row[4]

            self.photoPath = "resources/" + self.name + ".jpg"
            print(self.photoPath)
            # print("in draw image")
            # save file to directoryvs
            self.writeTofile()

            self.fileName = "resources/" + self.name + ".jpg"
            # print(type(self.fileName))
            # file_name = str(self.fileName)

            # draw image on canvas
            self.canvas = Canvas(self.left, width=120, height=120)
            self.canvas.pack()
            self.img = ImageTk.PhotoImage(Image.open(self.fileName))
            self.canvas.create_image(0, 0, anchor=NW, image=self.img)  # anchor specifies the position
            self.canvas.image = self.img

            # deleteProfilePic(self.fileName)
            os.remove(self.fileName)

    def aboutMaster(self):
        about = Toplevel()  # toplevel widget for new window
        about.geometry("480x320+0+0")
        about.title("About")
        about.iconphoto(False, PhotoImage(file="resources/icon.png"))

        self.loginLabel = Label(about,
                                text="\n\n\n\nThe application has been created using tkinter for GUI. \nThe data has been saved and accessed using SQLite3.\n\nMade by:",
                                font=('arial 11'), fg='black')
        self.loginLabel.pack()

        self.gitProfile = Label(about, text="Sandesh", fg='blue', font=('arial 11 underline'), cursor="hand2")
        self.gitProfile.place(x=180, y=180)
        self.gitProfile.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Sandesh-Uprety"))

        self.photo = PhotoImage(file="resources/github-100.png")
        self.photoimage = self.photo.subsample(3, 3)
        self.githubButton = Button(about, text='Open sourced on GitHub', image=self.photoimage, compound=LEFT,
                                   width=220, height=40, bg='grey', fg='white', command=lambda: webbrowser.open(
                'https://github.com/akshit6/hospital-management-system-using-tkinter'))
        self.githubButton.place(x=110, y=250)


# def deleteProfilePic(filepath):
#     print("Deleting: "+filepath)
#     os.remove(filepath)

root = Tk()  # making an object of class Tk
b = App(root)  # making the object of class tkinter class App with root as variable to constructor
root.bind('<Return>', b.login)  # making enter key as event to press login button


def hide_root():
    # Hide root window
    root.withdraw()


def show_root():
    # Show root window
    root.deiconify()


def exitRoot(root):
    MsgBox = tkinter.messagebox.askquestion('Exit Application', 'Do you really want to exit?', icon='warning')
    if MsgBox == 'yes':
        root.destroy()


root.mainloop()
