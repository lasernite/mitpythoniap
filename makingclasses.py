class Point:
    # A class that represents a 2D Point

    def __init__(self, x, y):
        """
        Initialization method, called when we create a point.
        Takes 2 arguments, x and y, that must be bumbers (ints or floats)
        """
        self.x = x  # Setting x for this instance to x
        self.y = y  # setting y for this instance to y

    def __str__(self):
        return str(self.x) + "," + str(self.y)
    
    def getX(self): #getter
        return self.x

    def setX(self, new_x):
        self.x = new_x

point1 = Point(5, 6)

print point1.x
print point1.y

point1.setX(8)

print point1.x
