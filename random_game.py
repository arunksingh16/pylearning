# Program for generating random number

from random import randint
import sys

# generate a random number between 1 to 10
# answer = randint(1, 10)

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# check that input

while True:
    try:
        guess = int(input('Guess a number: '))
        if 0 < guess < 11:
            if guess == answer:
                print('Good Guess !')
                break

    except ValueError:
        print('Please enter a number !')
        continue
