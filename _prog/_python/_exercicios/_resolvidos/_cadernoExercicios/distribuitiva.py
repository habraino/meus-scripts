a = int(input('1º valor -> '))
b = int(input('2º valor -> '))
c = int(input('3º valor -> '))
d = int(input('4º valor -> '))

soma = (a + b) + (a + c) + (a + d) + (b + c) + (b + d) + (c + d)
mult = (a * b) + (a * c) + (a * d) + (b * c) + (b * d) + (c * d)

print('A soma é: {}'.format(soma))
print('A multiplicação é: {}'.format(mult))
