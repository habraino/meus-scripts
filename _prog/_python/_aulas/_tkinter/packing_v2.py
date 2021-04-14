from tkinter import *

class Packing:

    def __init__(self, arg):

        self.fr1 = Frame(arg)
        self.fr2 = Frame(arg)
        self.fr3 = Frame(arg)
        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()

        Button(self.fr1, text='B3').pack(side=RIGHT)
        Button(self.fr1, text='B2').pack(side=RIGHT)
        Button(self.fr1, text='B1').pack(side=RIGHT)

        self.bt4 = Button(self.fr2, text='B5')
        self.bt5 = Button(self.fr2, text='B4')
        self.bt6 = Button(self.fr3, text='B6')
        self.bt6.pack(side=LEFT)
        self.bt5.pack(side=LEFT)
        self.bt4.pack()


app = Tk()
Packing(app)
app.title('Packing')
app.geometry("250x200")
app.mainloop()