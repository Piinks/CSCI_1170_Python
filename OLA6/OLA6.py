###############################################################################
# File: ola6_Archer.py
# Author: Kate Archer
# Insructor: Dr. Yoo
# Course: CSCI 1170-008
# Date Due: November 30, 2015
# Description: This program grades a multiple choice exam. It reads to
#               contents of a file containing the answer key, student IDs
#               and answers. It then calculates their grades and class standing.
# Input: Data file containing the answer key, student IDs and answers.
# Output: The student IDs with their answers, grades, and standings.
###############################################################################

def main():

    # Get the file name from the user and vaildate using the get_File_Name
    # function.
    fileName = get_File_Name()

    # Open the file for reading.
    inFile = open(fileName, 'r')

    # Read the first line of the file and assign to answer key.
    answerKey = inFile.readline()

    # Display the answer key.
    print('Key: ', answerKey)
    print()

    # Create empty lists to read data into.
    idList = []; answersList = []; gradeList=[]; highScore = 0

    # Read the lines of the file, appending the appropriate sections into their
    # respective lists.
    for line in inFile:

        # Split the line into a list.
        lineList = line.split()

        # Append the student ID and score to their repsective list.
        idList.append(lineList[0])
        answersList.append(lineList[1])
        answers = lineList[1]

        # Find the grade and append to gradeList using the gradeMCExam function.
        grade = gradeMCExam(answerKey.rstrip(), answers)
        gradeList.append(grade)

        # Determine the high score.
        if grade >= highScore:
            highScore = grade
            highScoreID = lineList[0]

    # Calculate the average grade.
    average = sum(gradeList)/len(gradeList)

    # Print the heading for the table.
    print('Student ID    Student Answers\t\tGrade\t Standing')

    # Print the data.
    for i in range(len(idList)):
        print(format(idList[i], '13s'), format(answersList[i], '25s'),
              format(gradeList[i], '5d'), end='')
        # Determine standing witht he function calculate_Standing.
        standing = calculate_Standing(gradeList[i], average)
        print('\t', standing)

    print()
    # Print the statistics for the data.
    print('The average score is', format(average, '.1f'))
    print('There are', len(idList), 'records in the file')
    print('The student ID', highScoreID, 'has the highest score of', highScore)




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

#***********************************************************
# Function Purpose: Calculate the students grade.
# Parameters: answerKey and and student's answers.
# Pre-condition: answerKeya and answers are the same length.
# Post-condition: Returns the correctCount, the number of
#                 correct answers and the grade for the
#                 student.
#***********************************************************
def gradeMCExam(answerKey, answers):
    correctCount = 0
    for i in range(len(answerKey)):
        if answerKey[i] == answers[i]:
            correctCount += 1
    return correctCount

#********************************************************
# Function Purpose: Calculates the student's standing
#                   based on the acheived grade.
# Parameters: The student's grade, and the average grade
#             for the class.
# Pre-condition: The grade is above, below, or equal to
#                the average.
# Post-condition: Returns the correct standing for the
#                 student
#********************************************************
def calculate_Standing(grade, average):
    if (grade > average):
        standing = 'above average'
    elif (grade == average):
        standing = 'average'
    else:
        standing = 'below average'
    return standing


# Call the main function.
main()
