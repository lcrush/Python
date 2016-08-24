from random import randint

number = randint(0,4)

correct = False

guess = ""
guesses = ['mouse', 'horse', 'zebra', 'elephant', 'gnu']


while not correct:
    guess = input('Guess mouse, horse, zebra, elephant, or gnu. Enter animal: ')
    if guess == guesses[number]:
        print('Correct!')
        break
    else:
        print('Duh!')
        
    
        