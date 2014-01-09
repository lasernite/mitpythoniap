# Name: Laser Nite
# Kerberos: nite
# homework_2b.py

##### Template for Homework 2, exercises 4.1-4.2  ######

# ********** Exercise 4.1 **********

## 1 - decimal values
list = range(2,11)
for x in list:
    print 1.0/x
    
## 2 - countdown
##### YOUR CODE HERE #####

# Get input from user
num = input("Enter a number to countdown! ")

# Countdown
if type(num) == int and num >= 0:
    while num >= 0:
        print str(num)
        num = num - 1
elif type(num) == int and num < 0:
    while num <= 0:
        print str(num)
        num = num + 1
else:
    print "Invalid input! Enter an integer!"
        



## 3 - exponentiation
base = input("Enter a base for exponentation: ")
exp = input("Enter an exponent: ")

num = base
for x in range(1,exp):
    num = num * base
print num

## 4 - even/odd

num = raw_input("Enter a number divisible by 2: ")
while float(num) % 2 != 0:
    print "How Odd! (Isn't that original?)"
    num = input("Enter a number divisible by 2: ")
print "Yay you escaped (certain death)!"
    

# ********** Exercise 4.2 **********

## 1 - rand_divis_3 function
from random import randint

def rand_div_3():
    a = randint(1,100)
    print a
    if a % 3 == 0:
        return True
    else:
        return False

print rand_div_3()

# Test Cases

print randint(1,100)
print randint(1,100)
print randint(1,100)
print randint(100,201)

## 2 - roll_dice function - remember that a die's lowest number is 1;
                          #its highest is the number of sides it has

def roll_dice(s, n):
    print "Your rolls are: "
    for i in range(n):
        print randint(1,s)
    print "That's all!"

roll_dice(20,5)


# Test Cases
roll_dice(6,10)
roll_dice(3,5)
roll_dice(8,4)
