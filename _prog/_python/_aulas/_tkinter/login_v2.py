from tkinter import *

class Janela:
    def __init__(self, root):
        self.fr = Frame(root, bg='#FFE0EE')
        self.fr.pack()
        self.fr2 = Frame(root, bg='#FFE0EE')
        self.fr2.pack()
        self.fr3 = Frame(root, bg='#FFE0EE')
        self.fr3.pack()
        self.fr4 = Frame(root, bg='#FFE0EE')
        self.fr4.pack(pady=8)
        self.fr5 = Frame(root, bg='#FFE0EE')
        self.fr5.pack(pady=10)

        Label(self.fr, text="PASSWORDS", fg='blue', bg='#FFE0EE',
            font=('Verdana 12 bold'), height=3).pack()

        self.font1 = 'Verdana 14 bold'

        Label(self.fr2, text='Nome:', font=self.font1,
            width=8, bg='#FFE0EE').pack(side='left')

        self.et1 = Entry(self.fr2, font=('times 14 bold'))
        self.et1.focus_force()
        self.et1.pack()

        Label(self.fr3, text='Senha:', font=self.font1,
            width=8, bg='#FFE0EE').pack(side='left')

        self.et2 = Entry(self.fr3, font=('times 14 bold'), show='*')
        self.et2.pack()

        self.btn = Button(self.fr4, text='Verify', relief='ridge',font=self.font1, bg='pink')
        self.btn.config(command=self.testa)
        self.btn.pack()

        self.msg = Label(self.fr5, text='AGUARDANDO...', fg='green', bg='#FFE0EE', font=('Ubuntu 10 bold'))
        self.msg.pack()
    
    def testa(self):
        n = self.et1.get()
        s = self.et2.get()

        if (n == '' or s == ''):
            self.msg.config(text='FAVOR PREENCHE OS CAMPOS!')
            self.msg.config(fg='red')
        else:
            if n == s:
                self.msg.config(text='ACESSO PERMITIDO')
                self.msg.config(fg='darkgreen')
            else:
                self.msg.config(text='ACESSO NEGADO')
                self.msg.config(fg='red')
                self.et1.focus_force()



app = Tk()
jan = Janela(app)
app.config(bg='#FFE0EE')
app.mainloop()
