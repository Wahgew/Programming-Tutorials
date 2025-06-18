# Hangman Program

import random

words = ("apple,", 'orange', 'kiwi', 'pear', 'watermelon')


# dic of ket:()
hangman_art = {0: ("   ",
                   "   ",
                   "   ",),
               1: (" @ "
                   "   ",
                   "   ",),
               2: (" @ ",
                   " | ",
                   "   ",),
               3: (" @ ",
                   "/| ",
                   "   ",),
               4: (" @ ",
                   "/|\\",
                   "   ",),
               5: (" @ ",
                   "/|\\",
                   "/  ",),
               6: (" @ ",
                   "/|\\",
                   "/ \\",),}

def display_man(wrong_guesses):
    print(40*'+')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print(40 * '+')

def display_hint(hint):
    print(' '.join(hint))

def display_answer(ans):
    print(' '.join(ans))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Sorry, that's not a single letter.")
            continue

        if guess in guessed_letters:
            print(f"Sorry, that letter {guess} was already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if '_' not in hint:
            display_man(wrong_guesses)
            display_hint(answer)
            print('You Win!')
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print('You Lose!')
            is_running = False

if __name__ == '__main__':
    main()