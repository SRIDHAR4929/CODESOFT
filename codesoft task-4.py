import random

your_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    user = input("Your choice: ")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("Computer chose:", computer)
    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        your_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score")
    print("You:", your_score)
    print("Computer:", computer_score)

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("Your score:", your_score)
        print("Computer score:", computer_score)
        print("Thanks for playing!")
        break
