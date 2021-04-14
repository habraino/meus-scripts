from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3, time


class Main:

    def __init__(self, root):

        # abre o banco de dados
        self.conn = sqlite3.connect('produtos.db')
        self.cursor = self.conn.cursor()

        # cria o banco de dados para cliente
        self.conn_cliente = sqlite3.connect('cliente.db')
        self.cursor_cliente = self.conn_cliente.cursor()

        # cria o banco de dados para venda
        self.conn_venda = sqlite3.connect('venda.db')
        self.cursor_venda = self.conn_venda.cursor()

        # carrega as imagens
        self.imgSearch = PhotoImage(file="img/search.png")
        self.logo = PhotoImage(file='img/logo.png')
        self.textLogo = PhotoImage(file='img/loja_logo.png')
        self.up = PhotoImage(file='img/update.png')
        self.imgApagar = PhotoImage(file='img/apagar.png')
        self.imgVender = PhotoImage(file='img/vender.png')
        self.imgCadastrar = PhotoImage(file='img/cadastrar.png')

        self.frTop = Frame(root, width=1024, height=100, bg='white')
        self.frTop.pack(fill=X)
        self.frLeft = Frame(root, width=200, height=700, bg='white')
        self.frLeft.pack(side=LEFT)
        self.frCenter = Frame(root, bg='white')
        self.frCenter.pack(fill=X)
        self.c = Label(self.frCenter)
        self.c.pack(side=RIGHT, fill=BOTH)

        # coloca campo de pesquisa e botão para evento
        self.campo = Entry(self.frTop, width=30, relief=SOLID)
        self.campo.place(x=900, y=50)

        self.btnSearch = Button(self.frTop, image=self.imgSearch, bg='white', width=20, height=20, relief=SOLID,
                                command=self.pesquisarPor, bd=0, activebackground='silver')
        self.btnSearch.place(x=1150, y=50)
        self.btnSearch.image = self.imgSearch

        # coloca os logos da loja
        self.lblLogo = Label(self.frTop, image=self.logo, width=100, height=100, bg='white')
        self.lblLogo.image = self.logo
        self.lblLogo.place(x=50, y=20)

        self.lblText = Label(self.frTop, image=self.textLogo, width=570, height=73, bg='white')
        self.lblText.image = self.textLogo
        self.lblText.place(x=300, y=20)

        # botão para atualizar dados
        self.btnUp = Button(self.frTop, image=self.up, width=30, height=30, bg='white',
                            relief=SOLID ,command=self.update, bd=0)
        self.btnUp.image = self.up
        self.btnUp.place(x=200, y=60)

        # os botões do lateral esquerdo
        self.cadastra = Button(self.frLeft, image=self.imgCadastrar, bg='white', fg='blue', relief=GROOVE, width=150, height=90
                               , command=self.cadastrar, activeforeground='red', activebackground='white')
        self.cadastra.image = self.imgCadastrar
        self.cadastra.place(x=20, y=40)

        self.vender = Button(self.frLeft, image=self.imgVender, bg='white', fg='blue', relief=GROOVE, width=150, height=90,
                             activeforeground='red', activebackground='white', command=self.venda)
        self.vender.image = self.imgVender
        self.vender.place(x=20, y=160)

        self.apaga = Button(self.frLeft, width=150, height=90, image=self.imgApagar, bg='white', fg='blue', relief=GROOVE,
                            command=self.apagar, activeforeground='red', activebackground='white')
        self.apaga.image = self.imgApagar
        self.apaga.place(x=20, y=280)

        # scroll no lateral direito
        self.scrool = Scrollbar(self.c, orient='vertical')
        self.scrool.pack(side=RIGHT, fill=BOTH)

        # cria um estilo
        self.s = ttk.Style()
        self.s.theme_use('classic')
        self.s.configure('Treeview', foreground='#882237',
                         font=('georgia 12 bold'), values=E)

        # coloca a treeview na parte centar
        self.tree = ttk.Treeview(self.frCenter, height=28, style='Treeview')
        self.scrool.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrool.set)

        # cria as colunas
        self.tree['columns'] = ('', 'preco', 'quant', 'total')
        self.tree.heading('#0', text='ID', anchor='center')
        self.tree.column('', anchor='center')
        self.tree.heading('', text='NOME-PRODUTO', anchor='center')
        self.tree.heading('preco', text='PREÇO', anchor='center')
        self.tree.column('preco', anchor='center')
        self.tree.heading('quant', text='QUANTIDADE', anchor='center')
        self.tree.column('quant', anchor='center')
        self.tree.heading('total', text='TOTAL', anchor='center')
        self.tree.column('total', anchor='center')

        # preenche automaticamente o tree view
        try:
            for row in self.lerDados():
                self.tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
        except Exception as e:
            print(e)
        else:
            self.tree.insert('', 'end', text='', values=('', '', '', ''))
        self.tree.pack(fill='x', side=LEFT)

    # método para chamar classe cadastrarProdutos
    def cadastrar(self):
        import cadastra_produto
        self.j = Tk()
        self.j.title('NOVO PRODUTO')
        self.j.resizable(False, False)
        self.c = cadastra_produto.Cadastra(self.j)

    # cria o widget toplevel venda
    def nova_venda(self):
        self.ap = Toplevel()
        self.ap.title('VENDA DE PRODUTOS')
        self.ap.config(bg='white')
        self.ap.geometry("600x700")
        self.ap.resizable(False, False)

        # chama as funções
        self.criaWidget()
        self.createAll()
        self.preenche()

        self.ap.mainloop() # inicia o TopLevel

    def venda(self):
        self.tVenda = Toplevel()
        self.tVenda.geometry("700x550")
        self.tVenda.config(bg='white')
        self.tVenda.resizable(False, False)


        # cria um frame no topo
        self.fr1 = Frame(self.tVenda, width=700, height=60, bg='white')
        self.fr1.pack()

        # cria outro frame para expandir todo resto da janela
        self.fr2 = Frame(self.tVenda, width=700, height=490, bg='white')
        self.fr2.pack()

        # cria um botão para nova_venda
        self.btn_nova = Button(self.fr1, text='NOVA VENDA', bg='white', fg='blue', activebackground='white',
                               activeforeground='red', command=self.nova_venda)
        self.btn_nova.place(x=50, y=20)

        # cria uma treeview que apresenta dados do cliente
        self.treeClient = ttk.Treeview(self.fr2, height=20, style='Treeview')
        self.treeClient['columns'] = ('', 'morada')

        self.treeClient.heading('#0', text='ID', anchor='center')
        self.treeClient.heading('', text='NOME', anchor='center')
        self.treeClient.heading('morada', text='MORADA', anchor='center')

        for i in self.cursor_cliente.execute('select * from cliente'):
            self.treeClient.insert('', 'end', text=i[0], values=(i[1], i[3]))
        self.treeClient.pack()


        self.tVenda.mainloop()

    # cria o widget do sistema
    def criaWidget(self):

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

        # cria o cabeçalho
        self.tit = Label(self.ap, text='VENDA DE PRODUTOS', fg='#003380', bg='white', font=('Helvetica 20 bold'))
        self.tit.place(x=150, y=20)

        # cria um labelFrame para dados do cliente
        self.lbFrame1 = LabelFrame(self.ap, bg='white', fg='blue', text='  DADOS DO CLIENTE  ', width=580,
                                   height=200,
                                   relief='sunken', bd=2)
        self.lbFrame1.place(x=10, y=100)

        # ------------- pega todos os dados do cliente --------------
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
        self.lbFrame2 = LabelFrame(self.ap, text='  VENDA DE PRODUTO ', bg='white', fg='blue', relief='sunken',
                                   bd=2, width=580, height=300)
        self.lbFrame2.place(x=10, y=320)

        # ------------- pega todos os dados da compra --------------
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
        self.spimQuant = Spinbox(self.lbFrame2, from_=1, to=2, justify='center', state='readonly',
                                 command=self.calcula_preco_total,
                                 textvariable=self.quantProd)
        self.spimQuant.place(x=10, y=100)

        # apresenta o preço total
        self.lblTotal = Label(self.lbFrame2, text='Total:', bg='white')
        self.lblTotal.place(x=10, y=150)
        self.edTotal = Entry(self.lbFrame2, width=15, justify='center', textvariable=self.preTotal,
                             state='readonly')
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

        # botão efetuar compra
        self.btnComprar = Button(self.ap, text='COMPRAR', bg='white', fg='blue',
                                 activeforeground='red', activebackground='white', command=self.salvar)
        self.btnComprar.place(x=280, y=640)

    # método para inserir dados no tree
    def lerDados(self):
        return self.cursor.execute('SELECT * FROM produtos')

    # remove item do banco de dados
    def delete(self, arg):
            self.cursor.execute('DELETE FROM produtos WHERE ID = ?',(arg,))
            self.conn.commit()

    # apagar registros
    def apagar(self):
        if not self.tree.focus():
            ms.showerror('ERRO', 'Nenhum item selecionado!')
        else:
            self.item_selecionado = self.tree.focus()
            if (ms.askquestion('Alerta', 'Desejas excluir o dados?') == 'yes'):
                row = self.tree.item(self.item_selecionado)
                self.delete(row['text'])
                self.tree.delete(self.item_selecionado)
            else:
                pass

    # atualiza e adiciona novos dados
    def update(self):
        self.x = self.tree.get_children()
        for item in self.x:
            self.tree.delete(item)

        # preenche automaticamente o tree view
        for row in self.lerDados():
            self.tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))


    # método para efetuar busca de produto
    def pesquisarPor(self):
        self.c = str(self.campo.get())
        itens = self.tree.get_children()
        sql = 'SELECT * FROM produtos WHERE nome = ?'
        self.dadoPesquisado = self.cursor.execute(sql, (self.c,))

        # caso usuário digite algo no campo de pesquisa
        if self.c != '':
            for item in self.dadoPesquisado:
                # apaga todos os elementos na tela
                for x in itens:
                    self.tree.delete(x)

                # insere o elemento pesquisado na tela
                if self.c in item: # caso nome estiver no banco de daods
                    self.tree.insert('', 'end', text=item[0], values=(item[1], item[2], item[3], item[4]))
            self.conn.commit()
        elif self.c == '':
            self.update()
            ms.showerror('ERRO', 'Campo está vázio!')
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
        if (self.n != '' and self.e != '' and self.t != '' and self.pagou != '' and self.eEntrega != '' and (
                '@' in self.e and '.com' in self.e)):
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
        elif (self.n != '' and self.e != '' and self.t != '' and self.pagou != '' and self.eEntrega != '' and (
                '@' not in self.e or '.com' not in self.e)):
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
            for row in self.lerDados():
                # preenche o combobox com nomes dos produtos
                self.nomeProd.append(row[1])
                self.listProd.append(row)
                self.combProd['values'] = self.nomeProd
            self.conn.commit()
        except Exception as e:
            print(e)
        else:
            pass

    # cria tabela cliente e venda
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


app = Tk()
app.title('CADASTRO DE PRODUTOS')
app.configure(bg='white')
app.resizable(False, False)
Main(app)
app.mainloop()

