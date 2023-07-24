# update the appointments
# import modules
from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)

        # creating the format in master
        self.left = Frame(master, width=800, height=720, bg='lightblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        # self.heading = Label(self.left, text="Techmirtz Hospital Appointment Application", font=('arial 25 bold'), fg='black', bg='lightblue')
        # self.heading.place(x=5, y=0)

        # patient's name
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.name.place(x=100, y=100)

        # age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.age.place(x=100, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.gender.place(x=100, y=180)

        # location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.location.place(x=100, y=220)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.time.place(x=100, y=260)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.phone.place(x=100, y=300)

        # Enteries for all labels==============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=380, y=110)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=380, y=150)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=380, y=190)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=380, y=230)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=380, y=270)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=380, y=310)



        # heading label
        self.heading = Label(master, text="Update Appointments", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name
        self.name = Label(master, text="Enter Patient's Name and Search", font=('arial 15 bold'))
        self.name.place(x=310, y=70)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=600, y=105)

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)

    # function to search
    def search_db(self):
        em = []
        self.input = self.name_ent.get()

        # execute sql 
        sql = "SELECT * FROM appointments WHERE name=?"
        self.res = c.execute(sql, (self.input,))
        # print(type(self.res))
        # print("hii " , self.res)
        self.res = self.res.fetchone()
        print(self.res)
        if (self.res == None):
            tkinter.messagebox.showwarning("Warning","No such record in database ")
            return
        self.row = self.res[0]
        self.name1 = self.res[1]
        self.age = self.res[2]
        self.gender = self.res[3]
        self.location = self.res[4]
        self.time = self.res[6]
        self.phone = self.res[5]

        self.age_ent.insert(0,self.age)
        self.gender_ent.insert(0,self.gender)
        self.location_ent.insert(0,self.location)
        self.time_ent.insert(0,self.time)
        self.phone_ent.insert(0,self.phone)
        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update


    
    
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.name_ent.get() #updated name

        try:
            self.var2 = int(self.age_ent.get())
        except ValueError:
            tkinter.messagebox.showwarning("Warning","Please fill up age correctly")
        self.var3 = self.gender_ent.get() #updated gender
        self.var4 = self.location_ent.get() #updated location
        self.var5 = self.time_ent.get() #updated phone
        self.var6 = self.phone_ent.get() #updated time
        if self.var1 == '' or self.var2 == '' or self.var3 == '' or self.var4 == '' or self.var5 == '' or self.var6 == '':
            tkinter.messagebox.showwarning("Warning","Please fill up all the boxes")

        elif (self.var3!="male"  and self.var3 !="female"):     #condition for gender
            tkinter.messagebox.showwarning("Warning","Please fill up a valid gender")

        elif (self.var2>105 or self.var2<0):                    #condition for age
            tkinter.messagebox.showwarning("Warning","Please fill up a valid age")

        elif (not(self.var6).isdecimal() or len(self.var6)==1):      #condition for mobile number
            tkinter.messagebox.showwarning("Warning","Please fill up a valid mobile number")

        else:

            query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
            c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var6, self.var5, self.name_ent.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
        self.name_ent.delete(0, 50)
        self.age_ent.delete(0, 50)
        self.location_ent.delete(0, 50)
        self.gender_ent.delete(0, 50)
        self.phone_ent.delete(0, 50)
        self.time_ent.delete(0, 50)
    
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.name_ent.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.name_ent.delete(0,50)
        self.age_ent.delete(0,50)
        self.location_ent.delete(0,50)
        self.gender_ent.delete(0,50)
        self.phone_ent.delete(0,50)
        self.time_ent.delete(0,50)


#creating the object
root = tk.Tk()
b = App(root)
root.geometry("1000x620+0+0")
root.resizable(False, False)
root.title("Hospital management system")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

# end the loop
root.mainloop()
