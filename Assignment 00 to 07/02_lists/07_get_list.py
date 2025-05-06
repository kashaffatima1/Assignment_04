# Task 7
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.


def main():
    values = []
    while True:
      user_input = input("Enter a value: ")
      if user_input == "":
       break
      values.append(user_input)
    print(f"Here's the list: {values}")

    
if __name__ == '__main__':
    main()