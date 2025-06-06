import random

# Scoreboard
user_score = 0
computer_score = 0
round_number = 1

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

print("Welcome to Rock, Paper, Scissors Showdown!")
print("Type rock, paper, or scissors to play.")
print("Type 'exit' to quit anytime.\n")

while True:
    print(f"--- Round {round_number} ---")
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice == 'exit':
        print("Game over. Thanks for playing!")
        break

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose rock, paper, or scissors.\n")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

    play_again = input("Play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! Stay sharp, champ!")
        break

    round_number += 1
    print()
