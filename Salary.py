from tkinter import *
import mysql.connector

class Salary(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.createGUI()

    def createGUI(self):
        self.frame = Frame(master=window, width=400, height=330)
        self.frame.pack()

        self.title = Label(master=self.frame, text="EMPLOYEE SALARY")
        self.title.place(x=150, y=0)

        self.name = Label(master=self.frame, text="Employee Name")
        self.name.place(x=0, y=50)
        self.nameEntry = Entry(master=self.frame)
        self.nameEntry.place(x=100,y=50)

        self.post = Label(master=self.frame,text="Employee Post")
        self.post.place(x=0, y=75)
        self.postEntry = Entry(master=self.frame)
        self.postEntry.place(x=100,y=75)

        self.searchB = Button(master=self.frame,text="Evaluate",command=self.search)
        self.searchB.place(x=270,y=70)

        self.details = Label(master=self.frame, text="Details:")
        self.details.place(x=0,y=120)

        self.id = Label(master=self.frame,text="Employee ID")
        self.id.place(x=0,y=140)
        self.idEntry = Entry(master=self.frame)
        self.idEntry.place(x=100,y=140)

        self.name2 = Label(master=self.frame, text="Employee Name")
        self.name2.place(x=0,y=165)
        self.name2Entry = Entry(master=self.frame)
        self.name2Entry.place(x=100,y=165)

        self.post2 = Label(master=self.frame,text="Employee Post")
        self.post2.place(x=0,y=190)
        self.post2Entry = Entry(master=self.frame)
        self.post2Entry.place(x=100,y=190)

        self.salary = Label(master=self.frame,text="Employee Salary")
        self.salary.place(x=0,y=215)
        self.salaryEntry = Entry(master=self.frame)
        self.salaryEntry.place(x=100,y=215)

        self.salaryB = Button(master=self.frame,text="Generate Net Salary",command=self.salaryGenerator)
        self.salaryB.place(x=270,y=210)

        self.homeB = Button(master=self.frame,text="Home",command=self.home)
        self.homeB.place(x=270,y=280)

        self.resetB = Button(master=self.frame,text="Reset",command=self.reset)
        self.resetB.place(x=330,y=280)

    def search(self):
        try:
            con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hrms"
            )
            print("Connection Successfull")
            c=con.cursor()
            
            sql="select * from employee where empName=%s and empPost=%s"
            values=(self.nameEntry.get(),self.postEntry.get())
            c.execute(sql,values)
            result=c.fetchall()
            for row in result:
                id=row[0]
                name=row[1]
                post=row[5]
                salary=row[7]

            self.idEntry.insert(0,str(id))
            self.name2Entry.insert(0,name)
            self.post2Entry.insert(0,post)
            self.salaryEntry.insert(0,str(salary))
        
        except:
            print("Connection Error")
        finally:
            if con:
                con.close()

    def salaryGenerator(self):

        window2=Tk()
        window2.title("Salary Generator")

        frame = Frame(master=window2, width=200, height=150)
        frame.pack()

        title = Label(master=frame, text="SALARY GENERATOR")
        title.place(x=50, y=0)

        idlbl = Label(master=frame, text="Employee ID:")
        idlbl.place(x=0, y=50)
        id=Label(master=frame)
        id.place(x=100,y=50)
        id["text"]=self.idEntry.get()

        namelbl = Label(master=frame, text="Employee Name:")
        namelbl.place(x=0, y=75)
        name=Label(master=frame)
        name.place(x=100,y=75)
        name["text"]=self.name2Entry.get()
       

        postlbl = Label(master=frame,text="Employee Post:")
        postlbl.place(x=0, y=100)
        post=Label(master=frame)
        post.place(x=100,y=100)
        post["text"]=self.post2Entry.get()        

        Bsalary=float(self.salaryEntry.get())

        if(self.post2Entry.get()=='CHRO'):
            TA=1500
            EA=500
            CA=1000
        elif(self.post2Entry.get()=='Manager'):
            TA=1300
            EA=200
            CA=750
        elif(self.post2Entry.get()=='HR Specialist'):
            TA=1000
            EA=100
            CA=500
        else:
            TA=700
            EA=0
            CA=250
        
        HRA=0.25*Bsalary
        NetSalary=Bsalary+HRA+TA+EA+CA

        salarylbl = Label(master=frame,text="Net Salary:")
        salarylbl.place(x=0,y=125)
        salary=Label(master=frame)
        salary.place(x=100,y=125)
        salary["text"]=NetSalary

        window2.mainloop()

    def reset(self):
        self.nameEntry.delete(0,END)
        self.postEntry.delete(0,END)
        self.idEntry.delete(0,END)
        self.name2Entry.delete(0,END)
        self.post2Entry.delete(0,END)
        self.salaryEntry.delete(0,END)

    def home(self):
        hide()
        import HRMS
        HRMS.show()

def show():
    window.deiconify()

def hide():
    window.withdraw()

def drop():
    window.destroy()

window=Tk() #main container object
window.title("Salary")
s=Salary(window)
window.mainloop() #displays main