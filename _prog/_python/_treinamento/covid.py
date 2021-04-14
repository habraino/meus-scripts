from tkinter import *

import os
try:
    from covid import Covid
except ImportError:# caso teu pc não tiver essas libs, a instalação é feita auto
    print("O seu computador não possui essa biblioteca!")
    if(os.name == "nt"):#se for windows
        os.system("pip3 install covid")
    else:#se for uma distro linux
        os.system("sudo pip3 install covid")

root = Tk()

#-------------------------------------------
# class
class sanCovid(Frame):
    def __init__(self, parent):
        super().__init__()

        self.root = root
        self.covid = Covid()
        
        self.root.title("San-Covid")
        self.altura = root.winfo_screenwidth()
        self.largura = root.winfo_screenheight()
        self.x = int(self.altura/2) - int(1280/2)
        self.y = int(self.largura/2) - int(720/2)
        self.root.geometry(f"1280x720+{self.x}+{self.y}")

        self.root["background"] = "#4377aa"

        self.widgets_tela()
        self.paises_enfetados()
        self.total_resultados()
        
        root.mainloop()

    #-------------------------------------------
    # parte lógica
    nome_pais = StringVar()

    def total_resultados(self):
        self.casos_ativo = self.covid.get_total_active_cases()
        self.casos_confirmado = self.covid.get_total_confirmed_cases()
        self.casos_recuperado = self.covid.get_total_recovered()
        self.casos_morto = self.covid.get_total_deaths()

        self.decionario = {"Total Activo:":self.casos_ativo, "Total Confirmados:":self.casos_confirmado, "Total Recuperados:":self.casos_recuperado, "Total Mortos:":self.casos_morto}
        
        for x in self.decionario:
            self.listabox_3.insert(END, x, self.decionario[x], "\n")

    def paises_enfetados(self):
        self.lista_pais = self.covid.list_countries()

        for i in self.lista_pais:
            self.listabox_2.insert(END, i['name'])

    def casos_detalhes(self):
        self.casos = self.covid.get_status_by_country_name(self.nome_pais.get())
    
        self.lista_dados = ["ID:", "País:", "Confirmado:", "Ativo:", "Mortos:", "Recuperado:"]
        
        y = 0
        for x in self.casos:
            self.listabox_1.insert(END, self.lista_dados[y], str(self.casos[x]), "\n")
            y += 1
            if(y == 6):
                break

        
    #-------------------------------------------
    # widgets
    def widgets_tela(self):
        self.label_nome = Label(self.root,
                           text = "Digite nome de um País:",
                           font = "Arial 14 bold",
                           background = "#4377aa",
                           fg = "#fff"
                           )
        self.label_exemple = Label(self.root,
                                   text = "Nota: Os nomes têm que está escrito\n desta forma no campo de formulário",
                                   background = "red",
                                   fg = "#fff")
        self.campo = Entry(root, textvariable = self.nome_pais)
        self.listabox_1 = Listbox(self.root, background = "#ccc")
        self.listabox_2 = Listbox(self.root, background = "#ccc")
        self.listabox_3 = Listbox(self.root, background = "#ccc")
        self.btn = Button(self.root,
                     text = "Consultar",
                     background = "#414146",
                     bd = 0,
                     height = 2,
                     fg = "#fff",
                     command = lambda: self.casos_detalhes()
                     )

        self.label_nome.place(relx = 0.45, rely = 0.2)
        self.label_exemple.place(relx = 0.2, rely = 0.92, relwidth = 0.2, relheight = 0.07)
        self.campo.place(relx = 0.45, rely = 0.25, relwidth = 0.41, relheight = 0.05)
        self.btn.place(relx = 0.83, rely = 0.25, relheight = 0.05)
        self.listabox_1.place(relx = 0.66, rely = 0.37, relwidth = 0.2, relheight = 0.43)
        self.listabox_2.place(relx = 0.2, rely = 0.02, relwidth = 0.2, relheight = 0.9)
        self.listabox_3.place(relx = 0.45, rely = 0.37, relwidth = 0.2, relheight = 0.43)

#-------------------------------------------
# executar
sanCovid(root)
