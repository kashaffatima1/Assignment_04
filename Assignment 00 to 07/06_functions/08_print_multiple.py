# Task 8
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    try:
       message = input("Please type a message: ")
       repeats = int(input("Enter a number of times to repeat your message: "))
       print_multiple(message, repeats)
    except ValueError:
        print("Invalid response. Please try again!")
if __name__ == '__main__':
    main()