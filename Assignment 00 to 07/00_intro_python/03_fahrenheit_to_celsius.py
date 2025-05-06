# Task 03
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def main():
   fahrenheit = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m "))
   convert_celsius = (fahrenheit - 32) * 5.0/9.0
   print(f"{fahrenheit} °F is equal to {convert_celsius}°C")
   
if __name__ == '__main__':
    main()