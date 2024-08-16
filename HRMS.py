from tkinter import *
class HRMS(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.createGUI()

    def createGUI(self):
        self.frame = Frame(master=window, width=300, height=400)
        self.frame.pack()

        self.title = Label(master=self.frame, text="HR MANAGEMENT SYSTEM")
        self.title.place(x=85, y=0)

        self.newB = Button(master=self.frame,text="New Employee",command=self.newEmp)
        self.newB.place(x=100,y=50)

        self.searchB = Button(master=self.frame,text="Search Employee",command=self.searchEmp)
        self.searchB.place(x=95,y=100)

        self.updateB = Button(master=self.frame,text="Update Employee",command=self.updateEmp)
        self.updateB.place(x=95,y=150)

        self.salaryB = Button(master=self.frame,text="Salary",command=self.salary)
        self.salaryB.place(x=115,y=200)

        self.skillsB = Button(master=self.frame,text="Skills",command=self.skillsEmp)
        self.skillsB.place(x=117,y=250)

        self.loginB = Button(master=self.frame,text="Login",command=self.login)
        self.loginB.place(x=115,y=300)

        self.logoutB = Button(master=self.frame,text="Logout",command=self.logout)
        self.logoutB.place(x=110,y=350)

    def newEmp(self):
        hide()
        import Employee
        Employee.show()
    
    def searchEmp(self):
        hide()
        import Search
        Search.show()

    def updateEmp(self):
        hide()
        import Update
        Update.show()

    def salary(self):
        hide()
        import Salary
        Salary.show()

    def skillsEmp(self):
        hide()
        import Skills
        Skills.show()

    def login(self):
        hide()
        import Login
        Login.show()
    
    def logout(self):
        drop()

def show():
    window.deiconify()

def hide():
    window.withdraw()

def drop():
    window.destroy()

window=Tk() #main container object
window.title("HRMS")
home=HRMS(window)
window.mainloop() #displays main window