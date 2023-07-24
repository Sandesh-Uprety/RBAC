# import modules

from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
import tkinter.messagebox
import sqlite3
import pyttsx3

#connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []
al = []
bl = []
cl = []

sql = "SELECT * FROM appointments ORDER BY scheduled_time ASC"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    a = r[2]
    b = r[3]
    c = r[4]
    print(a,b,c)
    number.append(ids)
    patients.append(name)
    al.append(a)
    bl.append(b)
    cl.append(c)



# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        
        # heading
        self.heading = Label(master, text="Appointments", font=('arial 40 bold'), fg='green')
        self.heading.place(x=270, y=0)

        # button to change patients
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=360, y=500)

        # empty text labels to later config

        self.tframe = Frame(master, bg = 'grey')
        self.tframe.place(x= 250, y=80, width=400, height=400)

        self.at = Label(self.tframe, text="Appointment Time", font=('arial 15 bold'), bg='grey')
        self.at.grid(sticky = 'w', pady = 20)

        self.pname = Label(self.tframe, text="Patients Name", font=('arial 15 bold'),bg='grey')
        self.pname.grid(sticky = 'w', pady = 20)

        self.age = Label(self.tframe, text="Age", font=('arial 15 bold'), bg='grey')
        self.age.grid(sticky = 'w', pady = 20)

        self.gen = Label(self.tframe, text="Gender", font=('arial 15 bold'), bg='grey')
        self.gen.grid(sticky = 'w', pady = 20)

        self.addr = Label(self.tframe, text="Address", font=('arial 15 bold'), bg='grey')
        self.addr.grid(sticky = 'w', pady = 20)

        self.n = Label(self.tframe, text="", font=('arial 15'), bg='grey')
        self.n.grid(row = 0, column = 1, sticky='w', pady = 20, padx = 30)

        self.pname = Label(self.tframe, text="", font=('arial 15'), bg='grey')
        self.pname.grid(row = 1, column = 1, sticky='w',pady = 20, padx = 30)

        self.page = Label(self.tframe, text="", font=('arial 15'), bg='grey')
        self.page.grid(row = 2, column = 1, sticky='w', pady = 20, padx = 30)

        self.pgen = Label(self.tframe, text="", font=('arial 15'), bg='grey')
        self.pgen.grid(row = 3, column = 1,sticky='w', pady = 20, padx = 30)

        self.paddr = Label(self.tframe, text="", font=('arial 15'), bg='grey')
        self.paddr.grid(row = 4, column = 1,sticky='w', pady = 20, padx = 30)

        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        self.page.config(text=str(al[self.x]))
        self.pgen.config(text=str(bl[self.x]))
        self.paddr.config(text=str(cl[self.x]))

        self.x +=1

    # function to speak the text and update the text
    def func(self):
        try:
            self.n.config(text=str(number[self.x]))
            self.pname.config(text=str(patients[self.x]))
            self.page.config(text=str(al[self.x]))
            self.pgen.config(text=str(bl[self.x]))
            self.paddr.config(text=str(cl[self.x]))
        except IndexError:
            print("The appointment list is completed :")
            tkinter.messagebox.showinfo("completed :","The appointment list is  completed")
        try:
            pass
            # engine = pyttsx3.init('sapi5')
            # voices = engine.getProperty('voices')
            # rate = engine.getProperty('rate')
            # engine.setProperty('rate', rate-50)
            # engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
            # engine.runAndWait()
        except:
            print("An Error occured in text to speech :")
        self.x += 1

root = Tk()
b = Application(root)
root.geometry("900x568")
root.resizable(False, False)
root.title("Appointments List")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))
root.mainloop()