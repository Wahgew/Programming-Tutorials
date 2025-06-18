from script1 import *

def fav_drink(drink):
    print(f'your drink is {drink}')

def main():
    print("This is script 2")
    food("burger")
    fav_drink("milk")

if __name__ == '__main__':
    main()