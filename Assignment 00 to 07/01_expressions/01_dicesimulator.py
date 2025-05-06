# Task 1
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random
NUM_SIDES = 6
def roll_dice():
    dice1 =  random.randint(1, NUM_SIDES)
    dice2 =  random.randint(1, NUM_SIDES)
    total: int = dice1 + dice2
    print(f"Die 1: {dice1}, Die 2: {dice2}, Total: {total}")     

def main():
     dice1 : int = 10
     print(f"Die1 in main() start as {dice1}")
     for i in range(3):
      roll_dice()
     print(f"Die1 in main() is still {dice1}")


if __name__ == '__main__':
 main()