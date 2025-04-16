import random

# Snakes and Ladders positions(dictionary)
snakes = {16: 6, 47: 26, 49: 11, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to check for snakes or ladders
def move_player(position):
    if position in snakes:
        print(f"Snake! Go down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Ladder! Climb up to {ladders[position]}")
        return ladders[position]
    return position

# Players
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

positions = {player1: 0, player2: 0}
winner = None

while not winner:
    for player in [player1, player2]:
        input(f"\n{player}, press Enter to roll the dice...")
        roll = roll_dice()
        print(f"{player} rolled a {roll}")

        if positions[player] + roll <= 100:
            positions[player] += roll
            print(f"{player} moves to {positions[player]}")
            positions[player] = move_player(positions[player])
        else:
            print("Need exact roll to reach 100.")

        # player just landed on square 100
        if positions[player] == 100:
            # Stores the winning player’s name
            winner = player
            # Ends the game loop because someone has won
            break

print(f"\n🏆 {winner} wins the game!")
