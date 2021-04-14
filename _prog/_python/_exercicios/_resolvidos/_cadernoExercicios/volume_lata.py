altura = float(input('Altura da lata -> '))
raio = float(input('Raio da lata -> '))

pi = 3.14159
volume = pi * (raio*raio) * altura

print('O volume da lata é de: {:.2f}'.format(volume))
