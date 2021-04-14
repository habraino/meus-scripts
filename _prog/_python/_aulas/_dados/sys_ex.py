'''
import sys
import os
from time import sleep as sp
'''
#nome = sys.argv[1]
#idade = sys.argv[2]

#limpar = lambda:os.system('clear')
#descanso = lambda:sp(2)

#print('Nome. {}\nIdade: {}'.format(nome, idade))
#descanso()
#limpar()

#soma = (lambda x, y: x + y)
#print(soma(2))

import _thread as t, time

def cont(test, cont):
	for i in range(1, cont):
		time.sleep(1)
		print("[{}] ==> [{}]".format(test, i))


for j in range(5):
	t.start_new_thread(cont, (j, 5))




