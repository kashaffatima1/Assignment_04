# Task 3
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

inches_in_foot = 12 # 12 inches per foot

def main():
    feet = float(input("Enter number of feet: "))
    inches = feet * inches_in_foot
    print(f"{feet} feet is equal to {inches} inches")

if __name__ == '__main__':
    main()