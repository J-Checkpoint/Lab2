# Josh Thiessen
import math


def calculate_circle_area(circle_radius):
    """Returns the calculated area of a circle"""
    circle_area = math.pi * circle_radius ** 2
    return float(circle_area)


def calculate_sphere_volume(sphere_radius):
    """Returns the calculated area of the sphere"""
    sphere_volume = (4 / 3) * math.pi * sphere_radius ** 3
    return float(sphere_volume)


def calculate_bmi():
    """Returns the body mass index of the user"""
    weight = float(input("enter the weight in kilograms:"))
    height = float(input("enter the height in meters:"))
    bmi = weight / (height * height)
    return bmi


def calculate_hypotenuse():
    """Returns the hypotenuse of the right triangle"""
    side_a = int(input("enter the length of side A in cm:"))
    side_b = int(input("enter the length of side B in cm:"))
    hypotenuse = math.hypot(side_a, side_b)
    return hypotenuse
