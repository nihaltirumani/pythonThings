# formulas!

def square_area(side: int) -> int:
    return side ** 2

def square_perimeter(side: int) -> int:
    return side * 4

def rectangle_area(length: int, width: int) -> int:
    return length * width

def rectangle_perimeter(length: int, width: int) -> int:
    return 2 * (length + width)

if __name__ == "__main__":
    sqArea = square_area(int(input("Enter input for area of square : ")))
    print(f"The area of square is {sqArea}")

    sqPerimeter = square_perimeter(int(input("Enter input for perimeter of square : ")))
    print(f"The perimeter of square is {sqPerimeter}")

    print("Enter input for area of perimeter :")
    rectArea = rectangle_area(int(input("Length : ")), int(input("Width : ")))
    print(f"The area of rectangle is {rectArea}")

    print("Enter input for perimeter of rectangle :")
    rectPerimeter = rectangle_perimeter(int(input("Length : ")), int(input("Width : ")))
    print(f"The perimeter of rectangle is {rectPerimeter}")