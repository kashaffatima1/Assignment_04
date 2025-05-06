# Task 1
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    curr_value = int(input("Enter the number: "))
    curr_value *= 2
    
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value *= 2
        
    print(curr_value)
    
    
if __name__ == '__main__':
    main()