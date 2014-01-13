from math import *

def pointDist(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    c = (a**2 + b**2)**0.5
    return c


def perpDist(point, line):
    top = abs(
    
