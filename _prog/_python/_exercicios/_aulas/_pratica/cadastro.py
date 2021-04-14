from os import system as s

users = []

while True:
    user = {}

    user['Name'] = input('Name: ')
    user['Age'] = int(input('Age: '))
    user['Residence'] = input('Residence: ')
    users.append(user)

    per = input('add new person? [y/n]: ').strip().lower()[0]

    if per == 'n':
        break
    else:
        s('cls')

# parte do programa que encarrega de mostrar as informações na tela
for i in users:
    print('******************************************')
    for k, v in i.items():
        print(f'{k}...................: {v}')
    print('******************************************')
       
