# simple print
# comment tags
"""
This is a block comment
"""
from sympy.solvers.diophantine.diophantine import length

# print('I like pizza!')
# print("Using double quotes to print")

"""
Variables
"""
# Strings
first_name = 'Peter'
food = 'Rice'
email = 'testemail@hotmail.com'

# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f'Your email is {email}')

# Integers
age = 22
quantity = 3
students = 32

#
# print(f"Your age is {age}!")
# print(f"Your quantity is {quantity}!")
# print(f"Your class has {students}")

# Floats
# price = 10.99
# gpa = 3.92
# distance = 6.3443445

#
# print(f"The price is {price}")
# print(f'The gpa is {gpa}')
# print(f'The distance is {distance}')

# Booleans
is_unemployed = True
is_student = False
for_sale = True
is_online = True

# print(f'Are you a student?: {is_student}')
#
# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")
#
# if for_sale:
#     print("You are on sale")
# else:
#     print("You are not on sale")
#
# if is_online:
#     print("You are online")
# else:
#     print("You are not offline")

"""
TypeCasting
the process of converting variables to another type
"""

# name = "Peter Madin"
# age = 22
# gpa = 3.81
# is_student = False
#
# gpa = int(gpa)
# age = float(age)
# age = str(age)
# name = bool(name)
#
# print(name) # false if string is empty
# print(gpa)
# print(age)
# print(type(age))

"""
Input = A function that prompts the user to enter data
Returns the entered data as a string
"""

# name = input('What is your name?: ')
# age = int(input('How old are you?: '))
#
# age += 1
#
# print(f'Hello, {name}')
# print('Happy Birthday!')
# print(f'You are {age} years old.')

# Exercise 1 Rectangle Area calc

# length = float(input('Enter Length: '))
# width = float(input('Enter Width: '))
# area = length * width
#
# print(f"The area is: {area}cm²")

# Exercise 2 Shopping cart program

# item = input('What item would you like to buy?: ')
# price = float(input('Enter price: '))
# quantity = int(input('How many items would you like to buy?: '))
# total_price = price * quantity
#
# print(f"The total price is: ${total_price} And you bought {quantity} items.")

"""
Madlibs Game
words game where you create a story
by filling in blanks with random words
"""

# adjective1 = input('Enter an adjective: ')
# noun1 = input('Enter a noun: ')
# adjective2 = input('Enter an adjective: ')
# verb1 = input('Enter a verb: ')
# adjective3 = input('Enter an adjective: ')
#
#
# print(f"\nToday I want to to a {adjective1} gym.")
# print(f'At the gym I saw {noun1}')
# print(f'{noun1} was {adjective2} and {verb1}')
# print(f"I was {adjective3}")