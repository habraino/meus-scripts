from time import sleep
import os, sys

def clear():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')


print('*'*65)
print('\t\t\t\033[1;33mWELCOME TO ENIGMA\033[m')
print('*'*65)

input('\033[1;32mprees <enter> to continue...\033[m')

print('\033[1;32mInitianizing...\033[m')
sleep(5)

clear()

# pega letras de 'a-z'
letters = list()
for x in range(97, 123):
    letters.append(chr(x))

    
# crio duas listas vazias
letter = list()
number = list()

msg = str(input('Type the text: ')).strip().lower()
key = str(input('Type the key: ')).strip()

# caso usuário digite chave negativo
while int(key) < 0:
    print('\033[1;31mPlease enter with key low of zero.\033[m')
    key = str(input('Type the key: ')).strip()


clear()

# prepara a msg para adicionar na lista
join1 = ''.join(msg.split())
for i in join1:
    letter.append(i)

# prepara a chave para adicionar na lista
join2 = ''.join(key.split())
for j in join2:
    number.append(j)

print("Message:",letter)

position = 0 # posição


try : # tenta executar
    # executa essa parte
    for i in range(0, len(letter)):
        posi = 0
        
        if letter[i] in letters:
            for p in range(0, len(letters)):
                if letter[i] == letters[p]:
                    posi = p + int(number[i])# aqui tem um problema na contação
                
            letter[i] = letters[posi]

        position += 1


except IndexError:# caso ocorrer erro
    # executa essa parte
    while (position != len(letter)):
        for i in range(0, len(number)):  
            posi1 = 0  
            
            if letter[position] in letters:
                for p in range(0, len(letters)):
                    if letter[position] == letters[p]:
                        posi1 = p + int(number[i])
                
                letter[position] = letters[posi1]

            position += 1

            # se posição for igual a número do tamanho da lista2 para a execução
            if position == len(letter):
                break

            if position == len(number): # se posição for igual a tamanho d lista1 cont recebe 0
                position = 0 # posição recebe 0
                
                # efetua um novo loop
                for j in range(position, len(letter)):
                    posi2 = 0
                    
                    if letter[j] in letters:
                        for p in range(0, len(letters)):
                            if letter[j] == letters[p]:
                                posi2 = p + int(number[position]) 
                                
                            
                        letter[j] = letters[posi2]

                    position += 1

print('\033[1;32mCodding...\033[m')
sleep(5)
print('\033[1;4;33mCifra was successfully!\033[m')
print("Cifred: ",letter)        



