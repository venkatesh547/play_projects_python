# to calculate area of Rectnagle
# hint area = width * height

width = int(input('Enter the width of Rectangle: '))
height = int(input('Enter the height of Rectnagle: '))

area = width * height

print(f'area is {area} sqft')
######################################################################################

# to print variable in reverse

a = 'Testing the Reverse method'
b = 'SingleWord'

print(a[::-1])
print(b[::-1])

######################################################################################

# to check if both words are same
ans1 = input('Please enter a word: ')

ans2 = input('Please enter 2nd word: ')

if ans1.lower() == ans2.lower():
    print('Both words are same!')

elif ans1.lower() != ans2.lower():
    print('Both words are not same!')
######################################################################################

