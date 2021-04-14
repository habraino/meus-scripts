from tkinter import *

class Palette(object):
    def __init__(self, root):
        self.canv = Canvas(root, width=200, height=200)
        self.canv.pack()

        self.canv.create_oval(10, 15, 180, 200, fill='yellow', tag='ball')

        self.frame = Frame(root, width=350, height=300)
        self.frame.pack()

        # color red
        self.lblRED = Label(self.frame, text='RED:')
        self.lblRED.place(x=10, y=15)
        self.edRED = Entry(self.frame, width=5)
        self.edRED.place(x=50, y=15)
        self.edRED.focus_force()

        # color green
        self.lblGREEN = Label(self.frame, text='GREEN:')
        self.lblGREEN.place(x=110, y=15)
        self.edGREEN = Entry(self.frame, width=5)
        self.edGREEN.place(x=170, y=15)

        # color blue
        self.lblBLUE = Label(self.frame, text='BLUE:')
        self.lblBLUE.place(x=220, y=15)
        self.edBLUE = Entry(self.frame, width=5)
        self.edBLUE.place(x=280, y=15)

        self.btnShow = Button(self.frame, text='SHOW', font=('times 14 bold'), command=self.complete)
        self.btnShow.place(x=130, y=100)

        self.rgb = Label(self.frame, text='', font=('times 15 bold'), fg='white')
        self.rgb.place(x=135, y=150)

    # fill the ball with color choosed
    def complete(self):
        if (self.edRED.get() == '' or self.edGREEN.get() == None or self.edBLUE.get() == None):
            self.rgb['text'] = 'VALUES INVALID'
        else:
            if (int(self.edRED.get()) > 255 or int(self.edGREEN.get()) > 255 or int(self.edBLUE.get()) > 255):
                self.rgb['text'] = 'Only values least or eguals that 255'

        self.color = "#%02x%02x%02x" % (int(self.edRED.get()),
                                            int(self.edGREEN.get()),
                                            int(self.edBLUE.get()))

        self.rgb['bg'] = self.color
        self.rgb['text'] = self.color
        self.edRED.focus_force()
        self.canv.delete('ball')
        self.canv.create_oval(10, 15, 200, 200, fill=self.color, tag='ball')

app = Tk()
app.title('Palette')
palette = Palette(app)
app.geometry("350x450+200+200")
app.resizable(False, False)
app.mainloop()

