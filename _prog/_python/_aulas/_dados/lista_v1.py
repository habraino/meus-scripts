#file_name: listas.py

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
        "Agosto", "Setembro", "Octubro", "Novembro", "Dezembro"]
"""
try:
    mes = int(input("Escolha um mês de (1-12) -> "))

    for i in meses:
        pega = meses[mes-1]

    print(f"O mês escolhido é: {pega}")
except IndexError:
    print("Nada encontrado nessa posição!")
"""

n = 1

while (n < 4):
    mes = int(input("De (1-12): "))
    
    if 1 <= mes <= 12:
        print("{}".format(meses[mes-1]))
    n += 1

    