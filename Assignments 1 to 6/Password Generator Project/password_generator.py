# Task : 7
# Password Generator 

import random
import string

def main():
    print("🔐 Welcome to the Password Generator!")
    num_password = (input("How many passwords do you want to generate? "))
    while not num_password.isdigit() or int(num_password) <= 0:
        print("Invalid input. Please enter a positive integer.")
        num_password = (input("How many passwords do you want to generate? "))
    num_password = int(num_password)
        
    length = (input("Enter the length of the password: "))
    while not length.isdigit() or int(length) <= 0:
        print("Enter a valid length!")
        length = (input("Enter the length of the password: "))
    length = int(length)
    
    print("Generated Passwords:")
    for i in range(num_password):
       password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for
                       _ in range(length))
       print(f"Password {i+1}: {password}")
    
       


if __name__ == "__main__":
    main()
