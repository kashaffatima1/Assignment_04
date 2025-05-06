# Task 0
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    Score  = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}:")
        number = int(input("Your number is: "))
        question = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        computer_number = random.randint(1, 100)

        if question == "higher":
            if number > computer_number:
              print("You were right! The computer's number was: ", computer_number)
              Score += 1
              print("Your score is now:", Score ) 
            else:
               print("Aww, that's incorrect. The computer's number was:", computer_number)

        elif question == "lower":
            if number < computer_number:
               print("You were right! The computer's number was: ", computer_number)
               Score += 1
               print("Your score is now:", Score ) 
            else:
                print("Aww, that's incorrect. The computer's number was:", computer_number)
        else:
            print("Invalid input! Please choose btw 'higher' or 'lower'.")

    print("\nYour final score is:", Score )  
    print("\nThanks for playing!")
    if Score == NUM_ROUNDS:
        print("🎉Wow! You played perfectly!")
    elif Score >= NUM_ROUNDS // 2:
        print("👍Good job, you played really well!")
    else:
        print("👀Better luck next time!")

if __name__ == "__main__":
    main()