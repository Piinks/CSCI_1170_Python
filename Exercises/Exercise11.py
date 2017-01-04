# Kate Archer
# CSCI 1170-008
# October 15, 2015

# Read input from the user.

symbol = input("Enter the symbol for the shapes: ")
width = int(input("Enter the width of the shapes: "))
height = int(input("Enter the height of the shapes: "))

# Draw the rectangular shape
for y in range (height):
    for x in range (width):
        print(symbol, end='')
    print()
print ()

# Draw the triangle shape.
for i in range (height):
    for j in range (i+1):
        print(symbol, end='')
    print()
for a in range(height-1, 0, -1):
    for b in range (a):
        print(symbol, end='')
    print()
