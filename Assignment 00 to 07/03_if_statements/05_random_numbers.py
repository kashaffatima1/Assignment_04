# Task 5
# Print 10 random numbers in the range 1 to 100.

import random
numbers_range = 10
min_value = 1
max_value = 100
def main():
    for i in range(numbers_range):
        random_number = random.randint(min_value, max_value) 
        print(random_number, end=" ")

if __name__ == '__main__':
    main()