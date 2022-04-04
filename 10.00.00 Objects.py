#WHAT IS OBJECT ORIENTED PROGRAMMING?

#programming uses logic
#   logic dictates actions taken and how they are performed
#   focusing on the action is difficult; look at bigger picture

#object oriented programming makes it easier to relate actions and logic

#a class is a template for an object
#   user can create attributes and perform actions on it 

#STEP 1: DEFINE THE CLASS... 

#when making a new class, define it
#   do this by entering keyword class, followed by parenthesis
class Object():
#   notice colon after class definition
#       colon = indent any code pertaining to Object class

#STEP 2: DEFINE INITIALIZER... 

#when making a new class, define the initializer
#   class is the function that runs when a new instance of the class is created
#   used to define any variables or attributes used throughout the object
#   to define initializer, make a function with name __init__ (w/ two underscores)
# SYNTAX:    def __init__(self, type, diameter, pressure):   #must be first function of the class
#   self parameter is reference to current instance of class & used to access variables belonging to class
#   does not have to have name "self", but has to be first parameter of any function in class
#user can define defaults, in case values were not supplied in initializer:
    def __init__(self, balltype = "Basketball", diameter = 9.51, pressure = 8.0):

#STEP 3: DEFINE OBJECT ATTRIBUTES... 

#object attribute is data that the user wants to keep with an object
#   can be nums, str, and any other datatype
#   created in __init__ function
#   attributes are called properties in other programming langs

#__init__ is like any other function, but can be complicated
#   attribute "self" allows user to create an attribute that plays off of existing attribute
#       tells object that this attribute is found within itself
#   when attributes are defined, they are defined as a part of object's self
        self.BallType = ballType 
        self.Diameter = diameter
        self.Pressure = pressure
#attributes are initialized to the values passed to it
#   when defining or changing attributes within a class, refer to them with the "self.ATTRIBUTE" format
#       tells class the attribute is its own

#STEP 4: MAKE ACTIONS... 

#to create actions, define them as normal functions
#   except they need to take self as an argument (like __init__)
    def Circumference(self):
        circumference = math.pi * self.Diameter
        return circumference
#Circumference method has no parameters (other than self) & it calculates circumference of ball
#method ChangePressure adds amount to current pressure
#   NOTE: the current pressure is returned (no change since pressureChange not associated w/ value)
    def ChangePressure(self, pressureChange):
        self.Pressure += pressureChange
        return self.Pressure

#STEP 5: CREATE THE INSTANCE... 

#to use Object class, make an instance of the class first
#   in other words, call the class and assign to a variable
myball1 = Object("Basketball", 9.51, 8.0)
myball2 = Object("Volleyball", 8.15, 7.5)
myball3 = Object("Soccerball", 8.65, 9.0)
myball4 = Object()
#print state of each ball object:
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference())
#set new diameter to myball1:
myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

#STEP 6: USE THE OBJECTS... 

#change pressure of myball1:
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())


#COMPLETE OBJECT... 

from math import pi

# Step 1 - Define the class object "Ball"
class Ball ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):

# Step 3 - Define the object attributes
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure

# Step 4 - Define Actions (Methods) associated with the object
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference

# Step 4 - Here is another action
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure

# Step 5 - Create 4 instances of ball
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()

# Print the attributes
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference())

# Change the Diameter attribute of myball1
myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

# Add Pressure to myball1
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())