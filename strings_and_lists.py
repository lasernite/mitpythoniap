# Name: Laser Nite
# Kerberos: nite
# strings_and_lists.py

# **********  Exercise 5.1 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num
    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

##### YOUR CODE HERE #####
def cumulative_sum(number_list):
    # number_list is a list of numbers
    total = 0
    cumulative = []
    for num in number_list:
        total += num
        cumulative.append(total)
    return cumulative

# Test Cases
print "cumulative sum of [4,3,6] is:", cumulative_sum([4, 3, 6])
print "cumulative sum of [5, 8, -2] is:", cumulative_sum([5, 8, -2])
print "cumulative sum of [43, 0.43, -12] is:", cumulative_sum([43, 0.43, -12])

# **********  Exercise 5.2 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    if word[0] in VOWELS:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"
    

# Test Cases
print "bunny in pig latin is", pig_latin("bunny")
print "elephant in pig latin is", pig_latin("elephant")
print "DaMonkey in pig latin is", pig_latin("Monkey")
print "Laser in pig latin is", pig_latin("Laser")
print "armadillo in pig latin is", pig_latin("armadillo")
