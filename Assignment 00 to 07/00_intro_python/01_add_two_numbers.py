#Task 01
# Write a Python program that takes two integer inputs from the user and calculates their sum.

def main():
  try:
    first_number = input("Enter the first number: ")
    first_number = int(first_number)
    second_number = input("Enter your second_number: ")
    second_number = int(second_number)
  except ValueError:
        print("Invalid input. Please enter a valid integer.")

  #Add two numbers
  total_sum = first_number + second_number
  print(f"The sum of {first_number} and {second_number} is: {total_sum}")

#call the main function
if __name__ == "__main__":
  main()