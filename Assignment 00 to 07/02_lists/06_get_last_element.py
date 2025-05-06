# Task 6
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    print("The last element in the list is:",lst[-1]) 
def main():
    list = []
    ques = input("How many elements do you want to add to the list?")
    for i in range(int(ques)):
       element = input("Please enter an element of the list: ")
       list.append(element)

    get_last_element(list)
    

    
if __name__ == '__main__':
    main()