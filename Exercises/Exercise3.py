# Program Exercise 3
# Kate Archer
# 1170-008
# 9/15/15

#This program will adjust the amount of ingredients needed to make the amount of cookies you input.

print('Welcome to the Cookie Converter!')

# This creates a midofier number for the amount of ingredients.
altNum = float(input('How many cookies would you like? '))/48

# Adjusts and assigns ingredient amounts.
altSug = format(1.5 * altNum, '.1f')
altBut = format(1 * altNum, '.1f')
altFlour = format(2.75 * altNum, '.1f')

# Prints results!
print('You will need', altSug, 'cups of sugar,', altBut, 'cups of butter, and', altFlour, 'cups of flour.')
print("Enjoy! And don't forget the milk!")
