# Basic Calculator
# Step1: Asking user to select operation to perform
operation = input('Would you like to Add/Subtract/Multiple/Divide?: ').lower()
print(f'You chose : {operation}')

# Step2: ask numbers, alter order matters for sub and divide
if operation == 'subtract' or operation == 'divide':
    print('Please keep in mind, that the order of numbers matter.')

num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))

print(f'1st number is : {num1}')
print(f'2nd number is : {num2}')

# Step3: setup try except for Maths operation
try:
    if operation == 'add':
        result = num1 + num2
        print(f'{num1} + {num2} is {result}')
    elif operation == 'subtract':
        result = num1 - num2
        print(f'{num1} - {num2} is {result}')
    elif operation == 'multiple':
        result = num1 * num2
        print(f'{num1} * {num2} is {result}')
    elif operation == 'divide':
        result = num1/num2
        print(f'{num1}/{num2} is {result}')
    else:
        print(f'Sorry, {operation} is not a operation, Please try again!')
except:
    print('Improper numbers, Please try again!')
