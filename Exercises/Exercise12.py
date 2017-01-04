# Program 12
# Kate Archer
# CSCI 1170-008
# October 22, 2015
# Exercise 12
# This program reads input from the user for the
# the symbol, height and width of a triangle and a
# rectangle. The program then prints these shapes.

# Read input from the user.
def main():
    symbol = input("Enter the symbol for the shapes: ")
    width = int(input("Enter the width of the shapes: "))
    height = int(input("Enter the height of the shapes: "))
    print()

    # Call the DrawRectanlge function.
    DrawRectangle(symbol, width, height)

    # Call the DrawTriangle function.
    DrawTriangle(symbol, height)


def DrawRectangle(symbol, width, height):
    for y in range (height):
        for x in range (width):
            print(symbol, end='')
        print()
    print ()

def DrawTriangle (symbol, height):
    for i in range (height):
        for j in range (i+1):
            print(symbol, end='')
        print()
    for a in range(height-1, 0, -1):
        for b in range (a):
            print(symbol, end='')
        print()

main()
