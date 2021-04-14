from random import randint

guessesTaken = 0
guess = 0

my_name = input('Hello, what is your name? ')

number = randint(1, 10)
print('Well %s I thinking in one munber between 1 and 10.'%my_name)

while guessesTaken <= 5:
    guess = int(input('Take a guess: '))
    guessesTaken += 1

    if guess > number:
        print('Your guess is so high.')
    elif guess < number:
        print('Your guess is so low.')

    if guess == number:
        break


if guess == number:
    print('Good Job %s! You guessed my number in %d guesses.'%(my_name, guessesTaken))

if guess != number:
    print('Nope! The number I was thinking is %s.'%number)


