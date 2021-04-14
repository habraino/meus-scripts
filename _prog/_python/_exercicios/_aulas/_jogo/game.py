from tkinter import *
from time import strftime


class MyGame:
    def __init__(self, root):

        # variables
        self.var = IntVar()
        self.var1 = StringVar()

        # Frames
        self.fr_main = Frame(root, bg="#FFFFFF", width=600, height=580, bd=0, relief="raised", highlightcolor="#000000")
        self.fr_main.pack(pady=15)

        self.fr_clock = Frame(self.fr_main, width=550, height=50, bg="#008080", relief='ridge', bd=3)
        self.fr_clock.pack(fill='x')

        self.fr_field = Frame(self.fr_main, width=550, height=300, relief='ridge', bg='#008080', bd=3)
        self.fr_field.pack(fill='x', pady=10)

        self.fr_settings = Frame(self.fr_main, width=550, height=220, relief='ridge', bg='#999999', bd=3)
        self.fr_settings.pack(fill='x', pady=3)

        # Colck the game
        #self.tac()
        self.lbl_clock = Label(self.fr_clock, bg='#008080', text="00:23:45", font=('Courier 10 New', '20', 'bold'))
        self.clock()
        self.lbl_clock.place(x=390, y=5)

        # Buttons of the game
        self.bt1 = Button(self.fr_field, width=4, fg='green', bg='#800000', text='X', font=('times', '50', 'bold'))
        self.bt1.grid(row=0, column=0, padx=11)
        self.bt2 = Button(self.fr_field, width=4, fg='#000080', bg='#800000', text='O', font=('times', '50', 'bold'))
        self.bt2.grid(row=0, column=1, padx=9)
        self.bt3 = Button(self.fr_field, width=4, fg='green', bg='#800000', text='X', font=('times', '50', 'bold'))
        self.bt3.grid(row=0, column=2, padx=9, pady=5)

        self.bt4 = Button(self.fr_field, width=4, fg='#000080', bg='#800000', text='O', font=('times', '50', 'bold'))
        self.bt4.grid(row=1, column=0)
        self.bt5 = Button(self.fr_field, width=4, fg='green', bg='#800000', text='X', font=('times', '50', 'bold'))
        self.bt5.grid(row=1, column=1, padx=9)
        self.bt6 = Button(self.fr_field, width=4, fg='#000080', bg='#800000', text='O', font=('times', '50', 'bold'))
        self.bt6.grid(row=1, column=2, padx=9, pady=5)

        self.bt7 = Button(self.fr_field, width=4, fg='green', bg='#800000', text='X', font=('times', '50', 'bold'))
        self.bt7.grid(row=2, column=0)
        self.bt8 = Button(self.fr_field, width=4, fg='#000080', bg='#800000', text='O', font=('times', '50', 'bold'))
        self.bt8.grid(row=2, column=1, padx=9)
        self.bt9 = Button(self.fr_field, width=4, fg='#000080', bg='#800000', text='O', font=('times', '50', 'bold'))
        self.bt9.grid(row=2, column=2, padx=9, pady=5)

        # Settings of game
        self.lbl_player = Label(self.fr_settings, fg='#000080', text='Set Player', font=('Courier 10 New', '14', 'bold'), bg="#999999")
        self.lbl_player.place(x=5, y= 10)

        self.rb_X = Radiobutton(self.fr_settings, text='X', font=('Courier 10 New', '12', 'bold'), bg="#999999", bd=0, variable=self.var, value=1)
        self.rb_X.place(x=5, y=40)

        self.rb_O = Radiobutton(self.fr_settings, text='O', font=('Courier 10 New', '12', 'bold'), bg="#999999", bd=0, variable=self.var, value=2)
        self.rb_O.place(x=60, y=40)

        self.bt_start = Button(self.fr_settings, text='START', font=('Courier 10 New', '20', 'bold'), bg='#999999')
        self.bt_start.place(x=210, y=80)

        self.bt_info = Button(self.fr_settings, text='?', font=('Courier 10 New', '20', 'bold'), bg='#999999')
        self.bt_info.place(x=480, y=80)

    # function with manipule hours
    def clock(self):
        self.lbl_clock['text'] = strftime("%H:%M:%S")
        self.lbl_clock.after(1000, self.clock)
    
    def play(self):
        pass
    
    
    

app = Tk()
toplevel = MyGame(app)
app.title('Game of OldWoman')
app.geometry("600x550")
app.resizable(False, False)
app.config(bg='#FFFFFF')
app.mainloop()
