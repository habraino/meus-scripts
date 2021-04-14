def in_bisect():
    try:
        lista = ['Ana', 'Maria', 'Joana', 'Rita', 'Marcos', 'Brayen', 'Hebraino', 'Jivaldo', 'Edgar']
        lista.sort()
        pal = input('Qual nome desejas procurar? ')

        print("Encontrado da posição:",lista.index(pal))
    except ValueError:
        print(None)

if __name__ == '__main__':
    in_bisect()

    
