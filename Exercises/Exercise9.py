# Program Exercise 9
# Kate Archer
# CSCI 1170-008
# October 1, 2015
# The purpose of this program is to practice FOR loops and WHILE loops.

# Step 1
# Read input from user and assign to variables.
word = input('Enter a word: ')
length = int(input('Enter a number between 3 and 7 inclusive: '))

print('===============')

# Step 2
# Print word length times.
for k in range (length):
    print(word)

print('===============')

# Step 3
# Print numbers 0-length on the same line.
x = 0
while (x <= length):
    print(x, end = '')
    x += 1

print('\\n===============')

# Step 4
# Print numbers length-1 in descending order on separate lines.
y = length
while (y >= 1):
    print(y)
    y -= 1

print('===============')

# Step 5
# Print the sum of the numbers 1-length.
total = 0
j = 1
while (j <= length):
    total += j
    j += 1
print('The sum of 1 to', length, 'is', total)
