import random

user_input = input("Enter your choice [rock, paper, scissor]: ")
possible_actions = ['rock', 'paper', 'scissor']
computer_action = random.choice(possible_actions)
print(f'You chose : {user_input}, Computer chose : {computer_action}')


if user_input == computer_action:
    print(f'You and Computer both selected{user_input}, Its a tie!!')
    
    # few more lines to add
