from random import randint

number = randint(0,4)

correct = False

english = ['rice', 'dog', 'chair', 'butterfly', 'fish']
japanese = ['gohan', 'inu', 'isu', 'chouchou', 'sakana']

guesses = []
guess = ""

print("Japanese guessing game. Guess the Japanese word for the word given in English.")

e_index = 0
j_index = 0

while not correct:
    guess = input(english[number]+': ')
    guesses.append(guess)
    if japanese.index(guess) == number:
        print('Correctt')
        correct = True
    else:
        print('Wrong')
        print(guess)
