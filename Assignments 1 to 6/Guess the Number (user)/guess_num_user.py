# Project 3
# Guess the Number Game Python Project (user)

import random

def main():
    print("Welcome to Number Guessing Game!")
    print("You think of a number between 1 and 100. I will try to guess it.")

    num_attempts = 0
    low = 1
    high = 100
    while True:
        if low > high:
            print("Oops! Seems like you gave incorrect hints. Let's restart.")
            break
        guess = random.randint(low, high)
        num_attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it 'higher', 'lower', or 'correct'? ").lower().strip()

        if feedback == "higher":
            low = guess + 1
            print("I'll guess higher next time.")
        elif feedback == "lower":
            print("I'll guess lower next time.")
            high = guess - 1
        elif feedback == "correct":
            print(f"Yay!! I guessed your number in {num_attempts} attempts.")
            break
        else:
            print("Invalid input. Please type 'higher', 'lower', or 'correct'.")

    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!👋")

if __name__ == "__main__":
    main()