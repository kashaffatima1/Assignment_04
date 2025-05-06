# Task 1
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!


def main():
    gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    user_earth_weight = float(input('Enter a weight on Earth: '))
    planet = input("Enter a planet: ")


    if planet in gravity:
      result = round(user_earth_weight * gravity[planet], 2)
      print(f"The equivalent weight on {planet} is {result}")
    else:
       print("Invalid planet. Please enter one of the following: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune")
  
if __name__ == "__main__":
    main()