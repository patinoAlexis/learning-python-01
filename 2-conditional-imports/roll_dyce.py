# Using random module

import random

roll = random.randint(1, 6)
# print(f'You rolled a {roll}')
guess = int(input('Guess the number you rolled: '))

if guess == roll:
    print('You guessed right!')
else:
    print(f'You guessed wrong! The number was {roll}')