from datetime import date

dia = int(input('Informe o dia do seu nascimento: '))
mes = int(input('Informe o mes em que você nasceu: '))
ano = int(input('Informe o ano em que você nasceu: '))

hY = date.today().year 
hM = date.today().month
hD = date.today().day

idade = hY - ano

if mes > hM:
    dM = mes - hM
    dD = dia - hD
    if dM > 1:
        print("Fantam {} meses e {} dias para seu aniversário de {} anos.".format(dM, dD, idade))
    else:
        print("Fantam {} mês e {} dias para seu aniversário de {} anos.".format(dM, dD, idade))
else:
    if dia > hD:
        dD = dia - hD 
    else:
        dD = hD - dia
    dM = hM - mes
    print('Você fez {} anos há {} meses e {} dias atras.'.format(idade, dM, dD))



