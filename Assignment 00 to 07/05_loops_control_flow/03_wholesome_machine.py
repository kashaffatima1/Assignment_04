# Task 3
# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

def main():
   Affirmation = "I am strong, confident, and capable of achieving my goals."
   print("Please type the following affirmation: ")
   print(Affirmation)

   feedback = input("Get Feedback: ")
   while feedback != Affirmation:
          print("❌That was not the affirmation. Try again!")
          print("Please type the following affirmation: ")
          print(Affirmation)
          feedback = input("Get Feedback: ")
   print("🎉 That's right! :)")


if __name__ == '__main__':
    main()