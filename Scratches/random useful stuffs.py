# Random Jokes 


import pyjokes

joke = pyjokes.get_joke('en', 'neutral')

print(joke)

#############################

# some useful Modules

from collections import Counter, defaultdict

li = [1, 2, 3, 4, 4, 3, 5]

sentence = 'Thinking about python programming'
# counter helps to count the input , list and convert as dictionary with counts, it helps during Optimisation
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
# defaultdict used to add an optional infront of actual dictionary,
# which avoids error if the object which we calling is not in dictionary

print(dictionary['g']) 


#########################
from datetime import datetime, timedelta, date
# below line is to print today's date
print(datetime.today())
#(or)
print(datetime.now())
############

# below line is to get both start date and end date to execute the process
current_date = datetime.today().date()
start_date = current_date + timedelta(days=-2)
end_date = current_date

print('Start date : ', start_date)
print('End date : ', end_date)

#######################
# to print variable in reverse

a = 'Testing the Reverse method'
b = 'SingleWord'

print(a[::-1])
print(b[::-1])

#############################
# email validation:
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

u_email = input("Please Enter your email address: ")

email_add = pattern.search(u_email)

# print(email_add)

if not email_add:
    print('Please try again with full e-mail address')
else:
    print('Thank you!')
#############################

# *args and **kwargs
# *args accept multiple inputs in a function

def sum_func(*args):
    print(args)
    return sum(args)

print(sum_func(1,2,3))

## *kwargs

def sum_func(*args, **kwargs):
    total = 0
    for item in kwargs.values():  # grabbing the values 10, 15 and do sum 
        total += item
    return sum(args) + total


print(sum_func(1, 2, 3, 4, num1=10, num2=15))

##################################
