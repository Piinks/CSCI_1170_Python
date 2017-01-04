# Program Exercise 6
# Kate Archer
# CSCI 1170-008
# September 28, 2015

# The purpose of this program is to get a number of
# seconds from the user and convert the seconds to
# days, hours, minutes, and seconds.

# Have then user input the seconds:
secondsStart = float(input('Enter number of seconds: '))

# Convert to days first.
days = int(secondsStart // 86400)

# Convert to hours next.
hours = int((secondsStart // 3600) % 24)

# Convert minutes next.
minutes = int((secondsStart // 60) % 60)

# Convert seconds last.
seconds = int(secondsStart % 60)

# Display the final result.
print(days, 'day(s),', hours, 'hour(s),', minutes, 'minute(s), and', seconds, 'second(s).')
