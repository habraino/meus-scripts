import math

def busca_binaria_recursiva(numeros,esquerda,direita,procurado):
    if esquerda > direita:
        return -1
    else:
        meio = math.floor((esquerda+direita)/2)
        if numeros[meio]==procurado:
            return meio
        else:
            if numeros[meio] > procurado:
                return busca_binaria_recursiva(numeros,esquerda,meio-1,procurado)
            else:
                return busca_binaria_recursiva(numeros,meio+1,direita,procurado)

numeros = [3,7,10,15,20,50]
n = 6
procurado = 15
resposta = busca_binaria_recursiva(numeros,0,n-1,procurado)
print (resposta)
