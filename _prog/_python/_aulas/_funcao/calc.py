# file_name: calc.py

def calc(x, y):
    return {'soma':x + y, 'subtração':x - y, 'multiplicação':x * y, 'divisão':x / y}

res = calc(12, 6)

for key in res:
    print(f'{key}: {res[key]}')

