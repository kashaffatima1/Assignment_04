# Task: Index Game

def main():
    my_list = [10, 20, 30, 40, 50]
    print("Current List: ", my_list)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter your choice: ")

    if operation == "access":
        index = int(input("Enter the index: "))
        if 0 <= index < len(my_list):
            print("Value at index", index, "is", my_list[index])
        else:
            print("Index out of range.")
    elif operation == "modify":
        index = int(input("Enter the index: "))
        if 0 <= index < len(my_list):
            value = int(input("Enter the new value: "))
            my_list[index] = value
            print("List after modification: ", my_list)
        else:
            print("Index out of range.")
    elif operation == "slice":
        start = int(input("Enter the start index: "))
        end = int(input("Enter the end index: "))
        print("Slice of list from index", start, "to", end, "is", my_list[start:end])
    else:
        print("Invalid operation.")

if __name__ == '__main__':
    main()