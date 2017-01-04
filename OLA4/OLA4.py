############################################################################
# File: ola4_Archer.py
# Author: Kate Archer
# Insructor: Dr. Yoo
# Course: CSCI 1170-008
# Date Due: October 21, 2015
# Description: This program simulates the classic game, Rock-Paper-Scissors.
#              The user is prompted to enter a shape, while the computer
#              selects one at random. When the user decides to end the game,
#              summary and user statistics are displayed.
# Input: 1. User inputs the shape r, s or p to play.
#        2. User inputs q to quit the game.
# Output: 1. Prompt for input of shape or quitting the game
#         2. Prompt for correction of user input if invalid.
#         3. Summary and User Statistics at the end of the game.
############################################################################

# Import the random module.
import random
# Call random.seed function, pass 0 as seed value.
random.seed(0)

# Define the main function.
def main():

    # Call the game_rules function to display game rules.
    game_rules()

    # Read input from the user and vaildate with the validate_input function.
    userChoice = validate_input(input('Enter a command (rpsq): '))

    # Initialize variables used for calculating statistics.
    tieCount = 0; winCount = 0; loseCount = 0
    roundCount = 0
    rockCount = 0; paperCount = 0; scissorsCount = 0

    # Use a while loop for continuous gameplay until the user enters 'q'.
    while (userChoice == 'r') or (userChoice == 'p') or (userChoice == 's'):

        # Determine the computer selection by calling the select_Random function.
        computerChoice = select_Random()

        # Add one to roundCount for each round played.
        roundCount += 1

        # Determine and display winner of each round. Update counting variables.
        if (userChoice == 'r'):
           rockCount += 1
           if (computerChoice == 1):
               print('User chose r, computer chose r.')
               print('This round is a tie.')
               tieCount += 1
           elif (computerChoice == 2):
               print('User chose r, computer chose p.')
               print('Computer wins this round.')
               loseCount += 1
           elif (computerChoice == 3):
               print('User chose r, computer chose s.')
               print('User wins this round.')
               winCount += 1

        if (userChoice == 'p'):
           paperCount += 1
           if (computerChoice == 1):
               print('User chose p, computer chose r.')
               print('User wins this round.')
               winCount += 1
           elif (computerChoice == 2):
               print('User chose p, computer chose p.')
               print('This round is a tie.')
               tieCount += 1
           elif (computerChoice == 3):
               print('User chose p, computer chose s.')
               print('Computer wins this round.')
               loseCount += 1

        if (userChoice == 's'):
           scissorsCount += 1
           if (computerChoice == 1):
               print('User chose s, computer chose r.')
               print('Computer wins this round.')
               loseCount += 1
           elif (computerChoice == 2):
               print('User chose s, computer chose p.')
               print('User wins this round.')
               winCount += 1
           elif (computerChoice == 3):
               print('User chose s, computer chose s.')
               print('This round is a tie.')
               tieCount += 1

        # Call the draw_Bar function to separate rounds of play.
        draw_Bar('-')

        # Read new input from user.
        userChoice = validate_input(input('Enter a command (rpsq): '))

    # When the user enters 'q', call the game_statistics function and user_statistics
    # function to calculate and display results.
    # Pass counting variables to the appropriate function.
    if userChoice == 'q':
        print()
        game_statistics(winCount, loseCount, tieCount, roundCount)
        user_statistics(rockCount, paperCount, scissorsCount, roundCount)
        print()
        print('Thanks for playing!')



# Define all functions:


# Display the rules of the game.
def game_rules():
    draw_Bar('*')
    print('Welcome to the Rock-Paper-Scissors game.')
    print('Enter a single character: r,s,p, or q to quit')
    print('Rock beats Scissors which beats Paper which beats Rock.')
    draw_Bar('*')

# Validate user input.
def validate_input(userChoice):
    while userChoice!='r' and userChoice!='p' and userChoice!='s' and userChoice!='q':
        print('Error. Try again.')
        userChoice = input('Enter a command (rpsq): ')
    return userChoice

# Draw a bar to separate
def draw_Bar(symbol):
    for x in range(40):
        print(symbol, end='')
    print()

# Select number randomly between 1 and 3.
def select_Random():
    return random.randint(1,3)

# Calculate and display game statistics.
def game_statistics(winCount, loseCount, tieCount, roundCount):
    print('Summary Statistics')

    userWinPercent = winCount / roundCount
    print('\tUser wins: ', winCount, ' (', format(userWinPercent, '.1%'), ')', sep='')

    computerWinPercent = loseCount / roundCount
    print('\tComputer wins: ', loseCount, ' (', format(computerWinPercent, '.1%'), ')', sep='')

    tiePercent = tieCount / roundCount
    print('\tTies: ', tieCount, ' (', format(tiePercent, '.1%'), ')', sep='')
    print()

# Calculate and display user statistics.
def user_statistics(rockCount, paperCount, scissorsCount, roundCount):
    print('User Statistics')
    rockPercent = rockCount / roundCount
    print('\tRock: ', rockCount, ' (', format(rockPercent, '.1%'), ')', sep='')

    paperPercent = paperCount / roundCount
    print('\tPaper: ', paperCount, ' (', format(paperPercent, '.1%'), ')', sep='')

    scissorsPercent = scissorsCount / roundCount
    print('\tScissors: ', scissorsCount, ' (', format(scissorsPercent, '.1%'), ')', sep='')


# Call the main function.
main()
