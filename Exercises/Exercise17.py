# Exercise 17
# Kate Archer
# Program Description: This program reads a file name and the fileâs contents
#   and determines the following:
#   1) The number of alphabetic (upper and lower case) letters in the file
#   2) The number of digits in the file
#   3) The number of lines in the file
# CSCI 1170-08
# November 12, 2015

def main():
    fileName = get_File_Name()

    inFile = open(fileName, 'r')

    lineCount = 0; alphaCount = 0; digitCount = 0

    for line in inFile:
        lineCount += 1
        line = line.rstrip()
        for i in range (len(line)):
            if is_Alpha(line[i]):
                alphaCount += 1
            if is_Digit(line[i]):
                digitCount += 1

    inFile.close()
    print()
    print('The number of alphabetic characters is', alphaCount)
    print('The number of digits is', digitCount)
    print('The number of lines is', lineCount)



def get_File_Name():
    fileName = input('Enter the name of the file to open for read: ')
    try:
        open(fileName, 'r')
        return fileName
    except:
        print('An error occured.')
        get_File_Name()

def is_Alpha(i):
    try:
        i = int(i)
        return False
    except:
        if i =='' or i==' ' or i== '.':
            return False
        else: return True

def is_Digit(i):
    try:
        i = int(i)
        return True
    except:
        return False


main()
