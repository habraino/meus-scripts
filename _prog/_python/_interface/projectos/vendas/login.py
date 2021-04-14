from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from time import strftime

class Login:
    def __init__(self, root):

        # cria banco de dados
        self.conn = sqlite3.connect('senha.db')
        self.cursor = self.conn.cursor()

        # cores
        fundo = 'white'

        # font
        fonte = 'Geometry 14 bold'
        fonte1 = 'Geometry 18 bold'
        fonte2 = 'Calibre 12 bold'
        configBtn = {'cor':'blue', 'fundo':'white',
                     'tipo':'groove'}

        self.frame = Frame(root, width=500, height=400, bg="white")
        self.frame.pack()

        # cria o titúlo principal
        self.tit = Label(self.frame, text='TELA LOGIN', fg='blue', bg=fundo, font=fonte1)
        self.tit.place(x=180, y=20)

        # label e entry de email
        self.lblEmail = Label(self.frame, text='Nome:', bg=fundo, font=fonte)
        self.lblEmail.place(x=40, y=100)
        self.edEmail = Entry(self.frame, width=25, font=fonte2)
        self.edEmail.focus_force()
        self.edEmail.place(x=140, y=100)

        # label e entry de senha
        self.lblSenha= Label(self.frame, text='Senha:', bg=fundo, font=fonte)
        self.lblSenha.place(x=40, y=140)
        self.edSenha = Entry(self.frame, width=25, show='*', font=fonte2)
        self.edSenha.place(x=140, y=140)

        self.aviso = Label(self.frame, text='', bg=fundo, font=fonte)
        self.aviso.place(x=100, y=260)

        # cria dois butões
        self.btnLog = Button(self.frame, text='LOGAR',
                             fg=configBtn['cor'], bg=configBtn['fundo'],
                             relief=configBtn['tipo'],
                             activeforeground='red', activebackground='white')
        self.btnLog.config(command=self.logar)
        self.btnLog.place(x=110, y=200)

        self.btnCad = Button(self.frame, text='CADASTRAR',
                             fg=configBtn['cor'], bg=configBtn['fundo'],
                             relief=configBtn['tipo'],
                             activeforeground='red', activebackground='white')
        self.btnCad.config(command=self.cadastrar)
        self.btnCad.place(x=265, y=200)

        # cria nova tabela
        self.chamaTabela()

    # cria a tabela
    def create(self):
        sql = 'CREATE TABLE IF NOT EXISTS login(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,' \
              'nome TEXT, senha TEXT, data TEXT)'
        self.cursor.execute(sql)

    # cadastra senha na tabela
    def insert(self, e, s):
        self.d = strftime('%d-%m-%Y  %H:%M:%S')
        self.cursor.execute('INSERT INTO login VALUES(NULL, ?, ?, ?)', (e, s, self.d,))
        self.conn.commit()

    def chamaTabela(self):
        try:  # tenta criar banco de dados
            self.create()
        except:  # caso ocorrer erro
            print('Erro ao criar banco de dados')
        else:  # banco de dados criado com sucesso!
            print('Banco de Dados criado com sucesso!')

    # cadastra nova senha
    def cadastrar(self):
        # pega dados do usuário e cadastra na tabela
        self.e = str(self.edEmail.get())
        self.s = str(self.edSenha.get())

        if self.e == '' or self.s == '':
            ms.showwarning('ALERTA', 'Todos campos são obrigatórios!')
        else:
            self.insert(self.e, self.s)
            # limpa os campos e coloca o focus no edEmail
            self.edEmail.delete(0, END)
            self.edSenha.delete(0, END)
            self.edEmail.focus_force()
            ms.showinfo('INFO', 'Senha Cadastrada com sucesso!')

    # login do usuário
    def logar(self):

        s_e = list()
        cont = 0

        # pega dados digitados pelo usuário
        self.e = str(self.edEmail.get())
        self.s = str(self.edSenha.get())

        sql = 'SELECT * FROM login'
        lista = self.cursor.execute(sql,).fetchall()
        for row in lista[:]:
            s_e.append(row)
            cont +=1

        a = 0
        try:
            while a < cont:
                # caso usuário digite algo na tela
                a += 1  # incrementa o contador do while 'a'
                if self.e != '' and self.s != '':
                    # faz verificação se usuário está cadastrado
                    for i in range(0, len(s_e)):
                        if (self.e in s_e[i]) and (self.s in s_e[i]):
                            ms.showinfo('INFO', 'LOGADO COM SUCESSO!')
                            app.destroy()  # mata a tela login
                            import main_venda  # chama a classe main_venda

                            # cria uma nova instância da classe main_venda
                            self.j = Tk()
                            self.j.config(bg='white')
                            self.j.title('CADASTRO DE PRODUTOS')
                            self.j.resizable(False, False)
                            self.c = main_venda.Main(self.j)
                            break
                    if (self.e not in s_e) and (self.s not in s_e):
                        self.aviso['text'] = 'Email ou senha estão incorrectos!!\nFavor certifique-se que já estás cadastrado!'
                        self.aviso.config(fg='red', font=('times 12 bold'))
                    else:
                        self.aviso['text'] = ''

                # caso campos estiverem vazios
                elif self.e == '' or self.s == '':
                    ms.showwarning('ALERTA', 'Todos os campos são obrigatórios')
                    break
        except Exception as e:
            print(e)
        else:
            pass
        '''
        # caso usuário digite algo na tela
        if self.e != '' and self.s != '':
            # faz verificação se usuário está cadastrado
            for i in range(0, len(s_e)):
                if (self.e in s_e[i]) and (self.s in s_e[i]):
                    ms.showinfo('INFO', 'LOGADO COM SUCESSO!')
                    app.destroy()# mata a tela login
                    import main_venda # chama a classe main_venda

                    # cria uma nova instância da classe main_venda
                    self.j = Tk()
                    self.j.config(bg='white')
                    self.j.title('CADASTRO DE PRODUTOS')
                    self.j.resizable(False, False)
                    self.c = main_venda.Main(self.j)
                    break
                elif (self.e not in s_e[i]) and (self.s not in s_e[i]):
                    ms.showerror('ERRO', 'Email ou senha estão incorrectas!!\nFavor certifique-se que já estás cadastrado!')
                    break
                else:
                    pass
            
        '''

app = Tk()
login = Login(app)
app.title('Tela Login')
app.geometry('500x400')
app.resizable(False, False)
app.mainloop()

