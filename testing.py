width = 20
height = 30

cord_wid = [[] for x in range(width)]

counter = 0
count = 0
count2 = 0
cord = [[] for x in range(width*height)]

while counter < height:
    for num in range(width):
        while count2 < width:
            cord_wid[count2].append(num)
            count2 += 1
        cord[count].append(num)
        count += 1
    cord += cord_wid
    counter += 1

import random


x={}
x['a']='apple'
x['b']='banana'
x['c']='chili dog'

def reverseLookup(d, value):
    listd = []
    for key in d.keys():
        if d[key] == value:
            listd.append(key)
    return listd
            
       
d = {'cat':7, 'coca':'cola', (1,2):3.2, 7:[1,2,3], \
     'hunde':'dogs', 'sieben':[1,2,3], 'dog':7, 'hamster':7}

def swap(d, k1, k2):
    k1value = d[k1]
    k2value = d[k2]
    d[k2] = k1value
    d[k1] = k2value


def subdict(d, keys):
    newdict = {}
    dvalues = d.values()
    for newkey in keys:
        if newkey in dvalues:
            newdict[newkey] = d[newkey]
    return newdict


ded = {(5,4):"clean"}

class Car:
  color = 'gray'
  def describeCar(self):
    return 'A cool ' + Car.color + ' car'
  def describeSelf(self):
    return 'A cool ' + self.color + ' car'

    
# List Comprehensions

def t():
    return [x*10 for x in range(5)]

def ThreeSeven(l):
    return [x for x in l if x % 3 == 0 or x % 7 == 0]

l1 = [4, 5, 6, 20, 21, 80, 108, 119]


def vowels(phrase):
    return [x for x in phrase if x.lower() in ['a','e','i','o','u']]

# print vowels("cat ib")

l1 = [10, 20, 30]
l2 = [1, 2, 3]
def unwrapped(l1,l2):
    new_list = []
    for y in range(len(l2)):
        for x in range(len(l2)):
            new_list.append(l1[y] + l2[x])
    return new_list

# print unwrapped(l1,l2)

def rec_exp(base, exp):
    if exp == 0:
        return 1
    else:
        return base*rec_exp(base, exp-1)

#def rec_mul(x,y):
#    if y == 0:
#        return 0
#    else:
#        return x+rec_mul(x,y-1)

def rec_mul(m,n):
    if n == 0 or m == 0:
        return 0
    elif n < 0 and m < 0:
        return -m+rec_mul(m,n+1)
    elif n > 0 and m < 0:
        return m+rec_mul(m,n-1)
    elif n < 0 and m > 0:
        return -m+rec_mul(m,n+1)
    else:
        return m+rec_mul(m,n-1)


# print count_zeros([3,3,0,3,3,3,0,35,5,5,50,0,0,0,21,0])
    

def qu():
    a = 0
    x = ""
    while a < 5:
        x += "cat" + x
        m = 7
        a += 1
    print x
    print m



def count_zerosd(aList):
    index = 0
    for num in aList:
        if num == 0:
            index += 1
    print index

    

def count_zeros(aList):
    if sum(aList) == 0:
        return len(aList)
    else:
        for num in range(len(aList)):
            if aList[num] != 0:
                del aList[num]
                return count_zeros(aList)



print count_zeros([5,5,5,0,0,0,23,4,0,213,0,1231,0])



def nullist(clist):
    if len(clist)==0:
        return 0
    else:
        if clist[0]==0:
            return 1+nullist(clist[1:])
        else:
            return nullist(clist[1:])

print nullist([5,5,5,0,0,0,23,4,0,213,0,1231,0])



