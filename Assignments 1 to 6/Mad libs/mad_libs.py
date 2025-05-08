# Project 1
# Task: Mad libs

import random

def main():
    adj = input("Enter an Adjective:")
    verb1 = input("Enter a Verb:")
    verb2 = input("Enter another Verb:")
    famous_person = input("Enter a Famous Person's Name:")

    sentence = [ 
        f"Yesterday, I saw {adj} {famous_person} walking down the street.",
        f"Computer programming is so {adj}! It makes me so excited all the time because "
        f"I love to {verb1}, stay hydrated, and {verb2} like I am {famous_person}!",
        f"{famous_person} once said, 'Always stay {adj}, work hard to {verb1}, and never forget to {verb2}.'",
    ]

    madlibs = random.choice(sentence)
     
    print("\nWelcome to the Mad Libs App!")
    print("====================================")
    print(madlibs)

if __name__ == "__main__":
    main()  