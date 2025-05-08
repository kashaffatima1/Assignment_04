# Task 2
# Guess the Number Game Python Project (computer)

import random

def main():
    print("Welcome to the Guess the Number Game!")
    print("I have thought of a number between 0 and 100.")
    print("Can you guess what it is?")

    com_guess = random.randint(0, 100)
    num_attempts = 0
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            num_attempts += 1

            if user_guess > com_guess:
                print("Too high! Try again.")
                num_attempts += 1
            elif user_guess < com_guess:
                print("Too low! Try again.")
                num_attempts += 1
            else:
                print(f"Congratulations! You guessed the number in {num_attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!👋")

if __name__ == "__main__":
    main()