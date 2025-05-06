# Task 10
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

def print_ones_digit(num): 
    print("The ones digit is", num % 10)

def main():
    try:
      number = int(input("Enter a number: "))
      print_ones_digit(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()