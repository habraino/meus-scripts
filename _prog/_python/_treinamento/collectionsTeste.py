import collections as c

def conta(text):
    return c.Counter(text)

texto = input('Insira um texto: ').strip()

a = conta(text=texto)

for k, v in a.items():
    if k == ' ':
        k = 'space'
    print(k, ' = ', v)


