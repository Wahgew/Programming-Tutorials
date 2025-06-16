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

"""
Math + Arithmetic
"""

friends = 10
# friends = friends + 1
# friends += 1
# friends -= 2
# friends *= 3
# friends /= 2
# friends **= 2
remainder = friends % 2

# print(friends)
# print(remainder)

x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(y,3)
# result = max(x,y,z)
# result = min(x,y,z)

import math

# print(math.pi)
# print(math.e)
#
# x = 9
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

# calculate circumference

# radius = float(input('Enter the radius of a circle: '))
#
# circumference = 2 * math.pi * radius
#
# print(f'The circumference of the circle is: {round(circumference, 2)}cm')

# calculate area of circle
# radius = float(input('Enter the radius of a circle: '))
#
# area = math.pi * radius ** 2 # or pow(radius, 2)
#
# print(f'The area of the circle is: {area}cm^2')
#
# # hypotenuse of right triangle
#
# a = float(input('Enter side A: '))
# b = float(input('Enter side B: '))
#
# c = math.sqrt(pow(a,2) + pow(b,2))
#
# print(f'Side C = {c}')

"""
if statements + else
"""

# age = int(input('Enter your age: '))
#
# if age >= 100:
#     print('You are too old.')
# elif age < 0:
#     print('You are not born.')
# elif age >= 18:
#     print('You are now signed up')
# else:
#     print('You must be 18+ to sign up')
#
# response = input('Would you like food?: (Y/N):')
#
# if response == 'Y':
#     print('You are now food.')
# else:
#     print('You are not food.')
#
# name = input('Enter your name: ')
#
# if name == '':
#     print('You are not named.')
# else:
#     print(f'You are named {name}')
#
# for_sale = True
#
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")

"""
Python calculator
"""

# op = input('Enter an operation (+ - * /): ')
# num1 = float(input('Enter a first number: '))
# num2 = float(input('Enter a second number: '))
#
# result = 0
# if op == '+':
#     result = num1 + num2
# elif op == '-':
#     result = num1 - num2
# elif op == '*':
#     result = num1 * num2
# elif op == '/':
#     result = num1 / num2
# else:
#     print(f'{op} is not a valid operation!')
# print(round(result,4))

"""
Weight converter
"""

# weight = float(input('Enter your weight: '))
# unit = input('Kilograms or Pounds? (K or L): ')
#
# if unit == 'K':
#     weight = weight * 2.205
#     unit = 'Lbs'
#     print(f'Your weight is: {round(weight,1)} {unit}')
# elif unit == 'L':
#     weight = weight / 2.205
#     unit = 'Kgs'
#     print(f'Your weight is: {round(weight,1)} {unit}')
# else:
#     print(f'{unit} is not a valid unit')

"""
Temperature converter
"""

# unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# if unit == 'C':
#     temp = round((temp * 9) / 5 + 32, 1)
#     print(f'The temperature is: {temp}°F')
# elif unit == 'F':
#     temp = round(temp - 32 / 5 / 9, 1)
#     print(f'The temperature is: {temp}°C')
# else:
#     print(f'{unit} is not a valid unit')

"""
Logical operators
evaluate conditions (or, and, not)
or = at least one must be true
and = both conditions must be true
not = inverts the conditon (not False, not True)
"""

# OR
# temp = 25
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is ok")

# AND

# temp = 20
# is_sunny = True
#
# if temp >= 28 and is_sunny:
#     print('it is hot outside')
#     print('sunny')
# elif temp <= 0 and is_sunny:
#     print('it is cold outside')
#     print('sunny')
# elif 28 > temp > 0 and is_sunny:
#     print('it is warm outside')
#     print('sunny')

# NOT
# temp = 0
# is_sunny = False
#
# if temp >= 28 and not is_sunny:
#     print('it is hot outside')
#     print('Cloudy')
# elif temp <= 0 and not is_sunny:
#     print('it is cold outside')
#     print('Cloudy')
# elif 28 > temp > 0 and not is_sunny:
#     print('it is warm outside')
#     print('Cloudy')

"""
Conditional expressions
A one line  shortcut for the if-else statement (ternary operator)
print or assinge one of two values based on a condition
X if condition else Y
"""

# num = 1
# a = 6
# b = 7
# age = 25
# temp = 30
# user_role = 'admin'
#
# # print('positive' if num > 0 else 'negative')
# # result = "Even" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = 'Adult' if age >= 18 else 'Child'
# weather = 'HOT' if temp > 20 else 'COLD'
# access_lvl = "FUll access" if user_role == 'admin' else "Limited Access"
#
# print(access_lvl)
# print(status)
# print(max_num)
# print(min_num)
# # print(result)

# name = input('What is your name: ')
phone_number = '206-251-6666'

# result = len(name)
# result = name.find(" ")
# result = name.rfind('n') # finds the ending first
# name = name.capitalize()
# name = name.lower()
# name = name.upper()

# result = name.isdigit()
# result = name.isalpha()
# result = name.isalnum()

# result = phone_number.count('-')
# phone_number = phone_number.replace('-', '')
#
# print(phone_number)
# print(result)
# print(name)

"""
Validate user input exercise
"""

# username = input("Enter a username: ")
#
# username.find(" ")
#
# if len(username) > 12:
#     print('Your username cant be more than 12 characters')
# elif not username.find(" ") == -1:
#     print('Your username must contain only letters')
# elif not username.isalpha():
#     print('Your username cant contain numbers')
# else:
#     print(f'Your username is {username}')
#

"""
Indexiing = acessing elements of sequence using []
[Start : end : step]
"""

credit_num = "1234-2425-2334-9953"

# print(credit_num[0])
# print(credit_num[:4])
# print(credit_num[5:9])
# print(credit_num[5:])
# print(credit_num[-1])
# print(credit_num[::2])

# credit_num = credit_num[::-1]
#
# last_digit = credit_num[-4:]
# print(f'XXXX-XXXX-XXXX-{last_digit}')

"""
Format specifiers = {:flags} format value based on what
flags are inserted
"""

# price1 = 332422.14149
# price2 = -4444442.54
# price3 = 1112.45
#
# print(f'price1 = ${price1:+>15,.2f}')
# print(f'price2 = ${price2:+>15,.2f}')
# print(f'price3 = ${price3:+>15,.2f}')

"""
While loops
"""

# name = input('Enter name:')
#
# while name == "":
#     print('Name is empty')
#     name = input('Enter name:')
# else:
#     print(f'hello {name}')
#
# age = int(input('Enter age: '))
#
# while age < 0:
#     print('Age cant be negative')
#     age = input('Enter age:')
# print(f'Age is {age} years old')

# food = input('Enter food you like (q to quit):')
#
# while not food == 'q':
#     print(f'you like {food}')
#     food = input('Enter food you like (q to quit):')
# print('bye')

# num = int(input('Enter a number # between 1 - 10: '))
#
# while num < 1 or num > 10:
#     print(f'{num} is not a valid number')
#     num = int(input('Enter a number # between 1 - 10: '))
#
# print(f'{num} is a valid number')


"""
Compound Interest calculator 
"""

principle = 0
rate = 0
time = 0

while True:
    principle = float(input('Enter the principle amount: '))
    if principle < 0:
        print('Cant be less than zero')
    else:
        break

while True:
    rate = float(input('Enter the rate amount: '))
    if rate < 0:
        print('Cant be less than zero')
    else:
        break

while True:
    time = int(input('Enter the time in years : '))
    if time < 0:
        print('Cant be less than zero')
    else:
        break
print(principle, rate, time)

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} years is: ${total:.2f}')