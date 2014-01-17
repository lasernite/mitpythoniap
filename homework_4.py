# Name: Laser Nite
# Kerberos: nite
# Homework_4.py

# Exercise 8.1 - Intro to Object Oriented Programming

''' 1. Local variables are those specific to, and created inside a function,
which cannot be accessed outside that function.

Object attributes, on the other hand, are data associated with a named attribute, like
a variable, that is associated with an object that represents a class.

2. the __init__(x) method

3. obj.do_something(self, attributes)

'''


# Exercise 8.2 - Understanding Objects

# 1.
class Address:
    
    def __init__(self, number, street_name):
        self.number = number
        self.street_name = street_name

# 2. (a)
''' The code should print out 5:30 '''
class Clock(object):

    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print self.time

clock = Clock('5:30')
clock.print_time()

''' The code does indeed print out 5:30

(b) Because __init__ initializes the class with attributes self and time. Then a
print_time function is created that references and sets the object attribute self.time,
through shortened 'time', followed by a statement that prints out the object attribute
value. Then, when the object 'clock' is created with the class and a time value of
5:30, it gains the ability to use the methods of the class, and so when the
function print_time() is called, the value of self.time which has been set to '5:30'
is printed. '''

# 3. (a) The code should print out 10:30. '''
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print time
clock = Clock('5:30')
clock.print_time('10:30')

# (b) It can be confusing, so they should have unique names.

# 4. (a) 







