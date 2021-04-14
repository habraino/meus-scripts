# file_name: num_arbitrario_v1.py
'''
Nota: só utilizamos os números arbitário (*args) quando não sabemos o número exato de argumentos.
'''
def teste(arg, *args):
    print(f'Primeiro argumento normal: {arg}')
    for arg in args:
        print(f'Outro argumento: {arg}')

lista = ['Java', 'ObjectiveC', 'Lisp']
teste('Python', *lista)

