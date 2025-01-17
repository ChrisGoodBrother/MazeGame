import turtle
import pathfinder as pf

class Entity(turtle.Turtle):
    def __init__(self, shape="null", colour="null"):
        turtle.Turtle.__init__(self)
        self.shape(shape)
        self.color(colour)
        self.penup()
        self.speed(0)
        self.win = -1
        self.x = -1
        self.y = -1

    def get_position(self):
        return self.ycor(), self.xcor() 
    
    def make_move(self, move, maze_walls=[]):
        if move == "up":
            x = self.xcor()
            y = self.ycor() + 22
            if (x, y) not in maze_walls:
                self.goto(x, y)
                self.y -= 1
        elif move == "down":
            x = self.xcor()
            y = self.ycor() - 22
            if (x, y) not in maze_walls:
                self.goto(x, y)
                self.y += 1
        elif move == "left" and not (self.x == 0 and self.y == 1):
            x = self.xcor() - 22
            y = self.ycor()
            if (x, y) not in maze_walls:
                self.goto(x, y)
                self.x -= 1
        elif move == "right":
            x = self.xcor() + 22
            y = self.ycor()
            if (x, y) not in maze_walls:
                self.goto(x, y)
                self.x += 1
    
class Player(Entity):
    def __init__(self):
        Entity.__init__(self, "circle", "green")

class Opponent(Entity):
    def __init__(self):
        Entity.__init__(self, "circle", "red")
        self.cheatPath = []
    
    def calculateCheatPath(self, maze, opponentCoordinates, treasureCoordinates, difficulty):
        if difficulty == "easy":
            self.cheatPath = pf.dfs(maze, opponentCoordinates, treasureCoordinates)
        elif difficulty == "hard":
            self.cheatPath = pf.bfs(maze, opponentCoordinates, treasureCoordinates)

        if self.cheatPath:
            self.cheatPath.pop(0)
    
    def moveAccordingToPath(self):
        if self.cheatPath:
            nextStep = self.cheatPath.pop(0)
            if nextStep == (self.y - 1, self.x):
                self.make_move("up")
            elif nextStep == (self.y + 1, self.x):
                self.make_move("down")
            elif nextStep == (self.y, self.x - 1):
                self.make_move("left")
            elif nextStep == (self.y, self.x + 1):
                self.make_move("right")

class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.x = -1
        self.y = -1
        
    def get_position(self):
        return self.ycor(), self.xcor() 