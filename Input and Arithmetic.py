# fuction to calculate area and perimeter of a rectangle
def calculate_rectangle_properties(lenght, width):    
    area = lenght * width
    perimeter = 2 * (lenght + width)
    return area, perimeter
def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area, perimeter = calculate_rectangle_properties(length, width)
    print(f"area: {area}")
    print(f"perimeter: {perimeter}")
# run function
if __name__ == "__main__":
    main()
