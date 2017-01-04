# Program Exercise 7
# Kate Archer
# CSCI 1170-008
# September 24, 2015
# The purpse of this program is to take two string inputs from the user of
# two different primary colors. The program returns the color that the two
# combined would create.

# Have the user input two different primary colors.
color1 = input('Enter a primary color:')
color2 = input('Enter a different primary color:')

# .lower() is used to account for user case input for comparing the strings.
color1 = color1.lower()
color2 = color2.lower()

# Determine what color is created when the two are combined.

# If the first color is blue.
if color1 =='blue':
    if color2 == 'yellow':
        print('Blue and yellow together make green.')
    elif color2 == 'red':
        print('Blue and red together make purple.')
    else:
        print('You did not enter two different primary colors.')

# If the first color is yellow.
elif color1 == 'yellow':
    if color2 == 'red':
        print('Yellow and red together make orange.')
    elif color2 == 'blue':
        print('Yellow and blue together make green.')
    else:
        print('You did not enter two different primary colors.')

# If the first color is red.
elif color1 == 'red':
    if color2 == 'yellow':
        print('Red and yellow together make orange.')
    elif color2 == 'blue':
        print('Red and blue together make purple.')
    else:
        print('You did not enter two different primary colors.')

# If the user does not enter a primary color, or enters the same color twice,
# the program will tell them so:
else:
    print('You did not enter two different primary colors.')
