# file_name: string.py

'''
Nota: com esse exemplo tu irá minima noção de como trabalhat com "strings"

E o uso de input("") é mesmo que str(input("")), só quando para stings
'''

var = input("Digite qualquer coisa: ")# lê qualquer coisa pelo teclado

# retorna o tamanho da 'palavra' informada
print("O tamanho total é: {}".format(len(var)))

# imprime tudo em maiúscula
print("{} em maiúscula fica: {}".format(var, var.upper()))

# imprime tudo em maiúscula
print("{} em minúscula fica: {}".format(var, var.lower()))

# remove todos os espaços e carateres ASCII
print("Tirando os espaços fica: {}".format(var.strip()))

# conta quantas letras 'a' foram digitadas
print("Quantas letras 'a' foram digitadas? {}".format(var.count('a')))

# procura por letra 'a' e retorna a posição da primeira que encontrar
print("A primeira letra 'a' está em que posição? {}".format(var.find('a')))

# procura por última letra 'a' e retorna sua posição
print("A última letra 'a' está em que posição? {}".format(var.rfind('a')))

# imprime tudo separado
print("Todo separado fica: {}".format(var.split()))

# imprime tudo junto
b = var.split()# separa tudo e armazena em 'b'
junto = ''.join(b)# ajunta todo e armazena em 'junto'
print("Todo junto fica: {}".format(junto))

# imprima tudo em forma de título
print("Em forma de títuloCase fica: {}".format(var.title()))

# imprime a palavra/frase com primeira letra sendo maúscula
print("Primeira letra maíuscula: {}".format(var.capitalize()))

# troca toda letra 'a' caso encontre para '@'
print("Todo 'a' trocado fica: {}".format(var.replace('a', '@')))
