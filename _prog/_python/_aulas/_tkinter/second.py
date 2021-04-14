from tkinter import *

class Janela:

    def __init__(self, arg):

        self.fr1 = Frame(arg)
        self.fr1.pack()

        self.bt1 = Button(self.fr1, text='Hi', height=3, bg='green', font=('Verdana     16 italic'))
        self.bt1.pack()

        self.bt2 = Button(self.fr1, text='Bye!', width=13, bg='red', fg='yellow', font=         ('Verdana 16'))
        self.bt2.pack()

app = Tk()        
Janela(app)
app.geometry("250x200")
app.mainloop()

