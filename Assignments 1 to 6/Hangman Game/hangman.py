# Task 5
# Hangman Python Project

import random

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()

def main():
    print("🎮 Welcome to Hangman Game!")
    print("Hint: The word is a fruit 🍎")
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
    word = get_valid_word(words)
    guess_word = ["_"] * len(word)
    lives = 6
    guessed_letters = []

    while lives > 0 and "_" in guess_word:
        print("\nWord: " + " ".join(guess_word))
        print(f"Lives left: {lives}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        user_guess = input("Guess a letter: ").lower().strip()
        if not user_guess.isalpha() or len(user_guess) != 1:
            print("Please enter a single letter.")
            continue
        if user_guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(user_guess)

        if user_guess in word:
            print(f"Good job! '{user_guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == user_guess:
                    guess_word[i] = user_guess
        else:
            print(f"Oops! '{user_guess}' is not in the word.")
            lives -= 1

    if "_" not in guess_word:
        print("\nCongratulations! You guessed the word: " + word)
    else:
        print("\nGame over! The word was: " + word)

if __name__ == "__main__":
    main()
