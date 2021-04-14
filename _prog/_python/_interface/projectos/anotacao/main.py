from tkinter import *
from tkinter import messagebox as ms
import sqlite3


class Anotacao(Tk):
    def __init__(self):
        super().__init__()

        # Cria um banco de dados
        self.conn = sqlite3.connect('DAO/nota.db')
        self.cursor = self.conn.cursor()

        try:
            self.cria_tabela()
        except:
            print('Erro ao criar DB')
        finally:
            print("DB criando com sucesso!")

        self.frame1 = Frame(self, width=600, height=100, bg='white')
        self.frame1.place(x=10, y=10)
        self.frame2 = Frame(self, width=600, height=300, bg='white')
        self.frame2.place(x=40, y=100)

        estilo = {'bg': 'white', 'fg': 'blue', 'font': 'times 14 bold', 'actFore': 'red', 'actBack': 'white'}

        self.btnNova = Button(self.frame1, text='NOVA NOTA', bg=estilo['bg'], fg=estilo['fg'],
                         activebackground=estilo['actBack'], activeforeground=estilo['actFore'], command=self.novaNota)
        self.btnNova.place(x=50, y=20)

        self.btnEditar = Button(self.frame1, text='EDITAR', bg=estilo['bg'], fg=estilo['fg'],
                         activebackground=estilo['actBack'], activeforeground=estilo['actFore'], command=self.novaNota1)

        self.btnEditar.place(x=160, y=20)

        self.btnDeletar = Button(self.frame1, text='DELETAR', bg=estilo['bg'], fg=estilo['fg'],
                         activebackground=estilo['actBack'], activeforeground=estilo['actFore'], command=self.deletar)
        self.btnDeletar.place(x=240, y=20)

        self.btnAtualizar = Button(self.frame1, text='ATUALIZAR', bg=estilo['bg'], fg=estilo['fg'],
                            activebackground=estilo['actBack'], activeforeground=estilo['actFore'], command=self.atualizar)
        self.btnAtualizar.place(x=330, y=20)

        self.sc = Scrollbar(self.frame2, orient='vertical')
        self.sc.pack(side='right', fill=Y)
        self.lista = Listbox(self.frame2, width=60, height=28)
        self.lista.config(yscrollcommand=self.sc.set)
        self.sc.config(command=self.lista.yview)
        self.lista.pack(side='left')
        self.preencheLista()

    # Cria nova tabela
    def cria_tabela(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS notas(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
                            'titulo TEXT NOT NULL, nota TEXT NOT NULL)')
    # Insere dados na tabela
    def insereDados(self, tit, nota):
        self.cursor.execute('INSERT INTO notas VALUES(NULL, ?, ?)', (tit, nota))
        self.conn.commit()

    # Deleta dados na tabela
    def deletaDados(self, arg):
        self.cursor.execute('DELETE from notas WHERE titulo = ?', (arg,))
        self.conn.commit()
    # Atualizar dados na Tabela
    def atualizaDados(self, arg1, arg2):
        self.cursor.execute('UPDATE notas set nota = ? WHERE titulo = ?', (arg1, arg2))
        self.conn.commit()

    # método criar nova nota
    def novaNota(self):

        self.nova = Toplevel()
        self.nova.title("Nova Nota")
        self.nova.config(bg='white')
        self.nova.geometry("600x650")
        self.nova.resizable(False, False)

        # Cria uma variável
        self.var = StringVar()

        self.fr1 = Frame(self.nova, width=600, height=100, bg='white')
        self.fr1.place(x=10, y=10)
        self.fr2 = Frame(self.nova, width=600, height=300, bg='white')
        self.fr2.place(x=10, y=120)

        self.tit = Label(self.fr1, text='Título:', fg='blue', bg='white', font='calibre 14')
        self.tit.place(x=10, y=20)

        self.ed = Entry(self.fr1, width=50, textvariable=self.var)
        self.ed.focus_force()
        self.ed.place(x=70, y=25)

        self.msg = Label(self.fr1, text='Escreva a nota:', fg='blue', bg='white')
        self.msg.place(x=10, y=80)

        self.scrool = Scrollbar(self.fr2, orient='vertical')

        self.caixaText = Text(self.fr2, width=60, height=25, autoseparators=True, font='helvetica 12')
        self.caixaText.config(yscrollcommand=self.scrool.set)
        self.scrool.config(command=self.caixaText.yview)
        self.caixaText.pack(side=LEFT)
        self.scrool.pack(side=RIGHT, fill=BOTH)

        self.btnSalvar = Button(self.nova, text='SALVAR', bg='white', fg='blue',
                            activebackground='white', activeforeground='red', command=self.salvaNota)
        self.btnSalvar.place(x=250, y=610)

        self.nova.mainloop()

    # método criar editar nota
    def novaNota1(self):
        self.nova = Toplevel()
        self.nova.title("Nova Nota")
        self.nova.config(bg='white')
        self.nova.geometry("600x650")
        self.nova.resizable(False, False)

        # Cria uma variável
        self.var = StringVar()

        self.fr1 = Frame(self.nova, width=600, height=100, bg='white')
        self.fr1.place(x=10, y=10)
        self.fr2 = Frame(self.nova, width=600, height=300, bg='white')
        self.fr2.place(x=10, y=120)

        self.tit = Label(self.fr1, text='Título:', fg='blue', bg='white', font='calibre 14')
        self.tit.place(x=10, y=20)

        self.ed1 = Entry(self.fr1, width=50, textvariable=self.var, state='readonly')
        self.ed1.place(x=70, y=25)

        self.msg = Label(self.fr1, text='Escreva a nota:', fg='blue', bg='white')
        self.msg.place(x=10, y=80)

        self.scrool = Scrollbar(self.fr2, orient='vertical')

        self.txt = Text(self.fr2, width=60, height=25, autoseparators=True, font='helvetica 12')
        self.txt.config(yscrollcommand=self.scrool.set)
        self.scrool.config(command=self.txt.yview)
        self.txt.pack(side=LEFT)
        self.scrool.pack(side=RIGHT, fill=BOTH)

        self.btnAt = Button(self.nova, text='ATUALIZAR', bg='white', fg='blue',
                                activebackground='white', activeforeground='red', command=self.at)
        self.btnAt.place(x=250, y=610)

        self.editar()
        self.nova.mainloop()


    def salvaNota(self):
        self.t = self.var.get()
        self.n = str(self.caixaText.get(1.0, END))

        if self.t.isspace() or self.n.isspace():
            ms.showerror('ERRO', 'Todos campos são obrigatórios.')
        else:
            self.insereDados(self.t, self.n)
            ms.showinfo('INFO', 'Salvo com sucesso!')

    def preencheLista(self):
        self.l = self.cursor.execute('SELECT * FROM notas').fetchall()

        for row in self.l[:]:
            self.lista.insert(END, row[1])

    def editar(self):
        self.it1 = str(self.lista.get(ACTIVE))
        self.it2 = self.lista.curselection()
        if not self.it2:
            ms.showerror('ERRO', 'Nenhum item selecionado!')
        else:
            self.listaNotas = self.cursor.execute('SELECT * FROM notas WHERE titulo = ?', (self.it1,)).fetchall()
            for i in range(0, len(self.listaNotas)):
                self.var.set(self.it1)
                self.txt.insert(0.0, self.listaNotas[i][2])

    def at(self):
        self.t = self.var.get()
        self.n = str(self.txt.get(1.0, END))

        if self.t.isspace() or self.n.isspace():
            ms.showerror('ERRO', 'Todos campos são obrigatórios.')
        else:
            self.atualizaDados(self.n, self.t)
            ms.showinfo('INFO', 'Atualizado com sucesso!')

    def deletar(self):
        self.item = str(self.lista.get(ACTIVE))
        self.item2 = self.lista.curselection()
        if not self.item2:
            ms.showerror('ERRO', 'Nenhum item selecionado!')
        else:
            if(ms.askquestion('DELETAR', 'Desejas deletar o item selecionado?') == 'yes'):
                self.deletaDados(self.item)
                self.lista.delete(self.item2)
            else:
                pass

    def atualizar(self):
        self.lista.delete(0, END)
        self.preencheLista()


if __name__ == '__main__':
    nota = Anotacao()
    nota.title('Anotação')
    nota.config(bg='white')
    nota.geometry("600x650")
    nota.resizable(False, False)
    nota.mainloop()
