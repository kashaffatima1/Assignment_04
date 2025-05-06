# Task 4
# Print 10 random numbers in the range 1 to 100.

import random

get_numbers = 10
min_num = 1
max_num = 100

def main():
    result = [random.randint(min_num, max_num)
               for _ in range(get_numbers)]
    print("Generated random numbers:")
    print(*result) # unpack the list element

if __name__ == '__main__':
    main()