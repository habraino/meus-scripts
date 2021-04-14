tempo_gasto = int(input('Informe o tempo gasto (horas) -> '))
vm = int(input('Informe a velocidade media (Km) -> '))

distancia = tempo_gasto * vm
litros_usados = distancia / 12

print('Velocidade Média...................: {} km'.format(vm))
print('Tempo Gasto........................: {} horas'.format(tempo_gasto))
print('Distância percorrida...............: {} km/h'.format(distancia))
print('Litros gasto durante viagem........: {:.2f} litros'.format(litros_usados))
