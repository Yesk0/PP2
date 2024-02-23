import math


# 1
def convert():
    degrees = int(input("Input degree: "))
    print("Output radians: ", round(math.sin(math.radians(degrees)), 6))


# 2
def trapezoid_area():
    height = int(input("Height: "))
    first_value = int(input("Base, first value: "))
    second_value = int(input("Base, second value: "))
    print("Area:", (first_value + second_value) * height / 2)


# 3
def regular_polygon_area():
    sides = int(input("Sides: "))
    length_of_side = int(input("Length of side: "))
    p_area = sides * (length_of_side ** 2) / (4 * math.tan(math.pi / sides))
    print("Area of regular polygon is: ", p_area)


# 4
def parallelogram_area():
    length = int(input("Length of parallelogram: "))
    height = int(input("Height: "))
    area = length * height
    print("Area: ", area)