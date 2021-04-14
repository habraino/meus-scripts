from tkinter import *

class AutoCADE(object):
    def __init__(self, root):
        self.canv = Canvas(root, width=500, height=600, bg='#beff8c', cursor='plus')
        self.canv.bind('<1>', self.draw)
        self.canv.pack()

    def draw(self, event):
        self.x_point = self.canv.winfo_rootx()
        self.y_point = self.canv.winfo_rooty()

        self.x_abs = self.canv.winfo_pointerx()
        self.y_abs = self.canv.winfo_pointery()

        try:
            P = (self.x_abs - self.x_point, self.y_abs - self.y_point)
            self.canv.create_line(self.ultimo_P, P)
            self.ultimo_P = P
        except:
            self.ultimo_P = (self.x_abs - self.x_point, self.y_abs - self.y_point)


app = Tk()
auto = AutoCADE(app)
app.title('AutoCADE')
app.geometry('500x600')
app.mainloop()

