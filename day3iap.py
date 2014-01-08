def odd(x):
    if x % 2 == 1:
        return True
    else:
        return False

def evalQuadratic(a, b, c, x):
    return a*x**2 + b*x + c

def quadraticRoots(a, b, c):
    if a == 0:
        return float(-c/b)
    else:
        root1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
        root2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
        return root1, root2



def threeline():
    newline()
    newline()
    newline()

def newline():
    print

def nineline():
    threeline()
    threeline()
    threeline()

def twentysevenline():
    nineline()
    nineline()
    nineline()
    
print 'cat'
twentysevenline()
print 'cat'
