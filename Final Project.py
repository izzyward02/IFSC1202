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
        self.canvas = [[" " for a in range(self.size)]for b in range(self.size)]
#   initialize methods... 
#       printSketch (no arguments)
    def printSketch(self):
#           prints canvas line by line
#           HINT: print canvas from last line to zeroth line w/ 1-step (puts origin at bottom)
        border = "+" + self.size * "-" + "+"
        print(border)
#           print current xpos, ypos, and direction under canvas
        for a in range(self.size):
            c = self.size - a - 1
            print("|", end = "")
            for b in range(self.size):
                print(self.canvas[c][b], end = "")
            print("|")
        print(border)
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
#           if pen is D, put * along the path
#           HINT: different code snippet for each direction; if turtle reaches canvas border, stop
        if self.direction == "U":
            if self.xPos + distance < self.size:
                self.xPos += distance
            else:
                self.xPos = self.size
        if self.direction == "D":
            if self.xPos - distance >= 0:
                self.xPos -= distance
            else:
                self.xPos = 0
        if self.direction == "R":
            if self.yPos + distance < self.size:
                self.yPos += distance
            else:
                self.xPos = self.size
        if self.direction == "L":
            if self.yPos - distance >= 0:
                self.yPos -= distance
            else:
                self.yPos = 0
        
        xMin = min(prevXPos, self.xPos)
        xMax = max(prevXPos, self.xPos)
        yMin = min(prevYPos, self.yPos)
        yMax = max(prevYPos, self.yPos)

        if self.pen == "D":
            for a in range(yMin, yMax - 1):
                for b in range(xMin, xMax + 1):
                    self.canvas[b][a] = "*"
fileTxt = open("Cshape.txt", "r")
fileRead = fileTxt.readlines()

size = int(fileRead[0])
drawing = Sketch(size)
for a in range(1, len(fileRead)):
    if fileRead[a].find(",") == -1:
        turtleMove = fileRead[a].strip()
        if turtleMove == "1":
            drawing.penUp()
        if turtleMove == "2":
            drawing.penDown()
        if turtleMove == "3":
            drawing.turnRight()
        if turtleMove == "4":
            drawing.turnLeft()
        if turtleMove == "6":
            drawing.printSketch()
    else:
        turtleMove, distance = fileRead[a].strip().split(",")
        drawing.move(int(distance))

#EXPECTED OUTPUT:

#+--------------------+
#|                    |
#|                    |
#|                    |
#|                    |
#|     ***********    |
#|     *         *    |
#|     *  ********    |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  ********    |
#|     *         *    |
#|     ***********    |
#|                    |
#|                    |
#|                    |
#|                    |
#+--------------------+
#X = 16  Y = 5  Direction = U