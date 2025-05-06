# Task 1
# Write a program to print terms in the Fibonacci sequence up to a maximum value.

MAX_TERM_VALUE : int = 10000

def fibonacci_seq():
    curr_term = 0 
    next_term = 1
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")
        curr_term, next_term = next_term, curr_term + next_term

def main():
    print("Fibonacci Sequence up to", MAX_TERM_VALUE, ":")
    fibonacci_seq()

if __name__ == '__main__':
    main()