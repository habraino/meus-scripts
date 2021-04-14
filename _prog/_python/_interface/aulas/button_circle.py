import tkinter as tk
import itertools as it

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Button Cycle')

        self.style1 = {'fg':'red', 'bg':'black', 'activebackground':'gold', 'activeforeground':'green'}
        self.style2 = {'fg':'yellow', 'bg':'grey', 'activebackground':'gold', 'activeforeground':'green'}
        self.style_cycle = it.cycle([self.style1, self.style2])

        self.button = tk.Button(self, text='style switch', command=self.style_switch)
        self.button.pack(padx=50, pady=50)

    def style_switch(self):
        style = next(self.style_cycle)
        self.button.configure(**style)

if __name__ == '__main__':
    window = Window()
    window.mainloop()



