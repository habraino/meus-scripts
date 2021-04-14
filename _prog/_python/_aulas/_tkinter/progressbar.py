from tkinter import *
from tkinter import ttk

class Treino:
    def __init__(self, master):
        self.frame = Frame(master, width=450, height=350, bg='red')
        self.frame.pack(fill='both')
        
        self.pro = ttk.Progressbar(self.frame, mode='determinate', takefocus=True, orient='horizontal')
        self.pro.start(10)
        self.pro.pack(fill='x')


app = Tk()
Treino(app)
app.title('Test with Progressbar')
app.geometry("450x350")
app.mainloop()


