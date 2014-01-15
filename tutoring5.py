from math import *

def pointDist(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    c = (a**2 + b**2)**0.5
    return c


def perpDist(point, line):
    top = abs(point[0]*line[0] + point[1]*line[1] + line[2])
    bottom = sqrt((line[0]**2)+(line[1]**2))
    return top/bottom

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

def myRange(n):
    count = 0
    list = []
    while count < n:
        list.append(count)
        count += 1
    return list


def everyOther(m):
    list = []
    for item in range(0,len(m),2):
        list.append(m[item])
    return list


def mean(n):
    if sum(n) == 0:
        return None
    else:
        mean = float(sum(n))/len(n)
    return mean

def foobar(aList):
    if 47 not in aList:
        aList.append(47)

    while 1 in aList:
        aList.remove(1)

    aList = list(set(aList))
    aList.sort()
    aList.reverse()
    return aList
        
foobar([4,8,7,1,1,1,9,4,3,1])

def piSeries(n):
    pii = 0
    for k in range(n):
        pii += (float((-1)**k))/(2*k+1)
    return pii*4

print piSeries(12345)
