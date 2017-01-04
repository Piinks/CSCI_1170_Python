############################################################################
# File: ola5_Archerb.py
# Author: Kate Archer
# Insructor: Dr. Yoo
# Course: CSCI 1170-008
# Date Due: November 9, 2015
# Description:
# Input:
# Output:
############################################################################

def main():
    # Print the purpose of the function by calling the
    # print_Purpose() function.
    print_Purpose()

    # Read the File Name from the user and validate with the
    # get_File_Name() function.
    fileName = get_File_Name()

    # Open the file for processing and assign to file object
    # inFile.
    inFile = open(fileName, 'r')

    # Print the heading for the table.
    print()
    print('User ID\t\tScore\tGrade')

    # Assign the userID and score by calling the
    # process_File(inFile, fileName) function.
    userID, score = process_File(inFile, fileName)

    # Initialize counting variables for the loop.
    recordCount = 0
    sumForAverage = 0
    highScore = 0

    # Set up a while loop to read the file, ending when userID
    # is read as an empty string.
    while userID != '':
        recordCount +=1

        # Convert the score to a float number.
        score = float(score)

        sumForAverage += score

        # Assign the highScore and highScoreID.
        if score >= highScore:
            highScore = score
            highScoreID = userID

        # Convert the score to a letter grade by calling
        # the find_Letter_Grade(score) function.
        letterGrade = find_Letter_Grade(score)

        # Print the data.
        print(userID, '\t', score, '\t', letterGrade)

        # Update the userID and score by calling the
        # process_File(inFile, fileName) functon.
        userID, score = process_File(inFile, fileName)

    # Close the file.
    inFile.close()

    # Print the analysis of the data.
    print()
    print('There are', recordCount, 'student records.')
    averageScore = sumForAverage/recordCount
    print('The average score is ', format(averageScore, '.1f'), '.', sep='')
    print(highScoreID, 'has the highest score of ', highScore, '.', sep = '')




#******************************************************
# Function Purpose: Print the purpose of the program.
# Parameters: None
# Pre-condition: None
# Post-condition: Printed purpose of the program.
#******************************************************
def print_Purpose():
    print('v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v')
    print('                WELCOME!')
    print('  The purpose of this program is to read')
    print('    the name of a data file containing')
    print(' student IDs and their scores. The program')
    print('will find and display the average score, the')
    print(' number of students processed, the student')
    print('ID with the highest score, and the processed')
    print('       output from the data file.')
    print('v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v')
    print()


#******************************************************
# Function Purpose: Read the file name, validate the
#                   file name, and return name to the
#                   main function.
# Parameters: None
# Pre-condition: None
# Post-condition: Returned valid file name.
#******************************************************
def get_File_Name():
    fileName = input('Enter the file name: ')
    try:
        open(fileName, 'r')
    except:
        print(fileName, 'does not exist.')
        fileName = get_File_Name()
    return fileName

#******************************************************
# Function Purpose: Process the file to get the user ID
#                   and score.
# Parameters: File object and file name.
# Pre-condition: File has data to be read.
# Post-condition: Returned userID and score.
#******************************************************
def process_File(inFile, fileName):
    userID = inFile.readline()
    score = inFile.readline()

    userID = userID.rstrip('\n')
    score = score.rstrip('\n')

    return userID, score

#***************************************************************
# Function Purpose: Return the letter grade for the score.
# Parameters: Student score.
# Pre-condition: Score has an appropriate value > 0 and <= 100.
# Post-condition: Returned corresponding letter grade.
#***************************************************************
def find_Letter_Grade(score):
    if score >= 90:
        letterGrade = 'A'
    elif score >= 80:
        letterGrade = 'B'
    elif score >= 70:
        letterGrade = 'C'
    elif score >= 60:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
    return letterGrade



main()
