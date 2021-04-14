#!python3
#phoneAndEmail.py -> Encontra o número de telefone e email numa clipboard
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # código de área
    (\s|-|\.)? # separador
    (\d{3}) # primeiros 3 dígitos
    (\s|-|\.) # separador
    (\d{4})  # últimos 4 dígitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
    )''', re.VERBOSE)

# cria regex para email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # nome do usuário
    @                   # simbolo @
    [a-zA-Z0-9.-]+      # nome do domínio
    (\.[a-zA-Z]{2,4})   # ponto seguido de outros carateres
)''', re.VERBOSE)

# Encontra as correspondências no texto do clipboard.
text = str(pyperclip.paste())
matches = list()

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copia os resultados para o clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email found.')

# texto a ser verificado
pyperclip.copy('It is my email: brayenstrong78@gmail.com and brayenstrong12@gmail.com and my phone number is 234-456-5665')

