print("Temperature Converter")
print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")
choice = input("Choose: ")
if choice == "1":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit:", fahrenheit)
elif choice == "2":
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius:", celsius)
else:
    print("Invalid choice")