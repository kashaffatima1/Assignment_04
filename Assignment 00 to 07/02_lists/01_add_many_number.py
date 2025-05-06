# Task 1
# Write a function that takes a list of numbers and returns the sum of those numbers.


def sum_of_numbers(numbers):
    return sum(numbers)

def main():
    list = [5, 10, 15, 20, 25]
    total = sum_of_numbers(list)
    print(f"The total is : {total}")
    
if __name__ == '__main__':
    main()