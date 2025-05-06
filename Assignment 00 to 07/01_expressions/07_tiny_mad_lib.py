# Task 7
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Sentence_start = "During my coding journey, I built a"
def main():
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    print(f"\n {Sentence_start} {adjective} {noun} that could eat {verb} the speed of light!")

if __name__ == '__main__':
    main()