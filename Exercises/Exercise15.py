# File: Exercise15.py
# Author: Kate Archer
# Insructor: Dr. Yoo
# Course: CSCI 1170-008
# Date Due: November 3, 2015
# Description:


def main():

    # Read the File Name from the user and validate with the
    # get_File_Name() function.
    fileName = get_File_Name()

    # Open the file for processing and assign to file object
    # inFile.
    inFile = open(fileName, 'r')


    # Assign the name and score by calling the
    # process_File(inFile, fileName) function.
    name, score = process_File(inFile, fileName)

    # Initialize counting variables for the loop.
    playerCount = 0
    lowScore = 100
    print()

    # Set up a while loop to read the file, ending when name
    # is read as an empty string.
    while name != '':
        playerCount +=1

        # Convert the score to a float number.
        score = int(score)

        # Assign the highScore and highScoreID.
        if score <= lowScore:
            lowScore = score
            lowScoreName = name

        # Print the data.
        print(format(name, '22s'), score)

        # Update the name and score by calling the
        # process_File(inFile, fileName) functon.
        name, score = process_File(inFile, fileName)

    # Close the file.
    inFile.close()

    # Print the analysis of the data.
    print()
    print('There are', playerCount, 'players in', fileName)
    print('The winner of this tournament is', lowScoreName, 'with a score of', lowScore)


def get_File_Name():
    fileName = input('Enter the name of the file to open for read: ')
    try:
        open(fileName, 'r')
    except:
        print(fileName, 'does not exist.')
    return fileName

def process_File(inFile, fileName):
    name = inFile.readline()
    score = inFile.readline()

    name = name.rstrip('\n')
    score = score.rstrip('\n')

    return name, score



main()
