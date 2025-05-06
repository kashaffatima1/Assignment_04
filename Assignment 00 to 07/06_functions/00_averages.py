# Task 0
# Write a function that takes two numbers and finds the average between the two.


def average(num_1, num_2):
     return  num_1 + num_2 / 2
def main():
    try:
       first_number = float(input("Enter first number: "))
       second_number = float(input("Enter second number:"))

       result = average(first_number,second_number)
       print(f"{first_number} and {second_number} average is {result}")
    except ValueError:
       print("Please enter a valid number!")
    
if __name__ == '__main__':
    main()