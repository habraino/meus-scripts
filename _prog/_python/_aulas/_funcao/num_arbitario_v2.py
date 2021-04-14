# file_name: num_arbitario_v2.py

'''
Nota: O uso de "**kwargs" é bem útil para manipular os dicionários em python
'''
def function(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}.........: {v}')

dic = {'Nome':'Brayen', 'Idade':20, 'Morada':'Neves'}

function(**dic)

