# Program Exercise 8
# Kate Archer
# CSCI 1170-008
# September 29, 2015
# The purpose of this program is to calculate the factorial
# of the inputted nonnegative integer.

# Display the purpose of the program.
print('Welcome to the Factorial Factory!')

# Get the input from the user.
n = int(input('Please enter a nonnegative integer: '))

# Set-up input validation loop in case an incorrect value is entered.
while n <= 0:
    print('You have entered an incorrect value.')
    n = int(input('Please enter a nonnegative integer: '))

# Set multiplier base.
total = 1

# Calculate Factorial.
for x in range (2, n+1):
    total *= x

# Display the result.
print('The factorial of', n, 'is', total, end=""); print('.')
