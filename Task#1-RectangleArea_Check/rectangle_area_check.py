# calculate_area.py
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

result_area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {result_area}")
