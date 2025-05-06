# Task 0
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

prompt = "What do you want?"
joke = "A software engineer goes to a job interview. The interviewer says, We're looking for someone who can do everything!. The programmer replies: Then I think you're looking for a recursive function."
sorry = "Sorry, I only tell jokes."
def main():
      user_input = input(prompt).strip().lower()
      if user_input == "joke":
          print(joke)
      else:
        print(sorry)
if __name__ == '__main__':
    main()