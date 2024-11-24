import turtle
import random

maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "XXX  XXXX X    XX XX",
    "XX   X XX X  XXXX  X",
    "X  XXX XX X   XXX  X",
    "X  XXX XX X  XXXX  X",
    "X  XXX       XXXX  X",
    "X  X XXX XXX XXXX  X",
    "X      X           X",
    "XXXXX  X           X",
    "XXXXX  X  XXXXXXX  X",
    "XXXXX  X  XXXXXXX  X",
    "XX     X  XXX XXX  X",
    "XX XXXXX  XXX XXX  X",
    "XX                 X",
    "XX XXXXX  X XXXXX  X",
    "X  XXXXX XX  XXXX  X",
    "X        XX  XXXX  X",
    "XXXXX  XXXXXX      X",
    "XXXXX  XXXXXX  XXXXX",
    "XXXXXXXXXXXXXXXXXXXX",
]

class BlackSquare(turtle.Turtle): #Black square
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class WhiteSquare(turtle.Turtle): #White square
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)

    def isOnTreasure(self, treasX, treasY):
        x, y = self.position()
        if(treasX == x and treasY == y):
            return True
        return False

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + 22
        if (x, y) not in maze_walls:
            self.goto(x, y)
    def move_down(self):
        x = self.xcor()
        y = self.ycor() - 22
        if (x, y) not in maze_walls:
            self.goto(x, y)
    def move_left(self):
        x = self.xcor() - 22
        y = self.ycor()
        if (x, y) not in maze_walls:
            self.goto(x, y)
    def move_right(self):
        x = self.xcor() + 22
        y = self.ycor()
        if (x, y) not in maze_walls:
            self.goto(x, y)

class Opponent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.win = -1

class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("yellow")
        self.penup()
        self.speed(0)

def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            item = maze[y][x] #Get maze wall or pathway

            posx = -210 + x * 22 #Get the position for x
            posy = 210 - y * 22 #Get the position for y

            if(item == "X"): #For wall
                black_squares.goto(posx, posy) #Go to position
                black_squares.stamp() #Draw square
                maze_walls.append((posx, posy))
            else: #For pathway
                white_squares.goto(posx, posy)
                white_squares.stamp()

def getRandomPosition(maze):
    while True:
        randX = random.randint(0, len(maze) - 1)
        randY = random.randint(0, len(maze[0]) - 1)

        if maze[randY][randX] == " ":
            return randX, randY

def placeEntity(maze, entity):
    x, y = getRandomPosition(maze)
    entity.x = x
    entity.y = y
    x = -210 + x  * 22
    y = 210 - y * 22
    entity.goto(x, y)

def moveOpponent(computer):
    computer.goto(-210 + 2 * 22, 210 - 2 * 22)

window = turtle.Screen()
window.screensize(500,500)
window.bgcolor("blue")
window.tracer(0)

white_squares = WhiteSquare()
black_squares = BlackSquare()

maze_walls = []
draw_maze(maze)

player = Player()
oppo = Opponent()
treasure = Treasure()

placeEntity(maze, oppo)
placeEntity(maze, player)
placeEntity(maze, treasure)

window.listen()
window.onkey(player.move_up, "Up")
window.onkey(player.move_down, "Down")
window.onkey(player.move_left, "Left")
window.onkey(player.move_right, "Right")

while True:
    treasX, treasY = treasure.position()
    if(player.isOnTreasure(treasX, treasY)):
        print("Player Won")
        window.update()
        turtle.done()
        
    window.update()