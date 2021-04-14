from tkinter import *

class Janela:

    def __init__(self, arg):

        self.frame = Frame(arg)
        self.frame.pack()

        self.button = Button(self.frame, text='Hi!', bg='green')
        self.button.pack()

app = Tk()
Janela(app)
app.geometry("250x200")
app.mainloop()
