from tkinter import *
import mysql.connector

class Update(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.createGUI()

    def createGUI(self):
        self.frame = Frame(master=window, width=330, height=400)
        self.frame.pack()

        self.title = Label(master=self.frame, text="UPDATE EMPLOYEE")
        self.title.place(x=100, y=0)

        self.name = Label(master=self.frame, text="Employee Name")
        self.name.place(x=0, y=50)
        self.nameEntry = Entry(master=self.frame)
        self.nameEntry.place(x=100,y=50)

        self.post = Label(master=self.frame,text="Employee Post")
        self.post.place(x=0, y=75)
        self.postEntry = Entry(master=self.frame)
        self.postEntry.place(x=100,y=75)

        self.searchB = Button(master=self.frame,text="Search",command=self.search)
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

        self.phone = Label(master=self.frame,text="Phone No.")
        self.phone.place(x=0,y=190)
        self.phoneEntry = Entry(master=self.frame)
        self.phoneEntry.place(x=100,y=190)

        self.email = Label(master=self.frame,text="Email")
        self.email.place(x=0,y=215)
        self.emailEntry = Entry(master=self.frame)
        self.emailEntry.place(x=100,y=215)

        self.address = Label(master=self.frame,text="Address")
        self.address.place(x=0,y=240)
        self.addressEntry = Entry(master=self.frame)
        self.addressEntry.place(x=100,y=240)

        self.updateB = Button(master=self.frame,text="Update",command=self.update)
        self.updateB.place(x=70,y=300)

        self.deleteB = Button(master=self.frame,text="Delete",command=self.delete)
        self.deleteB.place(x=10,y=300)

        self.homeB = Button(master=self.frame,text="Home",command=self.home)
        self.homeB.place(x=220,y=350)

        self.resetB = Button(master=self.frame,text="Reset",command=self.reset)
        self.resetB.place(x=280,y=350)

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
            
            sql="select * from employee where empName= %s and empPost= %s"
            values=(self.nameEntry.get(),self.postEntry.get())
            c.execute(sql,values)
            result=c.fetchall()

            for row in result:
                id=row[0]
                name=row[1]
                phone=row[2]
                email=row[3]
                address=row[8]

            self.idEntry.insert(0,str(id))
            self.name2Entry.insert(0,name)
            self.phoneEntry.insert(0,phone)
            self.emailEntry.insert(0,email)
            self.addressEntry.insert(0,address)
        
        except:
            print("Connection Error")
        finally:
            if con:
                con.close()

    def update(self):
        try:
            con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hrms"
            )
            print("Connection Successfull")
            c=con.cursor()

            id=self.idEntry.get()
            name=self.name2Entry.get()
            phone=self.phoneEntry.get()
            email=self.emailEntry.get()
            address=self.addressEntry.get()

            sql="update employee set empName=%s,phoneNo=%s,email=%s,empAddress=%s where empID=%s"
            values=(name,phone,email,address,id)

            try:
                c.execute(sql,values)
                con.commit()
                print("Data Updated Successfully!")
            except:
                con.rollback()

        except:
            print("Connection Error")
        finally:
            if con:
                con.close()

    def delete(self):
        try:
            con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hrms"
            )
            print("Connection Successfull")
            c=con.cursor()

            id=self.idEntry.get()
            name=self.name2Entry.get()
            sql="delete from employee where empID=%s and empName=%s"
            values=(id,name)
            try:
                c.execute(sql,values)
                con.commit()
                print("Data Deleted Successfully!")
            except:
                con.rollback()
            
        except:
            print("Connection Error")
        finally:
            if con:
                con.close()

    def reset(self):
        self.nameEntry.delete(0,END)
        self.postEntry.delete(0,END)
        self.idEntry.delete(0,END)
        self.name2Entry.delete(0,END)
        self.phoneEntry.delete(0,END)
        self.emailEntry.delete(0,END)
        self.addressEntry.delete(0,END)

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
window.title("Update Data")
u=Update(window)
window.mainloop() #displays main