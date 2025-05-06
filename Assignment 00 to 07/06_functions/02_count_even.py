# Task 2
# Fill out the function count_even(lst):

def is_even(number):
    return number % 2 == 0

def user_num():
    numbers = []
    while True:
        user_input = (input("Enter an integer (or press Enter to finish): "))
        if user_input == "":
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return numbers

def count_even(numbers):
    return sum(1 for num in numbers if is_even(num))

def main():
    print("Welcome to the Even Number Counter!")
    user_numbers = user_num()
    even_count = count_even(user_numbers)
    print(f"\nYou entered {len(user_numbers)} numbers.")
    print(f"Count of even numbers: {even_count}")

if __name__ == "__main__":
    main()