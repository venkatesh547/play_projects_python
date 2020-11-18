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


# below line is to get both start date and end date to execute the process
current_date = datetime.today()
start_date = current_date + timedelta(days=-2)
end_date = current_date

print('Start date : ', start_date)
print('End date : ', end_date)
