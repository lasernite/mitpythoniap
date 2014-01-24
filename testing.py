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

print ded[(5,4)]
    
