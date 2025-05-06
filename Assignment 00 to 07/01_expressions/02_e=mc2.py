# Task 2
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

c = 299792458.0 # Speed of light in meters per second
def main():
    mass_in_kg = float(input("Enter kilos of mass: "))
    energy_in_joules = mass_in_kg * (c ** 2)

    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg ")
    print(f"C = {c} m/s")
    
    print(f"{energy_in_joules}  joules of energy!")
   
if __name__ == '__main__':
    main()