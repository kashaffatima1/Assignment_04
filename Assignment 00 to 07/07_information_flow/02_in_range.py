# Task 2
# Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high):
    if n >= low and n <= high:
       return True

    return False

def main():
    print(in_range(7, 9, 8))   
    print(in_range(9, 5, 20))   
    print(in_range(10, 4, 5))  
    print(in_range(13, 8, 89))   


if __name__ == '__main__':
    main()