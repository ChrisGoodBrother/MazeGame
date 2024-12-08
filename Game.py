import turtle
import random
import pathfinder as pf
import mazegenerator as mgen
import imagetoarray as imtoar

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)

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

class PathSquare(turtle.Turtle): #Path square
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

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

def draw_path(path, maze_height, maze_width):

    x_start = -maze_width // 2 * 22
    y_start = maze_height // 2 * 22

    for y, x in path:
        posx = x_start + x * 22
        posy = y_start - y * 22
        path_squares.goto(posx, posy)
        path_squares.stamp()

def getRandomPosition(maze):
    while True:
        randX = random.randint(0, len(maze) - 1)
        randY = random.randint(0, len(maze[0]) - 1)

        if maze[randY][randX] == 0:
            return randX, randY

def placeEntity(maze, entity):
    x, y = getRandomPosition(maze)
    entity.x = x
    entity.y = y
    height = len(maze)
    width = len(maze[0])
    x_start = -width // 2 * 22
    y_start = height // 2 * 22
    screenx = x_start + entity.x  * 22
    screeny = y_start - entity.y * 22
    entity.goto(screenx, screeny)

def moveOpponent(maze, computer, treasure):
    path = pf.bfs(maze, (computer.x, computer.y), (treasure.x, treasure.y))

def isOnTreasure(entity, treasX, treasY):
        x, y = entity.position()
        if(treasX == x and treasY == y):
            return True
        return False

def changeTreasurePosition(treasure, maze):
    posx = treasure.x
    posy = treasure.y
    newx, newy = posx, posy

    while (posx, posy) == (newx, newy):
        newx, newy = getRandomPosition(maze)
    
    treasure.x, treasure.y = newx, newy

    newx = -210 + newx * 22
    newy = 210 - newy * 22
    treasure.goto(newx, newy)

    #window.ontimer(lambda: changeTreasurePosition(treasure, maze), 15000)

mazes = imtoar.convert_image_to_array(5)
selected_maze = mazes[0]
maze_walls = mgen.get_maze_walls(selected_maze)
window = mgen.generate_maze(selected_maze)

path_squares = PathSquare()

player = Player()
oppo = Opponent()
treasure = Treasure()

placeEntity(selected_maze, oppo)
placeEntity(selected_maze, player)
placeEntity(selected_maze, treasure)

window.listen()
window.onkey(player.move_up, "Up")
window.onkey(player.move_down, "Down")
window.onkey(player.move_left, "Left")
window.onkey(player.move_right, "Right")

moveOpponent(selected_maze, oppo, treasure)

path = pf.bfs(selected_maze, (oppo.y, oppo.x), (treasure.y, treasure.x))
print(oppo.x, oppo.y)
print(treasure.x, treasure.y)
print(path)

if path:
    draw_path(path, len(selected_maze), len(selected_maze[0]))

while True:
    
    treasX, treasY = treasure.position()

    if(isOnTreasure(player, treasX, treasY)):
        print("Player Won")
        break
    elif isOnTreasure(oppo, treasX, treasY):
        print("Opponent Won")
        break
        
    window.update()

window.update()
turtle.done()

#Instead of timer make it go by turns, every 15 turns the treasure changes place