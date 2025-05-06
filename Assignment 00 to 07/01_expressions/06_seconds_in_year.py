# Task 
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):


days = 365
hours = 24
minutes = 60
seconds = 60

def main():
    seconds_in_year = days * hours * minutes * seconds
    print(f"There are {seconds_in_year} seconds in a year.")
    
if __name__ == '__main__':
    main()