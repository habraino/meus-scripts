from tkinter import *
from tkinter import messagebox as ms


class Login:
    def __init__(self, master):


        self.frame = Frame(master, width=450, height=300, bg='#0FF0FF', bd=5, relief='raised')
        self.frame.pack(fill='x')

        self.label_address = Label(self.frame, text='Address:', bg='#0FF0FF', font=      ('verdana 12 bold'), justify='center')
        self.label_address.pack()

        self.entry_adrress = Entry(self.frame, width=30, font=("calibri 18 bold")
        self.entry_adrress.insert(0, 'example123@gmail.com')
        self.entry_adrress.pack()

        self.label_password = Label(self.frame, text='Password:', bg='#0FF0FF', font=      ('verdana 12 bold'), justify='center')
        self.label_password.pack()

        self.entry_password = Entry(self.frame, width=30, show='*', font=("calibri 18 bold"))
        self.entry_password.insert(0, '********')
        self.entry_password.pack()

        self.button = Button(application, width=12, text='Login', font=('calibri 12 bold'), command=self.enter)
        self.button.place(x=160, y=150)

        self.msg = Label(application, text='', bg="#0FF0FF", font=('calibri 14       italic'))
        self.msg.place(x=170, y=220)

    
    def enter(self):
        self.ad = self.entry_adrress.get()
        self.sn = self.entry_password.get()

        if self.ad == "brayenstrong78@gmail.com" and self.sn == "programador":
            self.msg.config(fg='green', text='Login successfully!')
        else:
            self.msg.config(fg='red', text='Login error!')

application = Tk()
Login(application)

application.title("Exemple of Login")
application.config(bg="#0FF0FF")
application.geometry("450x300")
application.resizable(False, False)
application.mainloop()