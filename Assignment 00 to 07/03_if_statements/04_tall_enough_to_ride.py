# Task 4
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

minm_height = 50
def main():
    user_height = float(input("How tall are you? "))
    if user_height >= minm_height:
        print("You're tall enough to ride!")
    elif user_height < 49:
        print("You're not tall enough to ride, but maybe next year!")
    else:
        print("You're too short to ride!")

if __name__ == '__main__':
    main()