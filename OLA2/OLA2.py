# File: ola2_Archer.py
# Auhtor: Kate Archer
# Instructor: Dr. Yoo
# Course: 1170-008
# Date Due: September 23, 2015
# Description: This program converts temperature reading from Fahrenheit to Celsius.
# Input: One temperature, in Fahrenheit -- fTemp
# Output: 1. The Purpose of the program.
#         2. The temperature in Celsius -- cTemp (float) formatted to one decimal place.
# Formula: cTemp = (fTemp - 32) * (5/9)


def main ():

    # Display the purpse of the program.
    print('Welcome to the Temperature Converter!')

    # Get the temperature from the user.
    fTemp = float(input('Please entert the temperature in Fahrenheit: '))

    # Calculate cTemp.
    cTemp = format(((fTemp - 32) * (5/9)), '.1f')

    # Print the results.
    print('In Celsius, the temperature is', cTemp, 'degrees.')

# Call the main function
main ()
