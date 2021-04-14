import tkinter as tk
import tkinter.messagebox as msbox

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Hello World 2')

        self.lb_text = tk.StringVar()
        self.lb_text.set("Choose One")

        self.lbl = tk.Label(self, textvariable=self.lb_text)
        self.lbl.pack(fill=tk.BOTH, expand=True, padx=100, pady=30)

        btn1 = tk.Button(self, text='Say Hello', command=self.sayHello)
        btn1.pack(side=tk.LEFT, expand=True, padx=(20, 0), pady=(0, 20))

        btn2 = tk.Button(self, text='Say Goodbye', command=self.sayGoobye)
        btn2.pack(side=tk.RIGHT, expand=True, padx=(0, 20), pady=(0, 20))

    def sayHello(self):
        msbox.showinfo('Hello', 'Hello World!')

    def sayGoobye(self):
        if (msbox.askyesno('Close window?', 'Would you like to close this window?')):
            self.lb_text.set('Window will clossing in 2 seconds')
            msbox.showinfo("Goodbye", "Goodbye, it's been fun!")
            self.after(2000, self.destroy)
        else:
            msbox.showinfo('Not Closing!', 'Great! This window will stay open.')


if __name__ == '__main__':
    window = Window()
    window.mainloop()

