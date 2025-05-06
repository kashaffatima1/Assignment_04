# Task 2
# Write a program that doubles each element in a list of numbers.


numbers = [1, 2, 3, 4, 5]

def main():
    doubled_numbers = [i * 2 for i in numbers]
    print(doubled_numbers)
if __name__ == '__main__':
    main()
