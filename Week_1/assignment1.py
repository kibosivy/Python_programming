import random

# Define the choices
choices = ["rock", "paper", "scissors"]

# computer's choice
computer_choice = random.choice(choices)

# user's choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer_choice}")
print(f"You chose: {user_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win")
else:
    print("Computer wins")