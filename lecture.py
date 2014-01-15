###### Lecture 8 ######

class Rectangle():

    def __init__(self, coord1, coord2):
        """Creates a rectangle object defined
        by two corners, given by coord1 and coord2.
        coord1 and coord2: tuples of x,y values."""
        self.corner1 = coord1
        self.corner2 = coord2
        self.color = None

    def getCorners(self):
        """returns the coordinates of both corners"""
        return self.corner1, self.corner2

    def getCorner1(self):
        """returns the coordinates of corner1"""
        return self.corner1

    def getCorner2(self):
        """returns the coordinates of corner2"""
        return self.corner2

    def getColor(self):
        """returns the rectangles color"""
        return self.color

    def setCorner1(self, newCoord):
        """assigns corner1 to a new point"""
        self.corner1 = newCoord

    def setCorner2(self, newCoord):
        """assigns corner2 to a new point"""
        self.corner2 = newCoord

    def setColor(self, color):
        """sets the rectangle's color
        color: a string"""
        self.color = color

    def getArea(self):
        """returns the area of the rectangle"""
        side1Length = abs(self.corner1[0] - self.corner2[0])
        side2Length = abs(self.corner1[1] - self.corner2[1])
        return side1Length * side2Length

    def getPerimeter(self):
        """returns the perimeter of the rectangle"""
        side1Length = abs(self.corner1[0] - self.corner2[0])
        side2Length = abs(self.corner1[1] - self.corner2[1])
        return 2 * side1Length + 2 * side2Length


rectangle1 = Rectangle((0,0), (5,5))
rectangle1.setColor("blue")
print rectangle1.color # "blue"

rectangle2 = Rectangle((0,5), (5,0))
print rectangle2.color # None because we never set a color

class Square(Rectangle): # child of Rectangle; a Square *is* a Rectangle

    def __init__(self, coord1, width):
        """Creates a Square instance by calling the Rectangle
        constructor.
        coord1: The lower left corner of the square; (x,y) tuple
        width: int or float length of side"""
        # We're using inheritance to call the Rectangle class
        # by only taking one point as an argument to the Square
        # __init__ method, we can calculate the other point
        # and ensure the object is actually a square
        Rectangle.__init__(self, coord1, (coord1[0] + width, coord1[1] + width))

    def getArea(self):
        """returns the area of the square"""
        # Technically, someone could have accessed the setCorner
        # methods from Rectangle to mess things up, but we're
        # going to assume that can't happen for simplicity's sake.
        sideLength = self.corner1[0] - self.corner2[0]
        return sideLength ** 2

    def getPerimeter(self):
        """returns the perimeter of the square"""
        sideLength = self.corner2[0] - self.corner1[0]
        return sideLength * 4


square1 = Square((0,0), 5) # creates a square has the same coordinates as
# the Rectangle from earlier
square1.getArea()
square1.setColor("hot pink")
print "square1 color:", square1.getColor()
Square.setColor(square1, "hot red") # reminder of how self is assigned to arguments
print "square1 color:", square1.getColor()
