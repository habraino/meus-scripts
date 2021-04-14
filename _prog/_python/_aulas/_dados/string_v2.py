# file_name: string_v2.py
'''
Nota: nesse exemplo só irá ser retornado (True/False) como resultado
'''
var = input("Digite qualquer coisa: ")

# verifica se está maúscula
print("Está em maúscula? {}".format(var.isupper()))

# verifica se está maúscula
print("Está em minuscula? {}".format(var.islower()))

# verifica se é numerico
print("É numerico? {}".format(var.isnumeric()))

# verifica se é alafabeto
print("É alafabetico? {}".format(var.isalpha()))

# verifica se é alfanumerico
print("É alfanumerico? {}".format(var.isalnum()))

# verifica se é decimal
print("É decimal? {}".format(var.isdecimal()))

# verifica se só contém espaços
print("Só contém espaços? {}".format(var.isspace()))

# verifica se é digito
print("É digito? {}".format(var.isdigit()))

# verifica se está em forma de titulocase
print("É título? {}".format(var.istitle()))

# verifica se é ascii
print("É da tabela ASCII? {}".format(var.isascii()))

# verifica se é imprimivél
print("É imprivél? {}".format(var.isprintable()))

