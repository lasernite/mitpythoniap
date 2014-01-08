# Name: Laser Nite
# Kerberos: nite
# Date: 1/6/19
# homework_1.py

##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 **********"

# Do your work for Exercise 1.2 here

print "Hello, World!"


print "********** Exercise 1.3 **********"

# Do your work for Excercise 1.3 here. Hint - how many different
# variables will you need?

# Print a tic-tac-toe board
print "  |  |\n", "--------\n","  |  |\n", "--------\n", "  |  |"


print "********** Exercise 1.4 **********"

# Do your work for Exercise 1.4 here.

# Define variables for horizontal and vertical components of tic-tac-toe board
vertical = "  |  |\n"
horizontal = "--------\n"

print vertical, horizontal, vertical, horizontal, vertical # Print tic-tac-toe board


# Request and print user info, Exercise 2.1

# Request first name, last name, and date of birth
first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
print "Enter your date of birth:"
mo = raw_input("Month? ")
day = raw_input("Day? ")
year = raw_input("Year? ")


# Print Name and Date of birth in format "Name was born on Date"
print first_name, last_name, "was born on ", mo, day + ",", year + "."
