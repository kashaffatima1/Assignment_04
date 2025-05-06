# Task 0
# his program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def user_number():
    number = []
    while True:
       user_input = input("Enter a number: ")
       if user_input == "":
         break
       num = int(user_input)
       number.append(num)
    return number

def count_numbers(num_list):
    num_dic = {}
    for num in num_list:
     if num not in num_dic:
          num_dic[num] = 1
    else:
          num_dic[num] += 1
    return num_dic


def main():
    numbers = user_number()
    counted = count_numbers(numbers)
    for num, freq in counted.items():
       print(f"{num} appears {freq} times.")

if __name__ == '__main__':
    main()