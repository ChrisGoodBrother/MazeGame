import turtle
import random
from PIL import Image as im
import numpy as np
import dfs_pathfinder as dfs

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

def draw_maze(maze):

    height = len(maze)
    width = len(maze[0])

    x_start = -width // 2 * 22
    y_start = height // 2 * 22
    #print(height, width)

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

def draw_path(path, x_start, y_start):
    # Draw the DFS path in green
    for y, x in path:
        posx = x_start + x * 22  # Calculate the position for x
        posy = y_start - y * 22  # Calculate the position for y
        path_square.goto(posx, posy)
        path_square.stamp()

mazes = []

for i in range(1, 6):
    image = im.open(f'mazes/maze{i}.png')
    image = image.convert('L')
    data = np.asarray(image)
    threshold = 128
    maze = (data < threshold).astype(int)
    mazes.append(maze)

# Find the path using DFS
path = dfs.dfs(mazes[0], (1, 0), (19, 20))

# Create the turtle window
window = turtle.Screen()
window.screensize(500, 500)
window.bgcolor("blue")
window.tracer(0)

# Initialize turtle objects for drawing
white_squares = WhiteSquare()
black_squares = BlackSquare()
path_square = turtle.Turtle()  # Create a new turtle for the path
path_square.shape("square")
path_square.color("green")
path_square.penup()
path_square.speed(0)

# Store maze walls for reference
maze_walls = []

# Draw the maze
draw_maze(mazes[0])

# Draw the DFS path in green
if path:
    draw_path(path, -mazes[0].shape[1] // 2 * 22, mazes[0].shape[0] // 2 * 22)

# Keep the window open
while True:
    window.update()