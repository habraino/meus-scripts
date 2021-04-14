from tkinter import *
from tkinter import messagebox as ms
import sqlite3


class Cadastra:
    def __init__(self, root):
        # cria banco de dados
        self.conn = sqlite3.connect('produtos.db')
        self.cursor = self.conn.cursor()

        # variável preço total
        self.total = 0

        # cores
        fundo = 'white'

        # font
        fonte1 = 'Calibre 12 bold'

        # configuração dos botões
        configBtn = {'cor': 'blue', 'fundo': 'white',
                     'tipo': 'groove'}

        self.frame = Frame(root, width=600, height=650, bg=fundo)
        self.frame.pack()

        # coloca o cabeçalho
        self.lblText = Label(self.frame, text='CADASTRO DE NOVOS PRODUTOS', bg=fundo,
                             fg='#003380' ,font=('Helvetica 20 bold'))
        self.lblText.place(x=80, y=30)

        # nome do produto
        self.lblNome = Label(self.frame, text='Nome do Produto:', bg=fundo, font=fonte1)
        self.lblNome.place(x=50, y=180)
        self.edNome = Entry(self.frame, width=25, relief='solid')
        self.edNome.focus_force()
        self.edNome.place(x=240, y=180)

        # preço do produto
        self.lblPreco = Label(self.frame, text='Preço do Produto:', bg=fundo, font=fonte1)
        self.lblPreco.place(x=50, y=220)
        self.edPreco = Entry(self.frame, width=25, relief='solid')
        self.edPreco.place(x=240, y=220)

        # quantidade
        self.lblquant = Label(self.frame, text='Quant. do Produto:', bg=fundo, font=fonte1)
        self.lblquant.place(x=50, y=260)
        self.edQuant = Entry(self.frame, width=25, relief='solid')
        self.edQuant.place(x=240, y=260)

        # dois butões
        self.btnCadas = Button(self.frame, text='CADASTRAR',
                             fg=configBtn['cor'], bg=configBtn['fundo'],
                             relief=configBtn['tipo'],
                               activeforeground='red', activebackground='white')
        self.btnCadas.config(command=self.cadastrar)
        self.btnCadas.place(x=250, y=350)

        # cria uma nova tabela
        self.create()  # cria a tabela

    # cria uma nova tabe
    # la
    def create(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                            'nome TEXT NOT NULL, preco REAL NOT NULL, quantidade INT NOT NULL, total REAL NOT NULL)')

    # insere dados na tabela
    def insert(self, n, p, q, t):
        self.cursor.execute('INSERT INTO produtos VALUES(NULL, ?, ?, ?, ?)', (n, p, q, t,))
        self.conn.commit()

    # método para cadastrar produto
    def cadastrar(self):
        self.n = str(self.edNome.get())
        self.p = str(self.edPreco.get())
        self.q = str(self.edQuant.get())

        if (self.n != '' and self.p != '' and self.q != ''):
            # calcula preço total
            self.total = float(self.p) * float(self.q) # calcula preço total

            # insere dados na tabela
            self.insert(self.n, self.p, self.q, self.total)
            ms.showinfo('INFO', 'Produto cadastrado com sucesso!')
            self.edNome.focus_force()
            self.edNome.delete(0, END)
            self.edPreco.delete(0, END)
            self.edQuant.delete(0, END)

        # casos os campos estiverem vazios
        if (self.n == '' or self.p == '' or self.q == ''):
            ms.showerror('Erro', 'Todos campos são obrigatórios!')


