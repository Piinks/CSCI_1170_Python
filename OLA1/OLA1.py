############################################################################
# File: ola1.py
# Author: Kate Archer
# Insructor: Dr. Yoo
# Course: CSCI 1170-008
# Date Due: September 9, 2015
# Description: This program determines the average of three test scores.
# Input: Three tests scores -- test1(float), test2(float), and test3(float)
# Output: 1. The Purpose of the program.
#         2. The average of three test scores -- average (float) with and an
#            identifying message.
# Formulas: Average= (test1 + test2 + test3) / 3
############################################################################

def main ():

    #1. Display the purpose of the program.
    print('')
    print ("This program computes the average of three scores.")

    #2. Read in the first three test scores.
    #2.1 Get the first score from the user.
    test1 = float( input("Enter the first test score: "))
    print ("You entered ", test1)

    #2.2 Get the second score from the user.
    test2 = float( input("Enter the second test score:  "))
    print ("You entered ", test2)

    #2.3 Get the third score from the user.
    test3 = float( input("Enter the third test score:  "))
    print ("You entered ", test3)

    #3. Calculate the average of the test scores.
    average = (test1 + test2 + test3)/3

    #4. Print the average with an identifying message.
    print ("The average of the three scores is: ", format(average, '.2f'),"(rounded to two decimal places)")

    if average < 90:
        print('Keep studying!')
    else:
        print ('Way to go!')

    print ("")


#Call the main function.
main ()
