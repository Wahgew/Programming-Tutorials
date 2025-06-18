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