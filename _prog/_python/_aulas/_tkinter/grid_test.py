from tkinter import *

class Window:
    def __init__(self, master):
        self.fr = Frame(master, width=400, height=450)
        self.fr.pack()
        
        self.bt1 = Button(self.fr, text="B1", font=('verdana 15 bold'))
        self.bt1.grid(row=0, column=0)

        self.bt2 = Button(self.fr, text="B2", font=('verdana 15 bold'))        
        self.bt2.grid(row=0, column=1)

        self.bt3 = Button(self.fr, text="B3", font=('verdana 15 bold'))
        self.bt3.grid(row=0, column=2)

        self.bt4 = Button(self.fr, text="B4", font=('verdana 15 bold'))        
        self.bt4.grid(row=0, column=3)

        self.bt5 = Button(self.fr, text="B5", font=('verdana 15 bold'))
        self.bt5.grid(row=1, column=0)

        self.bt6 = Button(self.fr, text="B6", font=('verdana 15 bold'))
        self.bt6.grid(row=1, column=3)

        self.bt7 = Button(self.fr, text="B7", font=('verdana 15 bold'))
        self.bt7.grid(row=2, column=0)

        self.bt8 = Button(self.fr, text="B8", font=('verdana 15 bold'))
        self.bt8.grid(row=2, column=3)

        self.bt9 = Button(self.fr, text="B1", font=('verdana 15 bold'))
        self.bt9.grid(row=3, column=0)

        self.bt10 = Button(self.fr, text="B2", font=('verdana 15 bold'))        
        self.bt10.grid(row=3, column=1)

        self.bt11 = Button(self.fr, text="B3", font=('verdana 15 bold'))
        self.bt11.grid(row=3, column=2)

        self.bt12 = Button(self.fr, text="B4", font=('verdana 15 bold'))        
        self.bt12.grid(row=3, column=3)

        self.bt13 = Button(self.fr, text="B1", font=('verdana 15 bold'))
        self.bt13.grid(row=4, column=1)

        self.bt14 = Button(self.fr, text="B2", font=('verdana 15 bold'))        
        self.bt14.grid(row=4, column=2)

        self.bt15 = Button(self.fr, text="B3", font=('verdana 15 bold'))
        self.bt15.grid(row=5, column=1)

        self.bt16 = Button(self.fr, text="B4", font=('verdana 15 bold'))        
        self.bt16.grid(row=5, column=2)

        self.bt17 = Button(self.fr, text="B5", font=('verdana 15 bold'))
        self.bt17.grid(row=6, column=1)

        self.bt18 = Button(self.fr, text="B6", font=('verdana 15 bold'))        
        self.bt18.grid(row=6, column=2)

app = Tk()
Window(app)
app.title('Teste with grid')
app.geometry('550x400+200+100')
app.mainloop()
