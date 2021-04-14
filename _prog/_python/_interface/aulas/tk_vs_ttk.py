import tkinter as tk
import tkinter.ttk as ttk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('TK vs TTK')

        self.tk_btn = tk.Button(self, text='Ok')
        self.tk_btn.pack(expand=True, padx=10, pady=10)

        self.ttk_btn = ttk.Button(self, text='Ok')
        self.ttk_btn.pack(expand=True, padx=10, pady=10)

if __name__ == '__main__':
    window = Window()
    window.mainloop()

