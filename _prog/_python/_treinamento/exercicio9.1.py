file = open('teste.txt')

for i in file:
    if len(i) > 5 and 'i'.upper() in i:
        print(i)
    else:
        continue

