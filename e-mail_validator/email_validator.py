# re fullfills the requirements need to be checked 
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

u_email = input("Please Enter your email address: ")

email_add = pattern.search(u_email)

# print(email_add)

if not email_add:
    print('Please try again with full e-mail address')
else:
    print('Thank you!')
