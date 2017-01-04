# Program Exercise 13
# Kate Archer
# October 29, 2015
# CSCI 1170-008
# The purpose of this program is to open, read, and print the contents of a file.

def main():
    # Read the desired file from the user.
    getFile = input("Enter the name of the file to open for read: ")
    # Open the File.
    inFile = open(getFile)

    content = inFile.read()
    # Display the contents of the file.
    print()
    print('The following is the contents of the data file:', getFile)
    print()
    print(content)

    # Close the file.
    print('closing', getFile)
    inFile.close()
    print()



main()
