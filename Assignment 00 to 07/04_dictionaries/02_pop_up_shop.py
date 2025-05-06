# Task 2
# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruit.

def main():
    fruits: dict[str, int] = {
        "apple": 5,
        "banana": 10,
        "grapes": 5,
        "strawberry": 6,
        "guava": 8,
    }

    cost = 0

    for fruit_name, price in fruits.items():
        try:
            asking_question = int(input(f"How many {fruit_name} do you want?"))
            cost += price *  asking_question
        except ValueError:
            print("Please enter a valid number!")
            continue

    print(f"\nYour total is {cost} $ ")
    print("Thank you for shopping")


if __name__ == '__main__':
    main()