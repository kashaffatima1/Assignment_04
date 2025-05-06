# Task 6
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd.

def is_odd(num):
    return num % 2 == 1

def main():
    for i in range(10 , 30):
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")
if __name__ == '__main__':
    main()