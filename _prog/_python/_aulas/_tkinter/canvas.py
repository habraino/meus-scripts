from tkinter import *

class AprendendoCanva:
    def __init__(self, root):
        self.canva1 = Canvas(root, width=500, height=300, bd=5, bg='blue', cursor='X_cursor')
        self.canva1.bind('<Left>', self.moveLeft)
        self.canva1.bind('<Right>', self.moveRight)
        self.canva1.bind('<Up>', self.moveUp)
        self.canva1.bind('<Down>', self.moveDown)
        self.canva1.focus_force()
        self.canva1.pack(side=LEFT)

        self.canva1.create_line(300, 180, 300, 192, tag='line', fill='red', width=100)
        
    def moveLeft(self, event):
        self.canva1.move('line', -10, 0)

    def moveRight(self, event):
        self.canva1.move('line', 10, 0)
    
    def moveUp(self, event):
        self.canva1.move('line', 0, -10)

    def moveDown(self, event):
        self.canva1.move('line', 0, 10)

app = Tk()
AprendendoCanva(app)
app.mainloop()

