# simple print
# comment tags
"""
This is a block comment
"""
import time

from sympy.concrete.guess import guess
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

# principle = 0
# rate = 0
# time = 0
#
# while True:
#     principle = float(input('Enter the principle amount: '))
#     if principle < 0:
#         print('Cant be less than zero')
#     else:
#         break
#
# while True:
#     rate = float(input('Enter the rate amount: '))
#     if rate < 0:
#         print('Cant be less than zero')
#     else:
#         break
#
# while True:
#     time = int(input('Enter the time in years : '))
#     if time < 0:
#         print('Cant be less than zero')
#     else:
#         break
# print(principle, rate, time)
#
# total = principle * pow((1 + rate / 100), time)
# print(f'Balance after {time} years is: ${total:.2f}')

"""
For loops
execute a block of code a fixed number of times.
"""

# credit_num = "1234-2425-2334-9953"
#
# for i in credit_num:
#     print(i)

# for i in range(1,21):
#     if i == 13:
#         continue
#     else:
#         print(i)
#
#
# for i in range(1,21):
#     if i == 13:
#         break
#     else:
#         print(i)


"""
Count down timer program
"""

# import time
#
# my_time = int(input("Enter the time in seconds: "))
#
# for i in range(my_time, 0, -1):
#     seconds = i % 60
#     minutes = i // 60
#     hours = i // 3600
#     print(f'{hours:02}:{minutes:02}:{seconds:02}')
#     time.sleep(1)
#
# print("Times Up")


"""
Nested loops 
A loop withing another loop (outer, inner)
"""

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter the symbol: ")
#
#
# for j in range(rows):
#     for i in range(columns):
#         print(symbol, end='')
#     print()

"""
Collection
single 'variable' used to store multiple values
list = [] ordered and changeable
set = {} unordered and immutable
Tuple = () ordered and unchanged
"""

# fruits = ['apple', 'banana', 'orange', 'pear']
fruits = {'apple', 'banana', 'orange', 'pear'}

# print(dir(fruits))
# print(len(fruits))
# print('banana' in fruits)
# print('apple' in fruits)

# fruits[0] = 'kiwi'
# fruits.append('kiwi')
# fruits.remove('apple')
# fruits.insert(0, 'berry')
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index('pear'))
# print(fruits.count('apple'))

# print(fruits)
# print(fruit[::2])
# for fruit in fruits:
#     print(fruit)

"""
Shoping cart program
"""

# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input('Enter food (q to quit): ')
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f'Enter price of a {food}: $'))
#         foods.append(food)
#         prices.append(price)
# print(5*'-', 'YOUR CART', 5 *'-')
#
# for food in foods:
#     print(food, end = " ")
#
# for price in prices:
#     total += price
# print(f'\nFinal total: ${total}')

"""
2D list/ matrix
"""


# fruits =     ['apple', 'banana', 'orange', 'pear']
# vegetables = ['tomato', 'celery', 'onion']
# meats =      ['steak', 'chicken', 'pork']
#
# groceries = [fruits, vegetables, meats]
#
# # fruits[0] = 'kiwi'
# # print(fruits)
# # print(groceries[2][1])
#
# for collection in groceries:
#     for food in collection:
#         print(food, end = ' ')
#     print()

# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ('*',0,'#'))
#
# for row in num_pad:
#     for num in row:
#         print(num, end= ' ')
#     print()


"""
Python quiz game
"""

# questions = ('What is the capital of France?: ',
#             'Who wrote the play Romeo and Juliet?: ',
#             'What is the largest planet in our solar system?: ',
#             'In what year did the Titanic sink?: ',
#             'What element does "O" represent on the periodic table?: ')
#
# options = (
#     ('A. Paris', 'B. London', 'C. Berlin', 'D. Madrid'),
#     ('A. William Shakespeare', 'B. Charles Dickens', 'C. J.K. Rowling', 'D. Jane Austen'),
#     ('A. Earth', 'B. Jupiter', 'C. Saturn', 'D. Mars'),
#     ('A. 1912', 'B. 1905', 'C. 1923', 'D. 1898'),
#     ('A. Oxygen', 'B. Hydrogen', 'C. Nitrogen', 'D. Carbon'))
#
# answers = ('A','A','B','A','A')
# guesses = []
# score = 0
# question_number = 0
#
# for question in questions:
#     print(50*'-')
#     print(question)
#     for option in options[question_number]:
#         print(option)
#
#     guess = input("Enter (A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_number]:
#         score += 1
#         print('Correct!')
#     else:
#         print('Incorrect!')
#         print(f'{answers[question_number]} was correct.')
#     question_number += 1
#
# print('answers:', end ='')
# for answer in answers:
#     print(answer, end =' ')
# print()
#
# print('guesses', end ='')
# for guess in guesses:
#     print(guess, end =' ')
# print()
#
# score = int(score / len(questions) * 100)
# print(f'score: {score}%')

"""
dictionary
Collection of {key:value} pairs (so java hashmap)
order anc changeable no dups
"""

capitals = {'USA': 'Washingtong D.C',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals.get('USA'))
# print(capitals.get('Japan'))
#
# if capitals.get('japan'):
#     print('that capital exist')
# else:
#     print('that capital doesn\'t exist')
# # capitals.update({'Germany': 'Berlin'})
# capitals.pop('China')
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
#
# print(capitals)
# print(keys)
#
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)
#
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# # print(items)
#
# for key, value in capitals.items():
#     print(f'{key}: {value:}')

"""
Concession stand program
"""

# menu = {
#     "Pizza Margherita": 8.99,
#     "Burger and Fries": 6.50,
#     "Spaghetti Carbonara": 10.00,
#     "Caesar Salad": 7.25,
#     "Grilled Chicken Sandwich": 7.75,
#     "Fish and Chips": 9.50,
#     "Vegetable Stir Fry": 8.00,
#     "Chocolate Cake": 4.50
# }
#
# cart = []
# total = 0
# print('------ MENU ------')
# for key, value in menu.items():
#     print(f'{key:25}: ${value:.2f}')
# print(50*'-')
#
# while True:
#     food = input('Select an item (q to quit): ')
#     if food == 'q' or food == 'Q':
#         break
#     elif menu.get(food)is not None:
#         cart.append(food)
# # print(cart)
#
# for food in cart:
#     total += menu.get(food)
#     print(food, end = ' ')
#
# print()
# print(f'Total is ${total:.2f}', end = ' ')

"""
Random guess number
"""
import random
# low = 1
# high = 100
# options = ('rock', 'paper', 'scissor')
# cards = ['2','3','4','5','6','7','8','9']


# number = random.randint(low,high)
# number = random.random()
# option = random.choice(options)
# random.shuffle(cards)

# print(cards)
# print(options)
# print(number)

# lowest_num = 1
# highest_num = 100
# guesses = 0
# is_running =  True
#
# ans = random.randint(lowest_num, highest_num)
#
# print('Number guessing game')
# print(f"Select a number between {lowest_num} and {highest_num}")
#
# while is_running:
#     guess = input("Enter Your Guess: ")
#
#     if guess.isdigit():
#         guess = int(guess)
#         guesses+= 1
#
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Select a number between {lowest_num} and {highest_num}")
#         elif guess < ans:
#             print('Too low')
#         elif guess > ans:
#             print('Too high')
#         else:
#             print(f'Congratulations, the answer was {ans}')
#             print(f'Your guesses was {guesses}')
#             is_running = False
#     else:
#         print('invalid guess, try again')
#         print(f"Select a number between {lowest_num} and {highest_num}")


"""
Rock Paper Scissors game
"""

# import random
#
# options = ('rock', 'paper', 'scissors')
#
# running = True
#
# while running:
#
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input('Enter a choice (Rock(R), Paper(P), Scissors(S)): ')
#     if player == computer:
#         print('Draw')
#     elif player == 'rock' and computer == 'scissors':
#         print('You win!')
#     elif player == 'scissors' and computer == 'paper':
#         print('You Win!')
#     elif player == 'paper' and computer == 'rock':
#         print('You Win!')
#     else:
#         print('You Lose!')
#     if not input('play again? (y/n): ').lower().startswith('y'):
#         running = False
#
# print(f'player: {player}')
# print(f'computer: {computer}')

# import random
#
# dice_art = {
#     1: '⚀',
#     2: '⚁',
#     3: '⚂',
#     4: '⚃',
#     5: '⚄',
#     6: '⚅',
# }
#
# dice = []
# total = 0
# num_of_dice = int(input('How many dices?: '))
#
# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))
#
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
#
# for die in dice:
#     total += die
# print(f'The total is: {total}')


"""
functions
A block of resuable code palce () after the function name to invoke it
"""

# def happy_birthday(name, age):
#     print('Happy Birthday to', name)
#     print(f'You are {age} old!')
#     print('Happy Birthday to', name)
#     print()
#
# happy_birthday('andy', 20)
# happy_birthday('Russia', 20)
# happy_birthday('Joe', 32)
#
# def display_invoice(username, amount, due_date):
#     print('Your invoice is', amount)
#     print(f'Your bill of ${amount:.2f} is due {due_date}.')
#
# display_invoice('Andussy', 40.03, '04/02')

"""
Return
statement used to end a function
and send a result back to the caller
"""

# z = 0
#
# def add(x,y):
#     z = x + y
#     return z
#
#
# def sub(x,y):
#     z = x + y
#     return z
#
# def multiply(x,y):
#     z = x * y
#     return z
#
# def divide(x,y):
#     z = x / y
#     return z
#
# print(add(1,2))
# print(multiply(1,2))
# print(divide(1,2))
# print(sub(2,2))
#
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return f'{first} {last}'
#
# full_name = create_name('Andy', 'whang')
#
# print(full_name)

"""
default arguments
A default valuie for certain params
deafult is used when arg is omitted
make fucntions more flexiable, reduces # of args
"""

# def net_price(list_price, discount=0, tax=0.10):
#     return list_price * (1 - discount) * (1 + tax)
#
# # print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))
#
# def count(end, start=0):
#     for i in range(start, end+1):
#         print(i)
#         time.sleep(1)
#     print("DONE!")
# count(30, 20)

"""
keyword arguments
and arg preceded by identifier
order of arguments dont matter
"""

# def hello(greeting, title, first, last):
#     print(f'{greeting} {title} {first} {last}')

# print(hello("hello", first='Andy', title='Dr.', last='Whang'))
# hello('hello', 'Mr', last='john', first='Jerry')

# for i in range(1,11):
#     print(i, end = ' ') # end is the keword

# print('1','2','3', sep = ' ')

# def get_phone(country, area, first, last):
#     return f'{country}-{area}-{first}-{last}'
#
# phone_number = get_phone(country=1, area=206, first=276, last=4242)
#
# print(phone_number)

"""
*args = allows you to pass multiple non-key arguments
**kwargs = allows you to pass multipule keyword-arguments
* unpacking operator
"""

# def add(*args):
#     total = 0
#     for arg in args:
#         total+= arg
#     return total
#
# print(add(1,2,3,7,6,6,4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end= ' ')
#
# display_name("Andy",'Gerald', 'Wang')

# def print_address(**kwargs):
#     for keys, value in kwargs.items():
#         print(f'{keys}: {value}')
#
# print_address(street='123 north ST',city='Atlanta', state='Georgia', apt ='304')

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end =' ')
#     print()
#
#     if 'apt' in kwargs:
#         print(f'{kwargs.get('street')} {kwargs.get('apt')}')
#         print(f'{kwargs.get('city')} {kwargs.get('state')}')
#     elif 'pobox' in kwargs:
#         print(f'{kwargs.get('street')}')
#         print(f'{kwargs.get('pobox')}')
#
#     else:
#         print(kwargs.get('street'))
#
# shipping_label("Andy",'Gerald', 'Wang', street ='2837 Cum zone St.', pobox = 'PO. BOX #322', state='oregon', city = 'portland')