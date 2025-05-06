# Task 6
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

NUM_slides = 6
def main():
    dice1 = random.randint(1, NUM_slides)
    dice2 = random.randint(1, NUM_slides)

    total = dice1 + dice2
    
    print(f"Rolling the dice...")
    print(f"First die: {dice1} ")
    print(f"Second die: {dice2} ")
    print(f"Total is {total}")
if __name__ == '__main__':
    main()