from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3, time, re

class Venda:
    def __init__(self, root):

        # declaração de algumas variáveis
        self.quantProd = IntVar()
        self.it = StringVar()
        self.end = StringVar()
        self.pre = IntVar()
        self.preTotal = DoubleVar()
        self.recibo = IntVar()
        self.pagamento = DoubleVar()
        self.listProd = list()
        self.nomeProd = list()
        self.var = 0

        # cria a frame principal
        self.frame = Frame(root, width=600, height=700, bg='white')
        self.frame.pack()

        # chama a função criaWidget
        self.criaWidget()

        # cria o banco de dados para cliente
        self.conn_cliente = sqlite3.connect('cliente.db')
        self.cursor_cliente = self.conn_cliente.cursor()

        # cria o banco de dados para venda
        self.conn_venda = sqlite3.connect('venda.db')
        self.cursor_venda = self.conn_venda.cursor()

        # chama as funções
        self.createAll()
        self.preenche()

    def createAll(self):
        try:
            self.create_clienteDB()
            self.create_vendaDB()
        except Exception as e:
            print(e)
        else:
            print('Done!')

    # ------------------- DATA BASE DO CLIENTE -----------------
    # cria nova tabela no DB
    def create_clienteDB(self):
        self.cursor_cliente.execute('CREATE TABLE IF NOT EXISTS cliente(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                            'nome TEXT NOT NULL, email TEXT NOT NULL, morada TEXT NOT NULL,'
                            'telefone INT NOT NULL, data TEXT NOT NULL)')

    # insere dados do cliente
    def insert_cliente(self, n, e, m, t):
        self.d = time.strftime('%d-%m-%Y %H:%M:%S')

        try:
            self.cursor_cliente.execute('INSERT INTO cliente VALUES(NULL, ?, ?, ?, ?, ?)', (n, e, m, t, self.d,))
            self.conn_cliente.commit()
        except:
            self.conn_cliente.rollback()

    # ------------------- DATA BASE DA VENDA -----------------
    def create_vendaDB(self):
        self.cursor_venda.execute('CREATE TABLE IF NOT EXISTS venda(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                                  'nome_produto TEXT NOT NULL,'
                                  'quantidade INT NOT NULL,'
                                  'preco_produto REAL NOT NULL,'
                                  'preco_total REAL NOT NULL,'
                                  'pagamento REAL NOT NULL,'
                                  'endereco_entrega TEXT NOT NULL,'
                                  'data TEXT NOT NULL)')

    def insert_vendaDB(self, nProd, qProd, pProd, pTotal, paga, eEntrega):
        try:
            self.data = time.strftime("%d-%m-%Y %H:%M:%S")
            self.cursor_venda.execute('INSERT INTO venda VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)', (
                            nProd, qProd, pProd, pTotal, paga, eEntrega, self.data,))
            self.conn_venda.commit()
        except:
            self.conn_venda.rollback()


    # cria o widget do sistema
    def criaWidget(self):

        # carrega o a tabela produtos
        self.prodConn = sqlite3.connect('produtos.db')
        self.prodCursor = self.prodConn.cursor()

        # cria o cabeçalho
        self.tit = Label(self.frame, text='VENDA DE PRODUTOS', fg='#003380', bg='white' ,font=('Helvetica 20 bold'))
        self.tit.place(x=150, y=20)

        # cria um labelFrame para dados do cliente
        self.lbFrame1 = LabelFrame(self.frame, bg='white', fg='blue', text='  Dados do Cliente  ', width=580, height=200,
                                   relief='sunken', bd=2)
        self.lbFrame1.place(x=10, y=100)

        #------------- pega todos os dados do cliente --------------
        self.lblNome = Label(self.lbFrame1, text='Nome:', bg='white')
        self.lblNome.place(x=5, y=10)
        self.edNome = Entry(self.lbFrame1, width=25)
        self.edNome.focus_force()
        self.edNome.place(x=60, y=10)

        self.lblEmail = Label(self.lbFrame1, text='Email:', bg='white')
        self.lblEmail.place(x=5, y=50)
        self.edEmail = Entry(self.lbFrame1, width=25)
        self.edEmail.place(x=60, y=50)

        self.lblTel = Label(self.lbFrame1, text='Tel.:', bg='white')
        self.lblTel.place(x=5, y=90)
        self.edTel = Entry(self.lbFrame1, width=25)
        self.edTel.place(x=60, y=90)

        self.lblMorada = Label(self.lbFrame1, text='Morada', bg='white')
        self.lblMorada.place(x=350, y=10)
        self.combMorada = ttk.Combobox(self.lbFrame1, takefocus=False, exportselection=1)
        self.combMorada.set('Neves')
        self.combMorada['values'] = ('Neves', 'Guadalupe', 'S.Tomé', 'Bairro Satom',
                                     'Almeirim', 'Sta.Catarina', 'Ponta Figo', 'Santana', 'Budu Budu',
                                     'Práia Gâmboa', 'Morro Peixe', 'Esprainha', 'Bombom', 'Ribeira Afonso',
                                     'Porto Alegre', 'Angolares', 'Trindade')
        self.combMorada.place(x=350, y=30)


        # cria uma labelFrame para venda de produtos
        self.lbFrame2 = LabelFrame(self.frame, text='  Venda de produto ', bg='white', fg='blue', relief='sunken',
                                   bd=2, width=580, height=300)
        self.lbFrame2.place(x=10, y=320)

        #------------- pega todos os dados da compra --------------
        # apresenta os nomes dos produtos
        self.lblNome_Prod = Label(self.lbFrame2, text='Escolha seu produto', bg='white')
        self.lblNome_Prod.place(x=10, y=10)
        self.combProd = ttk.Combobox(self.lbFrame2, takefocus=False, state='readonly')
        self.combProd.config(textvariable=self.it)
        self.combProd.bind('<<ComboboxSelected>>', self.op)
        self.combProd.place(x=10, y=30)

        # pega a quantidade a ser comprada
        self.lblQuant_Prod = Label(self.lbFrame2, text='Quantidade a ser comprado', bg='white')
        self.lblQuant_Prod.place(x=10, y=80)
        self.spimQuant = Spinbox(self.lbFrame2, from_=1, to=2, justify='center', state='readonly', command=self.calcula_preco_total,
                                                textvariable=self.quantProd)
        self.spimQuant.place(x=10, y=100)

        # apresenta o preço total
        self.lblTotal = Label(self.lbFrame2, text='Total:', bg='white')
        self.lblTotal.place(x=10, y=150)
        self.edTotal = Entry(self.lbFrame2, width=15, justify='center', textvariable=self.preTotal, state='readonly')
        self.edTotal.place(x=50, y=150)

        # efetua o pagamento
        self.lblPagamento = Label(self.lbFrame2, text='Efetuar o Pagamento:', bg='white')
        self.lblPagamento.place(x=10, y=200)
        self.edPagamento = Entry(self.lbFrame2, width=20, textvariable=self.pagamento)
        self.edPagamento.place(x=10, y=220)

        # apresenta o preço do produto selecionado
        self.lblPreco = Label(self.lbFrame2, text='Preço do Produto:', bg='white')
        self.lblPreco.place(x=350, y=10)
        self.edPreco = Entry(self.lbFrame2, width=15, justify='center', textvariable=self.pre, state='readonly')
        self.edPreco.place(x=350, y=30)

        # pega o endereço da entrega
        self.lblEndereco = Label(self.lbFrame2, text='Endereço da Entrega:', bg='white')
        self.lblEndereco.place(x=350, y=80)
        self.edEndereco = Entry(self.lbFrame2, width=25, textvariable=self.end)
        self.edEndereco.place(x=350, y=100)

        # ----------- cria dois botões ------------

        # botão efetuar compra
        self.btnComprar = Button(self.frame, text='COMPRAR', bg='white', fg='blue',
                                 activeforeground='red', activebackground='white', command=self.salvar)
        self.btnComprar.place(x=280, y=640)


    # salva a compra
    def salvar(self):
        # pega todos os dados do cliente
        self.n = str(self.edNome.get())
        self.e = str(self.edEmail.get())
        self.m = str(self.combMorada.get())
        self.t = str(self.edTel.get())

        # pega todos os dados da compra
        self.nProd = self.it.get()
        self.qProd = self.quantProd.get()
        self.pProd = self.pre.get()
        self.pTotal = self.preTotal.get()
        self.pagou = float(self.pagamento.get())
        self.eEntrega = self.end.get()

        # faz as possíveis verificações para salvar a venda
        if (self.n != '' and self.e != '' and self.t != '' and self.pagou != '' and self.eEntrega != '' and ('@' in self.e and '.com' in self.e)):
            self.insert_cliente(self.n, self.e, self.m, self.t)
            self.insert_vendaDB(self.nProd, self.qProd, self.pProd, self.pTotal, self.pagou,
                                    self.eEntrega)
            ms.showinfo('INFO', 'Compra efetuada com sucesso!')
            self.it.set('')
            self.end.set('')
            self.edNome.delete(0, END)
            self.edNome.focus_force()
            self.edEmail.delete(0, END)
            self.edTel.delete(0, END)
            self.quantProd.set(1)
            self.pre.set(0)
            self.preTotal.set(0.0)
            self.pagamento.set(0.0)
        elif (self.n != '' and self.e != '' and self.t != '' and self.pagou != '' and self.eEntrega != '' and ('@' not in self.e or '.com' not in self.e)):
            ms.showwarning('ALERTA', 'O E-Mail nao esta no seu formato padrao!')
        else:
            pass

        # verifica se os campos esta vazio
        if (self.n == '' or self.e == '' or self.t == '' or self.pagou == '' or self.eEntrega == ''):
            ms.showerror('ERRO', 'Todos os campos é obrigatório!!')


   #preenche o combobox
    def preenche(self):
        try:
            # preenche os possíveis campos com dados da tabela produtos
            for row in self.prodCursor.execute('SELECT * FROM produtos'):
                # preenche o combobox com nomes dos produtos
                self.nomeProd.append(row[1])
                self.listProd.append(row)
                self.combProd['values'] = self.nomeProd
            self.prodConn.commit()
        except Exception as e:
            print(e)
        else:
            pass


    # pega os dados do produto selecionado
    def op(self, *args):
        # seleciona o produto disponível a venda
        for x in range(0, len(self.listProd)):
            if self.listProd[x][1] == self.it.get():
                self.pre.set(self.listProd[x][2])
                self.var = self.listProd[x][3]
                self.spimQuant['to'] = self.var

        self.calcula_preco_total()

    # método para calcular preço total
    def calcula_preco_total(self, *args):
        self.p = self.pre.get()
        self.q = self.quantProd.get()

        self.mult = int(self.p) * int(self.q)
        self.preTotal.set(self.mult)

app = Tk()
v = Venda(app)
app.title('VENDA DE PRODUTOS')
app.resizable(False, False)
app.mainloop()

