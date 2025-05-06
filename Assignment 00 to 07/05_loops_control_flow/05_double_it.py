# Task 5
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    number = int(input("Enter the number:"))
    curr_value = number * 2
    
    while number < 100:
        print(f"{number} doubled is {curr_value}")
        number = curr_value
        curr_value = number * 2
        
    print(f"{number} doubled is {curr_value}")
    
    
if __name__ == '__main__':
    main()