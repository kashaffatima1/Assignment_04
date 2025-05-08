# Task 4
# Rock, paper, scissors Python Project

import random

def main():
    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    while True:
       user = input("Enter a choice (Rock, Paper, Scissors): ").lower().strip()
       while user not in ["rock", "paper", "scissors"]:
           user = input("Invalid choice. Please type Rock, Paper, or Scissors: ").lower().strip()
       computer = random.choice(['rock', 'paper', 'scissors'])

       print(f"\nYou chose: {user}")
       print(f"Computer chose: {computer}")

       if user == computer:
          print(f"It's a tie!")
       elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):   print("You win!")
       else:
          print("You lose!")

       play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
       if play_again != "yes":
         print("👋 Thanks for playing!")
         break
       
if __name__ == "__main__":
    main()



    


    
