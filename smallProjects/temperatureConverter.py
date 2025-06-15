# creates func that converts celsius to fahrenheit.
def celsius_to_fahrenheit(temp): return (temp * 9/5) + 32

# creates func that converts fahrenheit to celsius.
def fahrenheit_to_celsius(temp): return (temp - 32) / (9/5)

# asking the choice.
choice = int(input("How do you want to convert (1 or 2): \n1. Celsius to fahrenheit \n2. Fahrenheit to celsius \n"))
temperature = float(input("temperature: "))

if choice == 1:
    print(f"temperature in fahrenheit: {celsius_to_fahrenheit(temperature)}°F")
elif choice == 2:
    print(f"temperature in celsius: {fahrenheit_to_celsius(temperature)}°C")
else:
    print("Invalid respone.")