# Kate Archer
# CSCI 1170-008
# Program Exercise 18
# Dr. Yoo
# November 19, 2015

def main():
    # Read the file to open.
    filename = input('Enter the file name: ')

    # Open the file and assign to a file object.
    inFile = open(filename, 'r')

    # Set up an empty list for reading integers.
    integers=[]

    # Read the integers into the list.
    for line in inFile:
        number = int(line)
        integers.append(number)

    # Close the file.
    inFile.close()

    # Calculate the average.
    average = sum(integers)/len(integers)

    print()

    # Print the results with proper formatting.
    print('There are', len(integers), 'values in file', filename)
    print('The average is', average)
    print()
    for i in range(len(integers)):
        print(format(integers[i], '10d'), end='\t')
        if integers[i] > average:
            print(format('above average', '15s'))
        elif integers[i] == average:
            print(format('average', '15s'))
        else:
            print(format('below average', '15s'))

# Call the main function.
main()
