from random import randint

number = randint(0,15)

correct = False

guess = ""
guesses = []

while not correct:
    guess = int(input('Enter number: '))
    guesses.append(guess)
    if guess == number:
        print('Correct')
        correct = True
    elif guess > number:
        print('Loser! Try lower!')
        print(guesses)
    else:
        print('Loser! Try higher!')
        print(guesses)
    
        