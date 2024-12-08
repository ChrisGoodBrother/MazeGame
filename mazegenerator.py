import turtle

class Individual:
    def __init__(self, maze):
        self.fitness = 0
        self.maze = maze
        self.geneLength = len(maze) - 1
    
    def calculateFitness(self):
        pass

    def __str__(self):
        return f"{self.maze}"

class Population:

    def __init__(self, mazes):
        self.populationSize = len(mazes)

        self.individuals = []
        for maze in mazes:
            self.individuals.append(Individual(maze))
    
    def printIndividuals(self):
        for individual in self.individuals:
            print(individual)

    def getPopSize(self):
        print(self.populationSize)

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

def get_maze_walls(maze):
    maze_walls = []
    height = len(maze)
    width = len(maze[0])

    x_start = -width // 2 * 22
    y_start = height // 2 * 22

    for y in range(height):
        for x in range(width):
            item = maze[y][x] #Get maze wall or pathway

            posx = x_start + x * 22 #Get the position for x
            posy = y_start - y * 22 #Get the position for y

            if(item == 1):
                maze_walls.append((posx, posy))
    return maze_walls

def draw_maze(maze):

    white_squares = WhiteSquare()
    black_squares = BlackSquare()

    maze_walls = []

    height = len(maze)
    width = len(maze[0])

    x_start = -width // 2 * 22
    y_start = height // 2 * 22

    for y in range(height):
        for x in range(width):
            item = maze[y][x] #Get maze wall or pathway

            posx = x_start + x * 22 #Get the position for x
            posy = y_start - y * 22 #Get the position for y

            if(item == 1): #For wall
                black_squares.goto(posx, posy) #Go to position
                black_squares.stamp() #Draw square
                maze_walls.append((posx, posy))
            else: #For pathway
                white_squares.goto(posx, posy)
                white_squares.stamp()

def generate_maze(maze):

    window = turtle.Screen()
    window.screensize(500, 500)
    window.bgcolor("blue")
    window.tracer(0)

    draw_maze(maze)

    return window