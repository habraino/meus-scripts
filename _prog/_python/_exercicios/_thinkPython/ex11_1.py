def read_word():
    d = dict()
    with open('word.txt') as file:
        for i in file.readlines():
            i = i.lower().strip()
            if i not in d:
                d[i] = None

    busca = input('O que desejas buscar? ').strip().lower()
    if busca in d:
        return True
    return False

if __name__ == '__main__':
    print(read_word())
    
