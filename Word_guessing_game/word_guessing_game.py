import random
# word guessing game
name = input('Enter your Name: ')
print('Good luck! ', name)

words = ['apple', 'boat', 'car', 'dance', 'python', 'data', 'team', 'focus']

word = random.choice(words)  # function to choose random word from the list

print('Guess the characters: ')

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print(':(')
            failed += 1
    if failed == 0:
        print('You win!')
        print('The word is ', word)
        break
    guess = input('Guess a Character: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong Guess!')
        print('You have ', + turns, 'more guesses')

        if turns == 0:
            print('You Loose!')

