# File: Exercise16.py
# Author: Kate Archer
# Insructor: Dr. Yoo
# Course: CSCI 1170-008
# Date Due: November 5, 2015
# This program has the same purpose as exercise 15, with 2 changes.
# A WHILE LOOP will be used when reading the file name to handle any exceptions.
# A FOR LOOP will be used to read all the values for this problem.


def main():

    # Read the File Name from the user and validate with the
    # get_File_Name() function.
    fileName = get_File_Name()

    # Open the file for processing and assign to file object
    # inFile.
    inFile = open(fileName, 'r')

    # Initialize counting variables for the loop.
    playerCount = 0
    lowScore = 100
    print()

    # Set up a FOR loop to read the file, assigning the input to appropriate
    # variables.
    for line in inFile:
        playerCount += 1
        name = line.rstrip()
        score = inFile.readline()

        # Convert the score to an integer.
        score = int(score)

        # Assign the lowScore and lowScoreID.
        if score <= lowScore:
            lowScore = score
            lowScoreName = name

        # Print the data.
        print(format(name, '22s'), score)

    # Close the file.
    inFile.close()

    # Print the analysis of the data.
    print()
    print('There are', playerCount, 'players in', fileName)
    print('The winner of this tournament is', lowScoreName, 'with a score of', lowScore)


def get_File_Name():
    # This function uses a WHILE loop to continue prompting the user for
    # a file name until it successfully opens.
    fail = True
    while fail:
        try:
            fileName = input('Enter the name of the file to open for read: ')
            open(fileName, 'r')
            fail = False
        except:
            print(fileName, 'does not exist.')
    return fileName


main()
