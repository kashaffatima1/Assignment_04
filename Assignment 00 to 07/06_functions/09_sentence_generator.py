# Task 9
# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

def  make_sentence(word, part_of_speech):
    if part_of_speech == 0:  # Noun
        print(f"I saw a {word} at the museum yesterday.")
    elif part_of_speech == 1:  # Verb
        print(f"She loves to {word} every weekend.")
    elif part_of_speech == 2:  # Adjective
        print(f"That painting is incredibly {word}.")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")


def main():
    try:
     word = input("Please type a noun, verb, or adjective: ").strip()
     print("Is this a noun, verb, or adjective?")
     part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
     make_sentence(word, part_of_speech)
    except ValueError:
        print("Invalid input! Please enter 0, 1, or 2.")

        

if __name__ == '__main__':
    main()