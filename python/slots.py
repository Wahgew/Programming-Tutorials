# Python slot machine
import random

def spin_row():
    symbol = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbol) for _ in range(3)]

def print_row(row):
    print(20 * '_')
    print(" | ".join(row))
    print(20 * '_')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '⭐':
            return bet * bet
    return 0

def main():
    balance = 100

    print(50*'-')
    print("Welcome to spin row")
    print('Symbols:🍒 🍉 🍋 🔔 ⭐')
    print(50 * '-')

    while balance > 0:
        print(f'Current balance: ${balance}')

        bet = input('Enter your bet: ')

        if not bet.isdigit():
            print('Enter a valid number')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient balance')
            continue

        if bet < 0:
            print('Bet must be positive')
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won ${payout}')
        else:
            print(f'You lose this round ${-payout}')

        balance += payout

        play_again = input('Would you like to play again? (y/n): ').lower()

        if play_again != 'y':
            break

    print('*', 30*'-', '*')
    print(f'Game over! Your balance is ${balance}')
    print('*', 30 * '-', '*')

if __name__ == '__main__':
    main()