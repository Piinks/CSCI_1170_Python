# Program Exercise 14
# Kate Archer
# October 29, 2015
# CSCI 1170-008
# The purpose of this program is to open, read, and print the contents of a file
# with a line count along the side, and total at the end.

def main():
    try:
        # Read the desired file from the user.
        getFile = input("Enter the name of the file to open for read: ")
        # Open the File.
        inFile = open(getFile)

        lineNum = 0
        line = inFile.readline()
        print()
        while line != '':
            line = line.rstrip('\n')
            lineNum +=1
            print('line', lineNum, line)
            line = inFile.readline()
        print()
        print('There are', lineNum, 'lines in file', getFile)

    except:
        print('Data file', getFile, 'does not exist.')


main()
