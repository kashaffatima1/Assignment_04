# Task 8
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long.

max_leng = 3
def shorten(lst):
    while len(lst) > max_leng:
        removed_item = (lst.pop())
        print(f"Removed: {removed_item}")

def main():
    items = []
    ques = input("How many elements in your list?")
    for i in range(int(ques)):
       item = input("Please enter an element of the list: ")
       items.append(item)

    shorten(items)
    print(f"Final list: {items}")

if __name__ == '__main__':
    main()