# Kate Archer
# CSCI 1170-008
# Program Exercise 19
# Dr. Yoo
# November 24, 2015

def main():

    # Open the file and assign to a file object.
    inFile = open('data16.txt', 'r')

    # Set up an empty list for reading integers.
    integers=[]

    # Read the integers into the list.
    for line in inFile:
        number = int(line)
        integers.append(number)

    # Close the file.
    inFile.close()

    print()

    # Print the results with proper formatting.
    print('Sum Equals: ', sum(integers))
    print('There are', len(integers), 'values:')
    for i in range(len(integers)):
        print(format(integers[i], '8d'), end='     ')
        print(format((integers[i]/sum(integers)), '.1%'))

# Call the main function.
main()
