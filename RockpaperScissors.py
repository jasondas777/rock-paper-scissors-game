import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    while True:
        choice = input("Enter Rock, Paper, or Scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid input! Please enter Rock, Paper, or Scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins!"

def play():
    wins, losses, draws = 0, 0, 0

    while True:
        print("\n--- Rock Paper Scissors ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            wins += 1
        elif "draw" in result:
            draws += 1
        else:
            losses += 1

        print(f"\nScore: Wins: {wins}, Losses: {losses}, Draws: {draws}")
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! 🎮")
            break

if __name__ == "__main__":
    play()
