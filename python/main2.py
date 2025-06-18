"""
Iterables
An object/collection that can return its elements one at a time
allow it ot be iterated over a loop
"""

# num = (1,2,3,4,5)
#
# for number in num:
#     print(number, end = ' ')

# fruits = {'apple', 'banana', 'pear', 'watermelon', 'grape'}
#
# for fruit in fruits:
#     print(fruit)

# my_dic = {'A': 1, "B": 2, "C": 3}
#
# for key, value in my_dic.items():
#     print(f'{key} {value}')


"""
Membership operators
used to test if a value or variable is found in a sequence
(String, list, tuple, set, or dic)
"""

# word = "APPLE"
#
# letter = input("Guess a letter in the secret word: ")
#
# if letter in word:
#     print(f'There is a {letter}')
# else:
#     print(f'There is no {letter}')

# students = {"Ken", "Peter", "Andy"}
#
# student = input("Enter a name of a student: ")
#
# if student in students:
#     print(f'{student} is in the students list')
# else:
#     print(f'{student} is not in the students list')

# grades = {"Mike": 'S', "Drew": 'A', 'Todd': 'E'}
#
# student = input('Enter the name of student: ')
#
# if student in grades:
#     print(f'{student} grade is {grades[student]}')
# else:
#     print(f'{student} does not have grade')

# email = 'yeet@hotmail.com'
#
# if '@' in email and '.' in email:
#     print('valid email')
# else:
#     print('invalid email')

"""
list comprehension
A concise way to create list in python
[expression for value in iterable if condition]
"""

# # More to write
# doubles = []
# for i in range(1,11):
#     doubles.append(i*2)
#
# print(doubles)

# doubles = [i * 2 for i in range(1,11)]
# triples = [j * 3 for j in range(1,11)]
# squares = [k * k for k in range(1,11)]
#
# print(doubles)
# print(triples)
# print(squares)

# fruits = ['apple', 'banana', 'pear', 'watermelon', 'grape']
# # fruits = [fruit.upper() for fruit in fruits]
# fruits = [fruit[0] for fruit in fruits]
# print(fruits)

# nums = [1,2,3,4,5,-2,-4,-7]
# pos_num = [num for num in nums if num >= 0]
# neg_num = [num for num in nums if num < 0]
# even_num = [num for num in nums if num % 2 == 0]
# odd_num = [num for num in nums if num % 2 != 0]
#
# print(odd_num)
# print(even_num)
# print(pos_num)
# print(neg_num)

# grades = [85,72,99,23,43,100, 45]
# pass_grade = [grade for grade in grades if grade >= 60]
#
# print(pass_grade)

"""
Match-case statement (Switch)
an alt to using many elif statments
execute some code if a value matches a 'case'
much more clear syntax
"""

# def weekend(day):
#     match day:
#         case "Monday":
#             return 'False'
#         case "Tuesday":
#             return 'False'
#         case "Wednesday":
#             return 'False'
#         case "Thursday":
#             return 'False'
#         case "Friday":
#             return 'False'
#         case "Saturday":
#             return 'True'
#         case "Sunday":
#             return 'True'
#
# print(weekend('Monday'))

# def weekend(day):
#     match day:
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return 'False'
#         case "Saturday" | "Sunday":
#             return 'True'
#         case _:
#             return 'False'

# print(weekend('Sunday'))
# print(weekend('Monday'))

"""
module
a file containg code you want to incluide in your program
use import to include a module (java class)
useful to break up a large program resizable separate files
"""

# import math
# import math as m
# from math import pi
from math import e

# print(math.e)
# print(pi)

# a,b,c,d,e = 1,2,3,4,5
# print(math.e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)

# import example
#
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.square(3)
# result = example.circumference(5)
# result = example.area(9)
#
# print(result)

"""
Scopes
variable scope
scope resolution
local -> enclosed -> global -> built-in (LEGB)
"""

# def func1():
#     x = 1
#     print(x)

# def func1():
#     x = 2
#     def func2():
#         x = 1 # local to fun2
#         print(x)
#     func2()
# func1()

# def func1():
#     print(x)
#
# def func2():
#     print(x)
#
# x = 3
# func1()
# func2()

# from math import e
# def func1():
#     print(e)
#
# e = 3
#
# func1()

"""
if __name__ == __main__:
function and classes in this module can be resued
without the main block of code executing

ex
library = import library for functionality
when running libary direcrly display a help page
"""

# def main():
#     # code goes here
#     x = 2
#
# if __name__ == "__main__":
#     main()


# s =  '[[[]]]'
#
# pairs = ['()', '[]', '{}']
# max_pairs = (len(s) / 2) -1
#
# pair = ''
#
# if pair in pairs:
#     print(True)
#
# for index in range(len(s)):
#     pair = s[index] + s[(len(s) - 1) - index]
#     if index == max_pairs: break
#     if pair not in pairs:
#         print(f'{pair} not in {pairs}')
#     pair = ''
#
#
#     class Solution:
#         def isValid(self, s: str) -> bool:
#             pairs = ['()', '[]', '{}']
#             max_pairs = (len(s) // 2) - 1
#             pair = ''
#
#             if (len(s) % 2 != 0):
#                 return False
#
#             for index in range(len(s)):
#                 pair = s[index] + s[(len(s) - 1) - index]
#                 if index == max_pairs: break
#                 if pair not in pairs:
#                     return False
#                 pair = ''
#             return True

# s = '[[[]]]'
# s = '()[]{}'
# s = '(]'
# s = '()()()()[[]]'
# s = '[()()[)[}[]()]'
# s = ''
# def isValid(s: str) -> bool:
#     if (len(s) % 2 != 0):
#         return False
#
#     # count total opening and closing
#     parentheses = 0
#     square_bracket = 0
#     curly_braces = 0
#     #
#     # for index in s:
#     #     if index == '(' or ')':
#     #         parentheses += 1
#     #     elif index == '[' or ']':
#     #         square_bracket += 1
#     #     elif index == '{' or '}':
#     #         curly_braces += 1
#
#     for index in s:
#         match index:
#             case '(' | ')':
#                 parentheses += 1
#             case '[' | ']':
#                 square_bracket += 1
#             case '{' | '}':
#                 curly_braces += 1
#
#     if parentheses % 2 != 0:
#         return False
#
#     if square_bracket % 2 != 0:
#         return False
#
#     if curly_braces % 2 != 0:
#         return False
#
#     return True
#
# print(isValid(s))

# string = "apple     banana     cherry"
# # string = "kiwi"
# string = 'Hello World'
# string = "   fly me   to   the moon  "
# array = string.split(" ")
#
# i = 0
# while i < len(array):
#     if array[i] == "":  # Check if the element is an empty string
#         array.pop(i)  # Remove the element at index i
#     else:
#         i += 1  # Only increment i if no element was removed
# print(array) # Output: ['apple', 'banana', 'cherry']
#
# print(len(array[len(array)-1]))

