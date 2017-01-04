# Kate Archer
# October 6, 2015
# CSCI 1170-008
# Exercise 10

# Read input from the user.
upper = int(input('Enter a number between 2 and 20 for the upper bound of the table: '))

# Validate input.
while (upper < 2) or (upper > 20):
    print('You have not entered a correct value.')
    upper = int(input('Please enter a number between 2 and 20: '))

print('')
print('The multiplication table for 2 to', upper)

# Format heading.
for a in range((upper*4)+2):
    print('-', end='')

print('')
print('    ', end='')

for b in range (2,upper+1):
    print(format(b, '4d'), end='')

print('')

# Calculate table values and display.
for c in range((upper*4)+2):
    print('-', end='')

print('')

for y in range(2,upper+1):
    print(format(y,'2d'), '|', end='')
    for x in range (2,upper+1):
        print(format(y*x, '4d'), end='')
    print('')
