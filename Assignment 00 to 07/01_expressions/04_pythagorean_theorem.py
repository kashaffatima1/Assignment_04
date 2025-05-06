# Task 4
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math

def main():
    ab = float(input("Enter the length of the side AB: "))
    ac = float(input("Enter the length of the side AC: "))
    bc = math.sqrt(ab ** 2 + ac ** 2)
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()