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
