def temperature_converter():
    print("Temperature Converter")
    print("--------------------")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    print("4. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15
                print(f"{celsius}°C = {fahrenheit}°F")
                print(f"{celsius}°C = {kelvin}K")
            elif choice == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5/9
                kelvin = celsius + 273.15
                print(f"{fahrenheit}°F = {celsius}°C")
                print(f"{fahrenheit}°F = {kelvin}K")
            elif choice == 3:
                kelvin = float(input("Enter temperature in Kelvin: "))
                celsius = kelvin - 273.15
                fahrenheit = (celsius * 9/5) + 32
                print(f"{kelvin}K = {celsius}°C")
                print(f"{kelvin}K = {fahrenheit}°F")
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    temperature_converter()