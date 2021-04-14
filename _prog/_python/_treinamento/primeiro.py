from random import randint

comp = randint(1, 10)
acerto = False
tent = 0
while not acerto:
    player = int(input('chut one number between (1 - 10): '))
    tent += 1
    if comp == player:
        print('You win.')
        acerto = True
    else:
        if player > comp:
            print('Please chut one number low.')
        elif player < comp:
            print('Please chut one number high.')

print('Tent: {}'.format(tent))

