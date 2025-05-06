# Task 3
# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

def stock_details(fruits):
    if fruits == 'apple':
        return 2
    elif fruits == 'grapes':
        return 4
    elif fruits == 'watermelon':
        return 10
    elif fruits == 'banana':
        return 8
    elif fruits == 'pear':
        return 4
    elif fruits == 'mango':
        return 9
    else:
        return 0

def main():
        fruits = input("Enter a fruit: ")
        stock = stock_details(fruits)
        if stock == 0:
                print("Sorry, we don't have this fruit in stock.")
        else:
                print(f"The number of {fruits} in stock is {stock}.")
 
if __name__ == '__main__':
    main()