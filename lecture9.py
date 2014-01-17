####### Lecture 9 #######

####### Recursion #######

# 1. Break a problem into smaller parts
# 2. Evaluate these sub-parts
# 3. Put everything back together

# Recursion is usually written as a function
# calling itself

# Recursion generally DOES NOT involve for
# or while loops



#########################
# String reversal

def reverseString(string):
    """returns string in reverse"""
    # Base case
    if string == '':
        return ''
##    if len(string) == 1:
##        return string
    # Recursive case
    else:
        return string[-1] + reverseString(string[:-1])

# print reverseString('hello')

#########################
# Fibonacci numbers

fibCount = 0

def fibMemo(n):
    return fibonacci(n, {})

# From http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap04.html
def fibonacci(n, memoDict):
    """Calculates the nth fibonacci number"""
    # Counting the number of calls
    global fibCount
    fibCount += 1
    # Memoized solution
    if n in memoDict:
        return memoDict[n]
    # Base cases
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        result = fibonacci(n-1, memoDict)  + fibonacci(n-2, memoDict)
        # Add the result to the dictionary
        memoDict[n] = result
        return result

# print fibMemo(3), fibCount
# print fibMemo(36), fibCount - 5 # I know fibCount is 5 for fib(3)



    

###########################
# Binary search

# Given a sorted list and an element, return either an index
# where that element can be found, or None if one does not exist.
def binary_search(l, elem):
    # Base case: element is not in an empty list
    if len(l) == 0:
        return None

    # Look for element in the middle
    mid = len(l)/2
    if l[mid] == elem:
        return mid
    
    # If not there, look in the half that would contain elem (recurse)
    if elem > l[mid]:
        sub = binary_search(l[mid+1:], elem)
        if sub is None:
            return None
        else:
            return mid + 1 + sub
    else: # elem < l[mid]
        return binary_search(l[:mid], elem)


# print binary_search(range(10), 0)
# print binary_search(range(10), 6)
# print binary_search(range(10), 11)
# print binary_search(range(10), -2)

###########################
# Merge sort

# Sorts a list, using the merge sort algorithm.
def merge_sort(l):
    # Base case: length 1 list is sorted
    if len(l) == 1:
        return l

    # Otherwise, split into 2 subproblems, sort recursively, and merge

    # split list into halves
    mid = len(l)/2  # integer division on purpose!
    lower = l[:mid]
    upper = l[mid:]

    # recursively sort halves
    lower = merge_sort(lower)
    upper = merge_sort(upper)

    # combine the sorted results
    return merge(lower, upper)


# helper method to merge already-sorted lists
def merge(l1, l2):
    # if either list empty, return the other
    if len(l1) == 0:
        return l2;
    elif len(l2) == 0:
        return l1

    # otherwise, pull off smaller element and keep going
    else:
        if l1[0] <= l2[0]:
            return [l1[0]] + merge(l1[1:], l2)
        return [l2[0]] + merge(l1, l2[1:])



# print merge_sort([5,4,7,2,8,4,1])




def countdown(n):
    if n == 0:
        print "Blastoff!"
    else:
        print n
        countdown(n-1)

def dash(n):
    print "-"*n


def dashfun(loops, size):
    if loops > 0:
        for a in range(1,size):
            dash(a)
        for a in reversed(range(1,size)):
            dash(a)
        dashfun(loops-1,size)
    else:
        return
        



def is_a_vowel2(char):
    char = char.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False

def is_a_vowel(char):
    char = char.lower()
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    else:
        return False


def count_all_vowels(sent):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in sent:
        if is_a_vowel(letter):
            count += 1
    return count


def sum_digits(aStr):
    total = 0
    strange = ['1','2','3','4','5','6','7','8','9']
    for s in aStr:
        if s in strange:
            total += int(s)
    return total


def is_palindrome(aStr):
    aStr = aStr.replace(" ", "")
    aStr = aStr.lower()
    if aStr == aStr[::-1]:
        return True
    else:
        return False


def most_freq_char(aStr):
    max_count = 0
    max_char = ""
    for char in aStr:
        occur = aStr.count(char)
        if occur > max_count:
            max_count = occur
            max_char = char
    return max_char






    
