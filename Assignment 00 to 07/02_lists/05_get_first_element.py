# Task 5
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst):
    print("The first element in the list is:",lst[0])
def main():
    list = []
    ques = input("How many elements do you want to add to the list?")
    for i in range(int(ques)):
       element = input("Please enter an element of the list: ")
       list.append(element)

    get_first_element(list)
    
if __name__ == '__main__':
    main()