#Izzy Ward      Final Project       IFSC 1202       05.02.22

#Simulate the operation of the turtle & create a computerized sketchpad
#create a 2D list "canvas" where each element is initialized into a single space
#   read commands from a file containing instructions for the shape
#       NOTE: first value of Cshape.txt is the value of the canvas
#   turtle should start at (0,0), direction up, pen up

#TURTLE COMMANDS:
#   1 = pen up
#   2 = pen down
#   3 = turn right
#   4 = turn left
#   5,# = move forward # spaces
#   6 = print canvas

#create object Sketch that holds value & actions for sketchpad
class Sketch():
#   define attributes...
    def __init__(self, size):
#       size = size of square canvas (determined when obj is initialized)
#       xpos = current x position of turtle (default = 0)
#       ypos = current y position of turtle (default = 0)
#       direction = current direction of turtle (default = U)
#       pen = pen is up or down (default = U)
#       canvas = 2D list containing spaces or "*" (default = " ")
        self.size = size
        self.xPos = 0
        self.yPos = 0
        self.direction = "U"
        self.pen = "U"
        self.canvas = []
#   initialize methods... 
#       printSketch (no arguments)
    def printSketch(self):
#           prints canvas line by line
#           HINT: print canvas from last line to zeroth line w/ 1-step (puts origin at bottom)
        print("+" + ("-" * int(self.size)) + "+")
#           print current xpos, ypos, and direction under canvas
        for a in range(len(self.canvas)):
            print("|", end = "")
            for b in range(len(self.canvas[a])):
                print(self.canvas[a][b], end = "")
            print("|")
        print("+" + ("-" * int(self.size)) + "+")
        print("X = " + str(self.xPos) + "  " + "Y = " + str(self.yPos) + "  " + "Direction = " + self.direction)
#       penUp (no arguments)
    def penUp(self):
#           sets penUp to U
        self.pen = "U"
#       penDown (no arguments)
    def penDown(self):
#           sets penDown to D
        self.pen = "D"
#       turnLeft (no arguments)
    def turnLeft(self):
#           sets direction to new CCW direction (HINT: check current direction to determine new direction)
        if self.direction == "U":
            self.direction == "L"
        elif self.direction == "L":
            self.direction == "D"
        elif self.direction == "D":
            self.direction == "R"
        elif self.direction == "R":
            self.direction == "U"
#       turnRight (no arguments)
    def turnRight(self):
#           sets direction to new CW direction (HINT: check current direction to determine new direction)
        if self.direction == "U":
            self.direction == "R"
        elif self.direction == "L":
            self.direction == "U"
        elif self.direction == "D":
            self.direction == "L"
        elif self.direction == "R":
            self.direction == "D"
#       move (self, distance)
    def move(self, distance):
#           moves turtle from current xpos, ypos along current direction
        prevXPos = self.xPos
        prevYPos = self.yPos

        if self.direction == "R":
            newYPos = int(self.yPos) + distance
            if newYPos >= int(self.size):
                newYPos = int(self.size) - 1
            if self.pen == "D":
                for a in range(newYPos - self.yPos):
                    self.canvas[prevXPos][self.yPos + a] = "*"
            newXPos = self.xPos
        elif self.direction == "L":
            newYPos = int(self.yPos) - distance
            if newYPos < 0:
                newYPos  = 0
            if self.pen == "D":
                for a in range(self.yPos - newYPos):
                    self.canvas[prevXPos][self.yPos - a] = "*"
                    self.yPos -= 1
            newXPos = self.xPos
        elif self.direction == "U":
            newXPos = int(self.xPos) + distance
            if newXPos >= int(self.size):
                newXPos = int(self.size) - 1
            if self.pen == "D":
                for a in range(newXPos - self.xPos):
                    self.canvas[self.xPos + a][prevYPos] = "*"
            newYPos = self.yPos
        elif self.direction == "D":
            newXPos = int(self.xPos) - distance
            if newXPos < 0:
                newXPos = 0
            if self.pen == "D":
                for a in range(newXPos - self.xPos):
                    self.canvas[self.xPos - a][prevYPos] = "*"
            newYPos = self.yPos
        self.xPos = newXPos
        self.yPos = newYPos
#           if pen is D, put * along the path
#           HINT: different code snippet for each direction; if turtle reaches canvas border, stop
with open("Cshape.txt") as commands:
    drawList = []
    for command in commands:
        if command != "\n":
            line = command.split(",")
            for a in range(len(line)):
                line[a] = line[a].strip()
            drawList.append(line)
    cSketch = Sketch(drawList[0][0])
    cSketch.canvas = int(cSketch.size) * [int(cSketch.size) * [" "]]
    for a in range(1, len(drawList)):
        if int(drawList[a][0]) == 1:
            cSketch.penUp()
        elif int(drawList[a][0]) == 2:
            cSketch.penDown()
        elif int(drawList[a][0]) == 3:
            cSketch.turnRight()
        elif int(drawList[a][0]) == 4:
            cSketch.turnLeft()
        elif int(drawList[a][0]) == 5:
            cSketch.move(int(drawList[a][1]))
        elif int(drawList[a][0]) == 6:
            cSketch.printSketch()
print()
