
# File: ola3_Archer.py
# Author: Kate Archer
# Instructor: Dr. Yoo
# Course: 1170-008
# Date Due: October 7, 2015
# Description: This program will tell the user what coins to use when making
#           change between 1 and 99 cents. Half-dollars are not included.
# Input: Number of cents -- change
# Output: 1. The purpose of the program.
#         2. The change in quarters, dimes, nickels and/or pennies.
# Formulas: Integer and remainder division.

def main ():
    more = 'y'
    # Display the purpose of the program.
    print('')
    for x in range (1):
        for y in range (35):
            print('*', end='')
    print('\\nWelcome to the Coin Change Machine!')
    for x in range (1):
        for y in range (35):
            print('*', end='')
    print('\\n')
    print('This program will count out the quarters,\\ndimes,' +
          ' nickels and pennies you will need for\\nthe amount' +
          ' of cents you enter.')

    while (more == 'y'):\

        # Get input from the user.
        change = int(input('Please enter an amount of cents between 1 and 99: '))

        # Check with input validation loop.
        while (change < 0) or (change >99):
            print('Error: You have not entered a correct amount of change.')
            change = int(input('Please enter an amount of cents between 1 and 99: '))

        # Calculate the amount of coins.
        quarters = int(change // 25)

        dimes = int(change % 25 // 10)

        nickels = int(change % 25 % 10 // 5)

        pennies = int(change % 25 % 10 % 5)

        # Output display.
        print('')
        print(change, 'cents can be given as:')

        # Tab display of results.
        print('\\t', end='')

        # Display relevant results based on calculations.
        if (quarters >= 2):
            print( quarters, 'quarters', end=' ')
        elif (quarters == 1):
            print(quarters, 'quarter', end=' ')

        if (dimes >= 2):
            print(dimes, 'dimes', end=' ')
        elif (dimes == 1):
            print(dimes, 'dime', end=' ')

        if (nickels == 1):
            print( nickels, 'nickel', end=' ')

        if (pennies >= 2):
            print( pennies, 'pennies', end=' ')
        elif (pennies == 1):
            print(pennies, 'penny', end=' ')

        # Ask the user if they would like to enter another amount.
        more = input('\\nWould you like to enter another amount? Type y or n: ')

    print('Thanks for playing!')



# Call the main function.
main ()
