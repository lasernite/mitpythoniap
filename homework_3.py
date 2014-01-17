# Name: Laser Nite
# Kerberos: nite
# homework_3.py

##### Template for Homework 3, exercises 6.1 - 7.2 ######

# **********  Exercise 6.1 **********

# broken

# def negate(num):
#     return -num

# def large_num(num):
#     res = (num > 10000)

# negate(b)
# neg_b = num
# print 'b:', b, 'neg_b:', neg_b

# big = large_num(b)
# print 'b is big:', big

# Bugs
##### BUG 1 #####

# b is undefined

##### BUG 2 #####

# nothing is returned by function large_num()

##### BUG 3 #####

# The negate() function should be equated to neg_b,
# not neg_b = num which are both undefined

# Working code:

def negate(num):
    return -num

def large_num(num):
    res = (num > 10000)
    return res

b = 500000
neg_b = negate(b)
print 'b:', b, 'neg_b:', neg_b

big = large_num(b)
print 'b is big:', big


# **********  Exercise 6.2 ********** 

# Define "mutable" and list what data structures have this characteristic

# Elements can be altered after creation:
# lists and dictionaries


# Define "immutable" and list what data structures have this characteristic

# Elements cannot be altered after creation:
# tuples and strings


# **********  Exercise 6.3 **********

def ball_collide(ball1, ball2):
    from math import sqrt
    '''
    Computes whether or not two balls are colliding
    
    ball1: a tuple of (x-coord, y-coord, radius) nums (ints and/or floats);
        represents first ball
    ball2: a tuple of (x-coord, y-coord, radius) nums (ints and/or floats); 
        represents second ball

    returns: True if the balls collide and False if they do not collide
    '''
    x1 = ball1[0]
    y1 = ball1[1]
    x2 = ball2[0]
    y2 = ball2[1]
    distance = sqrt((float(x2)-x1)**2+(float(y2)-y1)**2)
    if distance > float(ball1[2]) + ball2[2]:
        return False
    else:
        return True
    
    

print ball_collide((0,0,1),(1,1,1)) # Should return True
print ball_collide((0,0,0),(0,5,4.9)) # Should return False
print ball_collide((0,0,0),(0,5,5)) # Should return True

# Test Cases for Exercise 6.3
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True


# **********  Exercise 7.1 **********

classes = {"8.01L":"Physics", 18.01:"Calculus", 7.012:"Biology", 3.091:"Chemistry"}

def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    class_dict[class_num] = desc

add_class(18.01,"Calculus",classes)
add_class(8.02,"Physics 2",classes)
add_class(6.00,"Python",classes)
add_class("21W.032","Writing",classes)
add_class(15.310,"Managerial Psychology",classes)
    

def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    keys = class_dict.keys()
    count = 0
    for key in keys:
        strkey = str(key)
        if strkey[0] == str(course) or strkey[0] + strkey[1] == str(course):
            print str(key) + " - " + str(class_dict[key])
            count += 1

    if count == 0:
        print "No Course " + str(course) + " classes taken."

# Test Cases for Exercise 7.1
print
print "Classes in course 8 are: "
print_classes(8,classes)
print
print "Classes in course 18 are: "
print_classes(18, classes)
print
print "Classes in course 9 are: "
print_classes(9,classes)
print
print "Classes in course 21 are: "
print_classes(21,classes)
print
print "Classes in course 20 are: "
print_classes(20,classes)
print


# **********  Exercise 7.2 **********

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in

    returns: a dictionary with keys and values generated
    '''
    # create empty dictionary to use as our address book
    addrBook = {}
    # open file
    inputF = open(fileName)
    # loop through each line of the file
    for line in inputF:
        # split the line separated by commas
        splitted_line = line.split(',')
        # 0th and 1st index corresponds to LastName, FirstName
        name = splitted_line[0] + ', ' + splitted_line[1]
        # 2nd index is phone number
        phone = splitted_line[2]
        # all the rest are email addresses
        # do rstrip to remove possible newline character in the email
        email = [x.rstrip("\r\n") for x in splitted_line[3:]]
        # combine phone and email to be value of the key name
        addrBook[name] = [phone] + email

    # close the file when we're done!
    inputF.close()
    return addrBook

def changeEntry(addrBook, entry, field, newValue):
    '''
    Changes one entry in the specified address book.

    addrBook: a dictionary in the address book format
      returned by buildAddrBook.
    entry: a string; the pre-existing entry to change
    field: a string; the field to change (one of: "name",
      "phoneNumber", "emailAddress")
    newValue: the new value for the specified field

    returns: nothing; only modifies addrBook
    '''
    if entry not in addrBook.keys():
        return "Invalid entry. Try a different name."
    elif field == "phoneNumber":
        addrBook[entry][0] = newValue
    elif field == "emailAddress":
        addrBook[entry].append(newValue)
    elif field == "name":
       addrBook[newValue] = addrBook[entry]
       del addrBook[entry]
    else:
        return "Invalid field"


print buildAddrBook("rawAddresses.csv")
print
changeEntry(buildAddrBook("rawAddresses.csv"), 'Obama, Barack', "name", "dog man pan")
print addrBook

