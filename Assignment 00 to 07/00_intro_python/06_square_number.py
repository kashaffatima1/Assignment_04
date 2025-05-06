# Task 6
# Ask the user for a number and print its square (the product of the number times itself).

def main():
    number = float(input("\033[1;3m Type a number to see its square: \033[0m "))
    convert_square = number ** 2
    print(f"The square of {number} is {convert_square}")

if __name__ == '__main__':
    main()