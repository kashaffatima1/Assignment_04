# Task 5
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    return num - 7

def main():
    try:
      number = int(input("Which number would you like to subtract 7 from? "))
      result = subtract_seven(number)
      print(f"The result of subtracting 7 from {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()