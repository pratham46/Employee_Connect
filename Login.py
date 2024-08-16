from tkinter import *
import mysql.connector

class Login(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.createGUI()

    def createGUI(self):
        self.frame = Frame(master=window, width=250, height=170)
        self.frame.pack()

        self.title = Label(master=self.frame, text="LOGIN")
        self.title.place(x=100, y=0)

        self.userIdLabel = Label(master=self.frame, text="Admin ID")
        self.userIdLabel.place(x=0, y=50)
        self.userIdEntry = Entry(master=self.frame)
        self.userIdEntry.place(x=70,y=50)

        self.passLabel = Label(master=self.frame,text="Password")
        self.passLabel.place(x=0, y=75)
        self.passEntry = Entry(master=self.frame,show="*")
        self.passEntry.place(x=70,y=75)

        self.loginB = Button(master=self.frame,text="Login",command=self.connection)
        self.loginB.place(x=100,y=130)

        self.resetB = Button(master=self.frame,text="Reset",command=self.reset)
        self.resetB.place(x=150,y=130)

    def connection(self):
        try:
            con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hrms"
            )
            print("Connection Successfull")
            c=con.cursor()
            sql="select * from login"
            c.execute(sql)
            result=c.fetchall()
            for row in result:
                username=row[1]
                password=row[2]
            self.login(username,password)
        except:
            print("Connection Error")
        finally:
            if con:
                con.close()

    def login(self,username,password):

        uname1=username
        pword1=password
    
        uname=self.userIdEntry.get()
        pword=self.passEntry.get()

        if(uname==uname1 and pword==pword1):
            print("Login Successfull")
            hide()
            import HRMS
            HRMS.show()
        elif(uname=="" and pword==""):
            print("Please fill the credentials")
        elif(uname=="" and pword==pword1):
            print("Please enter your Username")
        elif(uname==uname1 and pword==""):
            print("Please enter your Password")
        else:
            print("Invalid credentials")

    def reset(self):
        self.userIdEntry.delete(0,END)
        self.passEntry.delete(0,END)

def show():
    window.deiconify()

def hide():
    window.withdraw()

def drop():
    window.destroy()

window=Tk() #main container object
window.title("Login")
l=Login(window)
window.mainloop() #displays main window