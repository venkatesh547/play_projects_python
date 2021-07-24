import random
import math

# taking inputs
lower = int(input('Enter Lower Bound:- '))
upper = int(input('Enter Upper Bound:- '))

# generate random number based on lower and upper bound
x = random.randint(lower, upper)
print("\n\tYou have only ", round(math.log(upper - lower + 2, 2)), " chances left")

count = 0  # initial count

while count < math.log(upper - lower + 2, 2):
    count += 1
    guess = int(input('Guess the number :- '))

    if x == guess:
        print('Congratulation you did it in ', count, ' try')
        break  # once guessed, loop will break
    elif x > guess:
        print('You guessed too small!')
    elif x < guess:
        print('You guessed too high!')

if count >= math.log(upper - lower + 2, 2):
    print('\nThe number is ', x)
    print('\tBetter luck next time!')
