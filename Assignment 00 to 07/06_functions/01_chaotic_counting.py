# Task 1
# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch.

import random
DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD

def counting():
    for i in range(10):
        result = i + 1
        if done():
            return
        print(result)
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    counting()
    print("I'm done")
if __name__ == '__main__':
    main()