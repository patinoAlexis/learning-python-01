import random


# if computerChoice == userChoice:
#     print('Tie!')
# elif computerChoice == 'rock' and userChoice == 'scissors' or computerChoice == 'paper' and userChoice == 'rock' or computerChoice == 'scissors' and userChoice == 'paper':
#     print('YOU F LOSER!')
# else:
#     print('You win!')

def result(computerChoice, userChoice):
    if computerChoice == userChoice:
        return 'Tie!'
    elif computerChoice == 'rock' and userChoice == 'scissors' or computerChoice == 'paper' and userChoice == 'rock' or computerChoice == 'scissors' and userChoice == 'paper':
        return 'YOU F LOSER!'
    else:
        return 'You win!'


# We randomize the value of the computer's choice

firstChoice = random.choice(['rock', 'paper', 'scissors'])
secondChoice = input('rock, paper, or scissors? ')

print(result(firstChoice, secondChoice))
