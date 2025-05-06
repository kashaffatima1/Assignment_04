# Task 2
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Kuwait_age = 21
China_age = 18
Bahrain_age = 20
Greece_age = 17
Brazil_age = 16

def main():
    user_age = int(input("Please enter your age: "))
    can_vote_anywhere = False

    if user_age >= Brazil_age:
        print("You can vote in Brazil")
        can_vote_anywhere = True
    if user_age >= Greece_age:
        print("You can vote in Greece")
        can_vote_anywhere = True
    if user_age >= China_age:
        print("You can vote in China")
        can_vote_anywhere = True
    if user_age >= Bahrain_age:
        print("You can vote in Bahrain")
        can_vote_anywhere = True
    if user_age >= Kuwait_age:
        print("You can vote in Kuwait")
        can_vote_anywhere = True
    if not can_vote_anywhere:
        print("You can't vote in any of these countries")


if __name__ == '__main__':
    main()