# Name: Laser Nite
# Kerberos: nite
# Homework_4.py

# Exercise 8.1 - Intro to Object Oriented Programming

''' 1. Local variables are those specific to, and created inside a function,
which cannot be accessed outside that function.

Object attributes, on the other hand, are data associated with a named attribute, like
a variable, that is associated with an object that represents a class.

2. the __init__(x) method

3. obj.do_something(self, attributes)

'''


# Exercise 8.2 - Understanding Objects

# 1.
class Address:
    
    def __init__(self, number, street_name):
        self.number = number
        self.street_name = street_name

# 2. (a)
''' The code should print out 5:30 '''
class Clock(object):

    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print self.time

clock = Clock('5:30')
clock.print_time()

''' The code does indeed print out 5:30

(b) Because __init__ initializes the class with attributes self and time. Then a
print_time function is created that references and sets the object attribute self.time,
through shortened 'time', followed by a statement that prints out the object attribute
value. Then, when the object 'clock' is created with the class and a time value of
5:30, it gains the ability to use the methods of the class, and so when the
function print_time() is called, the value of self.time which has been set to '5:30'
is printed. '''

# 3. (a) The code should print out 10:30. '''
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print time
clock = Clock('5:30')
clock.print_time('10:30')

# (b) It can be confusing, so they should have unique names.

# 4. (a) Since paris_clock is made an alias of boston_clock, 10:30 should be printed
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print self.time
boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
# (b) They do not act like different objects as they are aliases of eachother



# Exercise 9.1 - Designing Your Own Inheritance
class Computer:
    def __init__(self, laptop, desktop, mobile, software):
        self.laptop = laptop
        self.desktop = desktop
        self.mobile = mobile
        self.software = software

class Apple(Computer):
    def __init__(self, ipod):
        Computer.__init__(self, laptop, desktop, mobile, software)
        self.ipod = ipod
        software = "OSX and iOS"
        laptop = "Macbook"
        desktop = "iMac"
        mobile = "iPhone"

class Windows(Computer):
    def __init__(self, software, game_systems):
        Computer.__init__(self, laptop, desktop, mobile, software)
        software = "Windows 8"
        self.game_systems = game_systems

class Linux(Computer):
    def __init__(self, open_source, free):
        Computer.__init__(self, laptop, desktop, mobile, software)
        self.open_source = open_source
        self.free = free
        software = "Linux"


# Exercise 9.2 - More Inheritance
       
# 1. Parent classes: Spell
# Child classes: Accio and Confundo

# 2. Accio
# Summoning Charm Accio
# No description
# Confundus Charm Confundo
# Causes the victim to become confused and befuddled

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()
    def get_description(self):
        return 'No description'
    def execute(self):
        print self.incantation
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def get_description(self):
        return 'This charm summons an object to the caster, potentilly over a \
significant distance'
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'
def study_spell(spell):
    print spell
spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

# Yay, my guesses were all correct :)


# 3. Confundo's, because __str__(self) references self.get_description() and because
# Confudo() is the child class, it's definition of a function overides the parent class

# 4. Under the class Accio should be a method that looks like:
'''
def get_description(self):
    return 'This charm summons an object to the caster, potentilly over a
    significant distance'
'''


