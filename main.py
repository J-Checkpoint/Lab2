# Josh Thiessen
import utilities


def main():
    circle_area = utilities.calculate_circle_area()
    print("the area of circle is:", circle_area)

    sphere_volume = utilities.calculate_sphere_volume()
    print("enter the radius of a sphere in cm:", sphere_volume)

    bmi = utilities.calculate_bmi()
    print("the Body Mass Index is:", bmi)

    hypotenuse = utilities.calculate_hypotenuse()
    print("the hypotenuse length of the right triangle is:", hypotenuse)


if __name__ == "__main__":
    main()


# Here is the expected output of main.py

# enter the radius of a circle in cm: 5
# the area of circle is 78.53981633974483
# enter the radius of a sphere in cm: 5
# the volume of the sphere is: 523.5987755982989
# enter the weight in kilograms: 63.5
# enter the height in meters: 1.73
# the Body Mass Index is: 21.216879949213137
# enter the length of side A in cm: 3
# enter the length of side B in cm: 4
# the hypotenuse length of the right triangle is: 5.0
# process finished with exit code 0
