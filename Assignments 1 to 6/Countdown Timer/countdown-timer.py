# Task : 6
# Countdown Timer Python Project

import time

def user_input():
    while True:
        try:
            user_time = int(input("Enter the countdown time in seconds: "))
            return user_time
        except ValueError:
            print("Invalid input. Please enter a number.")

def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds}")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

def main():
    print("Countdown Timer⏰")
    user_time = user_input()
    print(f"Countdown timer for {user_time} seconds started.")
    countdown(user_time)

if __name__ == "__main__":
    main()