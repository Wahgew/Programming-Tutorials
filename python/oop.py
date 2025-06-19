"""
Object
a bundle of related attributes (variables) and method (functions)

class = (blueprint) used to design the structure and layout of an object
"""

# from car import Car
#
# car1 = Car('red', 'Supra', 2025, True)
# car2 = Car('blue', 'Tesla', 2020, False)
#
# # print(car1.color)
# # print(car1.model)
# # print(car1.year)
# # print(car1.for_sale)
#
# car1.drive()
# car1.stop()
#
# car2.drive()
# car2.stop()
# car1.details()
# car2.details()

"""
class variables
shared among all the instances of a class
defined outside the consturctor
allow you to share data among all objects created from that class
"""

# class Student:
#     class_year = 2025
#     num_students = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1
#
# s1 = Student("John", 22)
# s2 = Student("Andy", 23)
# s3 = Student("Mike", 44)
# s4 = Student("leroy", 18)
#
# # print(s1.name, s1.age)
# # print(s2.name, s2.age)
# print(s1.class_year, s2.class_year, s3.class_year)
# print(Student.class_year) #better to use the class name rather than the object instance
# print(Student.num_students)
#
# print(f'My graduating class of {Student.class_year} has {Student.num_students} students')
# print(s1.name, s2.name, s3.name, s4.name, sep= '\n')

"""
Inheritance
Allows a class to inherit attributes and methods from another class
helps with code resuablity and extenstion
class Child(Parent)
"""

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.alive = True
#
#     def eat(self):
#         print(f'{self.name} eats')
#
#     def sleep(self):
#         print(f'{self.name} sleeps')
#
# class Dog(Animal):
#     def speak(self):
#         print('Woof')
#
# class Cat(Animal):
#     def speak(self):
#         print('Meow')
#
# class Mouse(Animal):
#     def speak(self):
#         print('Squeek')
#
# dog = Dog('Max')
# cat = Cat('Milk')
# mouse = Mouse('Jerry')
#
# dog.eat()
# cat.sleep()
# mouse.eat()
# cat.speak()
# mouse.speak()
# dog.speak()

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator): # multi level
#     pass
#
# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("unc")
#
# hawk.hunt()
# fish.flee()
# fish.hunt()
#
# rabbit.eat()
# rabbit.sleep()
#
# fish.eat()
# fish.sleep()

"""
super()
used in a child class to call method from a parent class (superclass)
"""

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def detail(self):
#         print(f'It is {self.color} and {'filled' if self.is_filled else 'not filled'}')
#
# class Circle(Shape):
#     def __init__(self, radius, color, filled):
#         super().__init__(color, filled)
#         self.radius = radius
#         self.filled = filled
#
#     def detail(self):
#         print(f'The circle with an area of radius {self.radius} is {3.14 * self.radius * self.radius:.2f}cm^2')
#
# class Square(Shape):
#     def __init__(self, width, color, filled):
#         super().__init__(color, filled)
#         self.width = width
#         self.filled = filled
#
#
# class Triangle(Shape):
#     def __init__(self, width, height, color, filled):
#         super().__init__(color, filled)
#         self.width = width
#         self.height = height
#
# circle = Circle(3, 'red', True)
# square = Square(20, 'blue', True)
# triangle = Triangle(20, 440, 'blue', False)
#
# print(triangle.width)
# print(triangle.height)
# print(triangle.color)
# print(square.width, square.color, square.filled)
# print(circle.radius)
# print(circle.is_filled)
# print(circle.color)
# circle.detail()
# triangle.detail()
# square.detail()

"""
Polymorphism
having many forms or faces
"""

# from abc import ABC, abstractmethod
#
# class Shape:
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return self.base * self.height * .5
#
# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping
#
#
# shapes = [Circle(4), Square(2), Triangle(3,4), Pizza('olive', 124)]
#
# for shape in shapes:
#     print(f'Shape: {shape.area()}cm^2')

"""
Duck typing
another way of polymorphism
must have min amount of attributes/methods
"""

# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
#
# class Car:
#     alive = False
#
#     def speak(self):
#         print("Honk")
#
# animals = [Dog(), Cat(), Car()]
# for animal in animals:
#     animal.speak()
#     print(animal.alive)

"""
Static method
method belong to a class rather than any object from that class (instance)
"""

# class Employee:
#     def __init__(self, name, pos):
#         self.name = name
#         self.pos = pos
#
#     def get_info(self):
#         return f'{self.name}, {self.pos}'
#
#     # belong to the class employee no the objects of the employee
#     @staticmethod
#     def is_valid_pos(pos):
#         valid_pos = ['Manager', 'Cook', 'Cashier']
#         return pos in valid_pos
#
# e1 = Employee('James', 'Manager')
# e2 = Employee('Jas', 'Cook')
# e3 = Employee('Jill', 'Cashier')
#
# print(Employee.is_valid_pos('Manager'))
# print(e1.get_info())
# print(e2.get_info())
# print(e3.get_info())

"""
Class methods
allo ops realted to class itself
"""

# class Student:
#     count = 0
#     total_gpa = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#
#     #instance method
#     def get_info(self):
#         return f'student name: {self.name}, GPA: {self.gpa}'
#
#     @classmethod
#     def get_count(cls):
#         return f'student count: {cls.count}'
#
#     @classmethod
#     def get_avg_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f'{cls.total_gpa/cls.count:.2f}'
#
# s1 = Student('andy', 4.0)
# s1 = Student('ken', 2.0)
# s1 = Student('peter', 3.0)
# print(Student.get_avg_gpa())
#
# print(Student.get_count())

"""
Magic methods
dunder method (double underscore __) __init__, __get__, __set__, __del__
allow automatic called by many of python's built in methods
they allow dev to define to customize the behavior of objects
"""

# class Book:
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
#
#     def __str__(self):
#         return f"'{self.title}' by {self.author} {self.num_pages} pages"
#
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
#
#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
#
#     def __gt__(self, other):
#         return self.num_pages > other.num_pages
#
#     def __add__(self, other):
#         return f'{self.num_pages + other.num_pages} pages'
#
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self, key):
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f'Keyword {key} not found'
#
#
# b1 = Book("The giver", author="lois lorry", num_pages=231)
# b2 = Book("Of mice and men", author="J. Steinbeck", num_pages=300)
# b3 = Book("Born A crime", author="Trevor Noah", num_pages=423)
#
# # print('mice' in b2)
# # print(b1)
# # print(b2 == b1)
# # print(b1 < b3)
# print(b1['author'])
# print(b2['author'])
# print(b3['name'])

"""
property decorator used to define a method as property
benefit add more logic when read, write, or delete attributes
gives you getter, setter, and delete method
"""

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#
#     # getters that are protected not private
#     @property
#     def width(self):
#         return f'{self._width:.1f} px'
#
#     @property
#     def height(self):
#         return f'{self._height:.1f} px'
#
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print('Width cannot be less than 0')
#
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print('Height cannot be less than 0')
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print('Width has been deleted')
#
#     @height.deleter
#     def height(self):
#         del self._height
#         print('Height has been deleted')
#
# rectangle = Rectangle(53, 100)
#
# rectangle.width = 23
# rectangle.height = 10
#
# del rectangle.width
# del rectangle.height


# print(rectangle.width)
# print(rectangle.height)

"""
Decorator
a function that extends the behavior of another function 
w/o modifying the base function
pass the base function as an argument to the decorator 

@add_sprinkle
get_ice_cream('vanilla')
"""

# # this is the decorator
# def add_sprinkle(func):
#     def wrapper(*args, **kwargs):
#         print('You added sprinkles')
#         func(*args, **kwargs)
#     return wrapper
#
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("You added fudge")
#         func(*args, **kwargs)
#     return wrapper
#
# @add_sprinkle
# @add_fudge
# def get_ice_cream(flavor):
#     print(f'Here is your flavor {flavor} of ice cream 🍦')
#
# get_ice_cream('chocolate')

"""
exception
an event that interrupts the flow of a program
(zerodvisionerror, typeerror, valueerror)
1.try 2.except 3. finally
"""

# try:
#     num = int(input("Enter a number: "))
#     print(1 / num)
# # except ZeroDivisionError:
# #     print("You can't divide by zero")
# # except ValueError:
# #     print("Enter only numbers")
# except Exception as e: # this tell your the kind of error
#     print(e)
# finally:
#     print("Do some clean up")

"""
Python file detection
"""

# import os # used for files
#
# # file_path = 'test.txt'
# file_path = 'text_files/new_test.txt' # relative files
# # file_path = 'C:/Desktop/test.txt' # absolute file path
#
# if os.path.exists(file_path):
#     print(f'The location "{file_path}" exists')
#     if os.path.isfile(file_path):
#         print(f'The file is a file')
# else:
#     print(f'The location "{file_path}" does not exist')

"""
python writing files (.txt, .json, .csv)
"""

txt_data = 'Mr milkyway'
import json
import csv

# employees = ['noah', 'ken', 'peter', 'andrew', 'jack']

# employees = {
#     "name": 'Andy',
#     "age": 23,
#     "Job": 'SWE'
# }

# employees = [['Name', 'Age', 'Job'],
#             ['John', '25', 'teacher'],
#             ['Mike', '32', 'mechanic'],
#             ['Amy', '18', 'nurse']]
#
# file_path = 'output.csv'
# try:
#     with open(file= file_path, mode= 'w', newline = '') as file: #with will close the file
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#
#         # json.dump(employees, file, indent=4)
#         # for employee in employees:
#         #     file.write(employee + '\n')
#         print(f'txt file written: {file_path}')
# except FileNotFoundError:
#     print('That file already exist')

"""
Python reading files (.txt, .json, .csv)
"""
#
# import json
#
# file_path = 'F:/University/My Personal Programs/Tutorial/python/output.csv'
#
# try:
#     with open(file_path, 'r') as file:
#         contents = csv.reader(file) # csv
#         for line in contents:
#             print(line)
#         # contents = json.load(file) # json
#         # contents = file.read() # normal file
#         # print(contents)
# except FileNotFoundError:
#     print('File not found')
# except PermissionError:
#     print('Permission error')

"""
Dates and Time
"""

# import datetime
#
# date = datetime.date(2025, 1,5)
# today = datetime.date.today()
# time = datetime.time(12,30,0)
# now = datetime.datetime.now()
#
# now = now.strftime('%H:%M:%S %m/%d/%Y')
#
# target_datetime = datetime.datetime(2017, 9,11)
# current_datetime = datetime.datetime.now()
#
# if target_datetime < current_datetime:
#     print('Target date has passed')
# else:
#     print('Target date has not passed')
#
# print(date)
# print(today)
# print(time)
# print(now)