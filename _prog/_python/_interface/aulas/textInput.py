import tkinter as tk
import tkinter.messagebox as msbox

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Text Input Example')

        self.lb_text = tk.StringVar()
        self.lb_text.set('My name is:')

        self.name = tk.StringVar()

        self.lb = tk.Label(self, textvar=self.lb_text)
        self.lb.pack(fill=tk.BOTH, expand=True, padx=100, pady=10)

        self.entry = tk.Entry(self, textvar=self.name)
        self.entry.pack(fill=tk.BOTH, expand=True, padx=100, pady=10)

        self.btn_sayHello = tk.Button(self, text='Say Hello', command=self.say_hello)
        self.btn_sayHello.pack(side=tk.LEFT, expand=True, padx=(20, 0), pady=(0, 20))

        self.btn_sayGoodbye = tk.Button(self, text='Say Goodbye', command=self.say_goodbye)
        self.btn_sayGoodbye.pack(side=tk.RIGHT, expand=True, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        msbox.showinfo('Hello', 'Hello World, ' + self.name.get())

    def say_goodbye(self):
        self.close = msbox.askyesno('Goodbye', 'Would you like to close this window?')
        if self.close:
            message = "This window will clousing in  seconds - goodbye " + self.name.get()
            self.lb_text.set(message)
            self.after(2000, self.destroy)
        else:
            msbox.showinfo('Not clousing', 'Great! This window will stay open.')

if __name__ == '__main__':
    window = Window()
    window.mainloop()

