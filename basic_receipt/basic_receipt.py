# Basic Bill Project
# Product and Price list

p1_name, p1_price = 'Chocolates', 500.00
p2_name, p2_price = 'Laptop', 2000.00
p3_name, p3_price = 'Books', 300.00

# Shop details
shop_name = 'VV Mart'
shop_address = '22, VV Building, OMR Road,'
shop_city = 'Chennai, TN'

# ending message
end_message = 'Thank you for Shopping with us!'

# Top border design
print('*' * 50)

# Print shop info
print('\t\t{}'.format(shop_name))
print('\t\t{}'.format(shop_address))
print('\t\t{}'.format(shop_city))

# printing a line separation
print('-' * 50)

# header for item section
print('\tProduct Name\t Price')

# statement for each item
print('\t{}\t\t${}'.format(p1_name.title(), p1_price))
print('\t{}\t\t\t${}'.format(p2_name.title(), p2_price))
print('\t{}\t\t\t${}'.format(p3_name.title(), p3_price))

# printing a line separation
print('-' * 50)

# header section for Title
print('\t\t\t\t\tTotal')

# Calculation
total = p1_price + p2_price + p3_price
print('\t\t\t\t\t${}'.format(total))

# line separation
print('-' * 50)

# Thank you message
print('\n\t{}\n'.format(end_message))

# bottom border line
print('*' * 50)

##########

## using f string type

# Basic Bill Project
# Product and Price list

p1_name, p1_price = 'Chocolates', 500.00
p2_name, p2_price = 'Laptop', 2000.00
p3_name, p3_price = 'Books', 300.00

# Shop details
shop_name = 'VV Mart'
shop_address = '22, VV Building, OMR Road,'
shop_city = 'Chennai, TN'

# ending message
end_message = 'Thank you for Shopping with us!'

# Top border design
print('*' * 50)

# Print shop info
print(f'\t\t{shop_name}')
print(f'\t\t{shop_address}')
print(f'\t\t{shop_city}')

# printing a line separation
print('-' * 50)

# header for item section
print('\tProduct Name\t Price')

# statement for each item
print(f'\t{p1_name.title()}\t\t${p1_price}')
print(f'\t{p2_name.title()}\t\t\t${p2_price}')
print(f'\t{p3_name.title()}\t\t\t${p3_price}')

# printing a line separation
print('-' * 50)

# header section for Title
print('\t\t\t\t\tTotal')

# Calculation
total = p1_price + p2_price + p3_price
print(f'\t\t\t\t\t${total}')

# line separation
print('-' * 50)

# Thank you message
print(f'\n\t{end_message}\n')

# bottom border line
print('*' * 50)


