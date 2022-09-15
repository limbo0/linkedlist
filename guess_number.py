
import random
import sys
import getpass




def guess_game(maxnum):
    target = int(getpass.getpass("What is a correct number?"))
    guess = int(input(f"Pick a number between 1 and {maxnum}\n"))
    tries = 0

    while guess != target:
        tries += 1

        if guess < target:
            guess = int(input("Higher!\n"))

        elif guess > target:
            guess = int(input("Lower!\n"))

    print(f"Correct! You took {tries} guesses.")

if len(sys.argv) > 1:
    guess_game(sys.argv[1])

else:
    guess_game("1000")

