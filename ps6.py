# Project 2: Simulating robots
# Name: Laser Nite
# Collaborators: None
# Kerberos: Nite

import math
from math import *
import random

import ps6_visualize
import pylab

# For python 2.6:
# from ps6_verify_movement26 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for python 2.7):
from ps6_verify_movement27 import testRobotMovement

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.clean_dic = {}
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.clean_dic[(pos.x, pos.y)] = "clean"
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m,n) in self.clean_dic.keys():
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.clean_dic)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.randrange(self.width), random.randrange(self.height))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.x
        y = pos.y
        return x >= 0 and y >= 0 and x <= self.width -1 and y <= self.height - 1


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = int(random.randrange(360))
        self.position = Position(random.randrange(self.room.width), random.randrange(self.room.height))
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # self.position = Position.getNewPosition(self.angle, self.speed)
        # self.room.cleanTileAtPosition(self.position)
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        currentposition = Position(self.getRobotPosition().x, self.getRobotPosition().y) 
        nextposition = currentposition.getNewPosition(self.getRobotDirection(), self.speed)
        nextposx = nextposition.getX()
        nextposy = nextposition.getY()
        if nextposx > self.room.width or nextposy > self.room.height or nextposx < 0 or nextposy < 0:
            # set new random direction
            self.room.cleanTileAtPosition(Position(floor(self.position.x),floor(self.position.y)))
            self.setRobotDirection(random.randrange(360))
        else:
            # move to newposition, clean tile
            self.room.cleanTileAtPosition(Position(floor(self.position.x),floor(self.position.y)))
            self.position = nextposition
       
            
        

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    time_steps = 0
    room = RectangularRoom(width, height)
    robots = []
    for bot in range(num_robots):
        robots.append(robot_type(room, speed))
    trials = 0
    total_time_steps = 0
    while trials < num_trials:
        anim = ps6_visualize.RobotVisualization(num_robots, width, height, 0.01)
        while room.getNumCleanedTiles() < room.getNumTiles()*min_coverage:
            anim.update(room, robots)
            for botid in range(len(robots)):
                robots[botid].updatePositionAndClean()
            time_steps += 1
        total_time_steps += time_steps
        time_steps = 0
        trials += 1
        room.clean_dic = {}
        anim.done()
    return total_time_steps/trials

print runSimulation(5, 1, 10, 25, 1, 2, StandardRobot)

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        currentposition = Position(self.getRobotPosition().x, self.getRobotPosition().y) 
        nextposition = currentposition.getNewPosition(self.getRobotDirection(), self.speed)
        nextposx = nextposition.getX()
        nextposy = nextposition.getY()
        if nextposx > self.room.width or nextposy > self.room.height or nextposx < 0 or nextposy < 0:
            # set new random direction
            self.room.cleanTileAtPosition(Position(floor(self.position.x),floor(self.position.y)))
            self.setRobotDirection(random.randrange(360))
        else:
            # move to newposition, clean tile
            self.room.cleanTileAtPosition(Position(floor(self.position.x),floor(self.position.y)))
            self.position = nextposition
            self.setRobotDirection(random.randrange(360))

# testRobotMovement(RandomWalkRobot, RectangularRoom)


# === Problem 5
#
# 1a) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your comment here ...)
#
# 1b) How does the performance of the two robot types compare when cleaning 80%
#       of a 20x20 room?
#
#       (... your comment here ...)
#
# 2a) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your comment here ...)
#
# 2b) How does the performance of the two robot types compare when two of each
#       robot cleans 80% of rooms with dimensions 
#       10x30, 20x15, 25x12, 50x6
#
#       (... your comment here ...)
#

def showPlot1(title, x_label, y_label):
    """
    Produces a plot comparing the two robot strategies in a 20x20 room with 80%
    minimum coverage.
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# showPlot1("Robots # Vs. Cleaning Speed", "Number of Robots", "Number of Time-Steps")

    
def showPlot2(title, x_label, y_label):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# showPlot2("Size of Room vs Cleaning Time", "Room Ratio", "Time-Steps")
