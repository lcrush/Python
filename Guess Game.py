from random import randint

guesses = []

number = randint(0,25)

guess = input('Enter a number: ')

if guess ==number:
    print('Got it!')
else:
    print('Loser!')

correct = False

while not correct:
    guess = input('Enter a number: ')
    guesses.append(guess)
    if guess == number:
        print('Correct')
        correct = True
    else:
        print('Wrong! Try again')
