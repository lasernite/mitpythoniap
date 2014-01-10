def quadraticRoots(a, b, c):
    complex(a, b)
    if a == 0:
        return float(-c/b)
    else:
        root1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
        root2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
        return root1, root2

def clip(lo, x, hi):
    low = min(lo, x, hi)
    high = max(lo, x, hi)
    x_high = min(x, hi)
    x_low = max(x, lo)
    return lo and x and hi

count = 0
for letter in 'Snow!':
    print 'Letter #', count, 'is', letter
    count += 1
    break
print count

def foo(x, y):
    # Make x's value over 100, if it isn't already
    while True:
        if x >= 100:
            break
        else:
            x = x + 1
    return x

def convert_knuts(knuts):
    sickles = 0
    galleons = 0
    while knuts > 29:
        sickles += 1
        knuts +- 29
        if sickles > 17:
            galleons += 1
            sickles -= 17
    print galleons, "galleons,", sickles, "sickles, and", knuts, "knuts."

print convert_knuts(343)
