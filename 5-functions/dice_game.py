import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def get_player_name(player_number):
    return input(f"Enter player {player_number} name: ")
def get_player_roll(player_name):
    roll = roll_dice()
    print(f"{player_name} rolled {roll}")
    return roll

def main():
    player1 = get_player_name(1)
    player2 = get_player_name(2)
    roll1 = get_player_roll(player1)
    roll2 = get_player_roll(player2)
    if roll1 > roll2:
        print(f"{player1} wins!")
    elif roll2 > roll1:
        print(f"{player2} wins!")
    else:
        print("It's a tie!")


# player1 = input("Enter player 1 name: ")
# player2 = input("Enter player 2 name: ")
#
# roll1 = roll_dice()
# roll2 = roll_dice()

# print(f"{player1} rolled {roll1}")
# print(f"{player2} rolled {roll2}")

main()
