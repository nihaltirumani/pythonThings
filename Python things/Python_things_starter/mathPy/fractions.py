numerator = int(input("Numerator : "))
denominator = int(input("Denominator : "))
mixed = int

fraction = f"{str(numerator)}/{str(denominator)}"
print(fraction)

if numerator > denominator:
    print("This is a improper fraction.")
    mixed = round((numerator - (numerator % denominator)) / denominator)
    numerator %= denominator
    fraction = f"{str(numerator)}/{str(denominator)}"
    print("Converted into mixed fraction.")
    print(f"{str(mixed)} {str(fraction)}")
    
else:
    print("This is a proper fraction.")