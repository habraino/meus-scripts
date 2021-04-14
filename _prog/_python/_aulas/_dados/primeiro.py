"""
 Faça um algoritmo que calcule a quantidade de litros de combustível gasta em uma viagem,
 utilizando um automóvel que faz 12Km por litro. Para obter o cálculo,
 o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
 Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
 Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula:
 LITROS_USADOS = DISTANCIA / 12.
 O programa deve apresentar os valores da velocidade média,
 tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem. 
"""

# método para analisar tudo numa viagem
def calc():
    # delcaração das variáveis global
    global tem 
    global vel
    global dis
    global litro
    
    tem = float(input("Informe o tempo gasto (horas) -> "))
    vel = int(input("informe a velocidade média (km) -> "))

    dis = tem * vel# calcula a distância

    litro = dis / 12# calcula quantidade de combustível

# método para printar os valores  
def main():
    calc()
    print("Velocidade média...............: {} km".format(vel))
    print("Tempo gasto....................: {} horas".format(tem))
    print("Distância percorrida...........: {} km/horas".format(dis))
    print("Conbustível gasto..............: {:.2f} litros".format(litro))

# chama a função main
if __name__ == '__main__':
    main()
