import tkinter as tk
from math import *

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Calculadora')

        self.num = tk.IntVar()
        self.lista = list()
        self.op = ''

        self.fr = tk.Frame(self, width=420, height=100, bg='#808080')
        self.fr.pack(fill=tk.X)
        
        self.fr1 = tk.Frame(self, width=420, height=480, bg='white')
        self.fr1.pack(fill=tk.X)

        self.num_entry = tk.Entry(self.fr, state='readonly', bg='#008080', textvar=self.num, bd=5, font=('times 24 bold'), relief='sunken', justify='right')
        self.num_entry.pack(fill=tk.X)

     # ------------------------------------ GRUPO DOS BOTOÕES ESPECIAIS ---------------------------------
        self.clearAll = tk.Button(self.fr1, width=9, height=2, text='CE', font=('times 12 bold'),
                             command=self.limpaTudo, fg='blue', bg='white', bd=2,
                                  relief='raised', activeforeground='red', activebackground='white')
        self.clearAll.place(x=8, y=30)
        self.sen = tk.Button(self.fr1, width=9, height=2, text='sin', font=('times 12 bold'),
                             command=lambda:self.getNum('sin('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.sen.place(x=110, y=30)
        self.cos = tk.Button(self.fr1, width=9, height=2, text='cos', font=('times 12 bold'),
                             command=lambda:self.getNum('cos('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.cos.place(x=210, y=30)
        self.tan = tk.Button(self.fr1, width=9, height=2, text='tan', font=('times 12 bold'),
                              command=lambda:self.getNum('tan('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.tan.place(x=310, y=30)

    # ------------------------------------ PRIMERO GRUPO DOS BOTOÕES ---------------------------------
        self.fat = tk.Button(self.fr1, width=9, height=2, text='!', font=('times 12 bold'),
                             command=lambda:self.getNum('factorial('), fg='blue', bg='white', bd=2,
                                  relief='raised', activeforeground='red', activebackground='white')
        self.fat.place(x=8, y=90)
        self.p_e = tk.Button(self.fr1, width=9, height=2, text='(', font=('times 12 bold'),
                             command=lambda:self.getNum('('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.p_e.place(x=110, y=90)
        self.p_d = tk.Button(self.fr1, width=9, height=2, text=')', font=('times 12 bold'),
                             command=lambda:self.getNum(')'), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.p_d.place(x=210, y=90)
        self.apaga = tk.Button(self.fr1, width=9, height=2, text='C', font=('times 12 bold'),
                              command=self.apaga, fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.apaga.place(x=310, y=90)

    # ------------------------------------ SEGUNDO GRUPO DOS BOTOÕES ---------------------------------
        self.bt7 = tk.Button(self.fr1, width=9, height=2, text='7', font=('times 12 bold'),
                             command=lambda:self.getNum(7), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt7.place(x=8, y=150)
        self.bt8 = tk.Button(self.fr1, width=9, height=2, text='8', font=('times 12 bold'),
                             command=lambda:self.getNum(8), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt8.place(x=110, y=150)
        self.bt9 = tk.Button(self.fr1, width=9, height=2, text='9', font=('times 12 bold'),
                             command=lambda:self.getNum(9), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt9.place(x=210, y=150)
        self.clear = tk.Button(self.fr1, width=9, height=2, text='÷', font=('times 12 bold'),
                              command=lambda:self.getNum('/'), fg='blue', bg='white', bd=2,
                               relief='raised', activeforeground='red', activebackground='white')
        self.clear.place(x=310, y=150)

    # ------------------------------------ TERCEIRO GRUPO DOS BOTOÕES ---------------------------------
        self.bt4 = tk.Button(self.fr1, width=9, height=2, text='4', font=('times 12 bold'),
                             command=lambda:self.getNum(4), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt4.place(x=8, y=210)
        self.bt5 = tk.Button(self.fr1, width=9, height=2, text='5', font=('times 12 bold'),
                             command=lambda:self.getNum(5), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt5.place(x=110, y=210)
        self.bt6 = tk.Button(self.fr1, width=9, height=2, text='6', font=('times 12 bold'),
                             command=lambda:self.getNum(6), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt6.place(x=210, y=210)
        self.div = tk.Button(self.fr1, width=9, height=2, text='x', font=('times 12 bold'),
                              command=lambda:self.getNum('*'), fg='blue', bg='white', bd=2,
                              relief='raised', activeforeground='red', activebackground='white')
        self.div.place(x=310, y=210)

    # ------------------------------------ QUARTO GRUPO DOS BOTOÕES ---------------------------------
        self.bt1 = tk.Button(self.fr1, width=9, height=2, text='1', font=('times 12 bold'),
                             command=lambda:self.getNum(1), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt1.place(x=8, y=270)
        self.bt2 = tk.Button(self.fr1, width=9, height=2, text='2', font=('times 12 bold'),
                             command=lambda:self.getNum(2), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt2.place(x=110, y=270)
        self.bt3 = tk.Button(self.fr1, width=9, height=2, text='3', font=('times 12 bold'),
                             command=lambda:self.getNum(3), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.bt3.place(x=210, y=270)
        self.mult = tk.Button(self.fr1, width=9, height=2, text='-', font=('times 12 bold'),
                              command=lambda:self.getNum('-'), fg='blue', bg='white', bd=2,
                              relief='raised', activeforeground='red', activebackground='white')
        self.mult.place(x=310, y=270)

    # ------------------------------------ QUINTO GRUPO DOS BOTOÕES ---------------------------------
        self.zero = tk.Button(self.fr1, width=9, height=2, text='0', font=('times 12 bold'),
                             command=lambda:self.getNum(0), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.zero.place(x=8, y=330)
        self.dote = tk.Button(self.fr1, width=9, height=2, text='.', font=('times 12 bold'),
                             command=lambda:self.getNum('.'), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.dote.place(x=110, y=330)
        self.sqrt = tk.Button(self.fr1, width=9, height=2, text='√', font=('times 12 bold'),
                             command=lambda:self.getNum('sqrt('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.sqrt.place(x=210, y=330)
        self.sub = tk.Button(self.fr1, width=9, height=2, text='+', font=('times 12 bold'),
                              command=lambda:self.getNum('+'), fg='blue', bg='white', bd=2,
                              relief='raised', activeforeground='red', activebackground='white')
        self.sub.place(x=310, y=330)
    # ------------------------------------ SEXTO GRUPO DOS BOTOÕES ---------------------------------
        self.ln = tk.Button(self.fr1, width=9, height=2, text='log', font=('times 12 bold'),
                             command=lambda:self.getNum('log('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.ln.place(x=8, y=390)
        self.exp = tk.Button(self.fr1, width=9, height=2, text='e', font=('times 12 bold'),
                             command=lambda:self.getNum('exp('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.exp.place(x=110, y=390)
        self.mod = tk.Button(self.fr1, width=9, height=2, text='mod', font=('times 12 bold'),
                             command=lambda:self.getNum('mod('), fg='blue', bg='white', bd=2,
                             relief='raised', activeforeground='red', activebackground='white')
        self.mod.place(x=210, y=390)
        self.soma = tk.Button(self.fr1, width=9, height=2, text='＝', font=('times 12 bold'),
                              command=self.operacao, fg='blue', bg='white', bd=2,
                              relief='raised', activeforeground='red', activebackground='white')
        self.soma.place(x=310, y=390)


    # pega os dígitos precionados
    def getNum(self, num):
        global op
        self.lista.append(num)
        self.op += str(num)
        self.num.set(self.op)

    # efetua os calculos
    def operacao(self):
        global op
        try:
            o = eval(self.op)
        except:
            self.limpaTudo()
            o = ('Erro')
        self.num.set(o)

    # limpa o campo
    def limpaTudo(self):
        global op
        self.op = ""
        self.num.set(self.op)

    # apaga o último valor
    def apaga(self):
        global op
        self.limpaTudo()

        try:
            self.lista.pop()
            for i in range(0, len(self.lista)):
                self.op += str(self.lista[i])
            self.num.set(self.op)
        except:
            self.num.set("Erro")

        
        

if __name__ == '__main__':
    win = Window()
    win.resizable(False, False)
    win.geometry("420x500")
    win.mainloop()
