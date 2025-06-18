# Banking program

def show_balance(balance):
    print(f'Your account balance is ${balance:.2f}')

def deposit():
    amount = float(input('How much do you want to deposit: '))
    if amount < 0:
        print('Not valid')
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('How much do you want to withdraw: '))
    if amount > balance:
        print('Not valid')
        return 0
    elif amount < 0:
        print('Amount must be positive')
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('Banking program')
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank you for using Banking program")

if __name__ == '__main__':
    main()