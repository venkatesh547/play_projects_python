from random import randint
from IPython.display import clear_output

guessed = False
number = randint(0, 100)
guesses = 0

while not guessed:
    ans = input('Try to guess the number I am thinking of!: ')

    guesses += 1
    clear_output( )

    if int(ans) == number:
        print('Congrats! You guessed it correctly!!')
        print('It took you {} guesses!'.format(guesses))
        break

    elif int(ans) > number:
        print('The number is lower than what you guessed. ')

    elif int(ans) < number:
        print('The number is greater than what you guessed. ')
        
        
# 2nd Method:

from random import randint

ans = randint(1, 10)

while True:
    try:

        guess = int(input('Guess a number from 1 to 10 :  '))
        if 0 < guess < 11:
            if guess == ans:
                print('You are Awesome!')
                break
            else:
                print('Try again!')
        else:
            print('number should be 1 to 10')
    except ValueError:
        print('Please enter a number!')
        continue










