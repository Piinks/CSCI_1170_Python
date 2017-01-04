# Kate Archer
# CSCI 1170-008
# September 17, 2015
# Programming Exercise 4

# This program calculates the average of men and women in a given class.

# Get the number if males and females from the user.
males = int(input('Enter number of males:'))
females = int(input('Enter number of females:'))

# Determine the percentage of males and females in class.
perMales = format(males/(males + females), '.0%')
perFemales = format(females/(males + females), '.0%')

# Print result.
print('Percent males:', perMales)
print('Percent females:', perFemales)
