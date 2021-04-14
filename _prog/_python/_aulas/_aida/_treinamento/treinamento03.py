'''
Implemente um algoritmo em Python que pede para Usuário fornecer dois números e indique se são iguais ou se são diferentes. Mostre o maior e o
menor (nesta sequência).
'''

print('*'*55)
print('\t\tAnalisando dois números')
print('*'*55)

num1 = int(input('Primeiro número -> '))
num2 = int(input('Segundo número -> '))

# verifica os números
if num1 == num2:
    print('{} e {} são iguais.'.format(num1, num2))
else:
    print('{} e {} são diferentes.'.format(num1, num2))    

# verifica o maior e menor
if num1 > num2:
    print('{} é maior\n{} é menor.'.format(num1, num2))
elif num2 > num1:
    print('{} é maior\n{} é menor.'.format(num2, num1))

