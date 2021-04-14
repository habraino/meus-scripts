from tkinter import *

class Window:

    def __init__(self, arg):

        self.fr = Frame(arg)
        self.fr.pack()

        self.lb = Label(self.fr, text='Click on button for stay red!', font=            ('Verdana 12'))
        self.lb.pack()

        self.bt = Button(self.fr, text='Click', relief='ridge', width=26, height=2, bg='green')
        self.bt.bind("<Return>", self.change_color)
        self.bt.bind("<ButtonRelease>", self.change_color)
        self.bt.bind("<FocusIn>", self.evento1)
        self.bt.bind("<FocusOut>", self.evento2)
        self.bt.pack()

        self.bt2 = Button(self.fr, text='Click', relief='ridge', width=26, height=2, bg='green')
        self.bt2.bind("<FocusIn>", self.evento3)
        self.bt2.bind("<FocusOut>", self.evento4)
        self.bt2.pack()

    def change_color(self, event):
        if self.bt['bg'] == 'green':
            self.bt['bg'] = 'red'
            self.lb['text'] = 'Click on button for stay green!'
        else:
            self.bt['bg'] = 'green'
            self.lb['text'] = 'Click on button for stay red!'
    
    def evento1(self, event): 
        self.bt['relief'] = GROOVE
    def evento2(self, event): 
        self.bt['relief'] = RIDGE

    def evento3(self, event): 
        self.bt2['relief'] = GROOVE
    def evento4(self, event): 
        self.bt2['relief'] = RIDGE

app = Tk()
Window(app)
app.title('Event_v1')
app.geometry("350x250")
app.mainloop()


