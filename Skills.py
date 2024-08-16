from tkinter import *
import mysql.connector

class Skills(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.createGUI()

    def createGUI(self):
        self.frame = Frame(master=window, width=330, height=170)
        self.frame.pack()

        self.title = Label(master=self.frame, text="EMPLOYEE SKILLS")
        self.title.place(x=100, y=0)

        self.post = Label(master=self.frame,text="Employee Post")
        self.post.place(x=0, y=50)
        self.postEntry = Entry(master=self.frame)
        self.postEntry.place(x=100,y=50)

        self.searchB = Button(master=self.frame,text="Analyse",command=self.search)
        self.searchB.place(x=270,y=45)

        self.homeB = Button(master=self.frame,text="Home",command=self.home)
        self.homeB.place(x=220,y=120)

        self.resetB = Button(master=self.frame,text="Reset",command=self.reset)
        self.resetB.place(x=280,y=120)

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

            post=self.postEntry.get()

            if (post=='CHRO'):
                sql="select * from employee where empPost='CHRO'"
                c.execute(sql)
                result=c.fetchall()
            elif (post=='Manager'):
                sql="select * from employee where empPost='Manager'"
                c.execute(sql)
                result=c.fetchall()
            elif(post=='HR Specialist'):
                sql="select * from employee where empPost='HR Specialist'"
                c.execute(sql)
                result=c.fetchall()
            elif(post=='HR Director'):
                sql="select * from employee where empPost='HR Director'"
                c.execute(sql)
                result=c.fetchall()
            elif(post=='HR Generalist'):
                sql="select * from employee where empPost='HR Generalist'"
                c.execute(sql)
                result=c.fetchall()
            elif(post=='HR Coordinator'):
                sql="select * from employee where empPost='HR Coordinator'"
                c.execute(sql)
                result=c.fetchall()
            elif(post=='Recruiter'):
                sql="select * from employee where empPost='Recruiter'"
                c.execute(sql)
                result=c.fetchall()
            else:
                print("Enter Valid Post")

            window2=Tk()
            window2.title("Employee Skills")

            frame2 = Frame(master=window2, width=330, height=150)
            frame2.pack()

            head = Label(master=frame2)
            head.pack()
            head["text"]=("ID   Name    Post    Skills")

            for row in result:
                lbl = Label(master=frame2)
                lbl.pack()
                lbl["text"]=("%d    %s    %s    %s"%(row[0],row[1],row[5],row[6]))
                print("%d    %s    %s    %s"%(row[0],row[1],row[5],row[6]))

            window2.mainloop()
        except:
            print("Connection Error")
        finally:
            if con:
                con.close()

    def reset(self):
        self.postEntry.delete(0,END)

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
window.title("Employee Skills")
s=Skills(window)
window.mainloop() #displays main