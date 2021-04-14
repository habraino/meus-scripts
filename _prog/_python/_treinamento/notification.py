'''import notify2 as nt
from time import *

# tempo em segundos!
time = 60

nt.init('app_name')

i = nt.Notification('AVISO', 'Não te esqueças de estudar!!')
i.show()

# depois de 5 minutos avisa para estudar
time *= 5
sleep(time)
av = nt.Notification('ALERTA', 'Então já começou a estudar?')
av.show()

contador = 1

while True:
    # depois de 30 minutos, notifica para pausar por 5 mim
    time = 60
    time *= 30
    sleep(time)
    pausa = nt.Notification('PAUSA', 'Pausa de 5 minutos!!')
    pausa.show()

    # depois de 30 minutos, notifica para voltar a estudar
    time = 60
    time *= 5
    sleep(time)
    retorno = nt.Notification('RETORNO', 'Hora de continuar os estudos!!')
    retorno.show()

    # caso contador % por 5 for igual o, fim da primeira sessão do estudo
    if contador % 5 == 0:
        pausa = nt.Notification('PAUSA', 'Pausa de 30 minutos!!')
        pausa.show()

        time = 60
        time *= 30
        sleep(time)
        retorno = nt.Notification('RETORNO', 'Hora de continuar os estudos!!')
        retorno.show()
            
    contador += 1
'''

