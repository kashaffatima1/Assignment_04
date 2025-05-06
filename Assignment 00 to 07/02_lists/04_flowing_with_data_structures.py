# Task 4
# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it.

def main():
    message = input("Enter a message to copy: ")
    list = []
    print(f"Before list: {list}")
    for i in range(3):
        list.append(message)
    print(f"After list: {list}")
if __name__ == '__main__':
    main()