#!/usr/bin/env python3
# Created By: Shem Irekpita
# Date: 21/9/2025
# This program displays the area and perimeter of a rectangle.

length = int(input("Enter length of the rectangle (cm): "))
width = int(input("Enter width of the rectangle (cm): "))


def main():
    print("The Perimeter and Area of a Rectangle is:")
    print()
    print("The area is: {}cm^2".format(length * width))
    print("The perimeter is: {}cm".format(2 * (length + width)))


if __name__ == "__main__":
    main()
