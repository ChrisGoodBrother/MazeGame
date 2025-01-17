import turtle
import random
import pathfinder as pf
import mazegenerator as mgen
import imagetoarray as imtoar
import Entity

class Game:
    def __init__(self, maze, player=Entity.Player(), opponent=Entity.Opponent(), treasure=Entity.Treasure()):
        self.maze = maze
        self.player = player #Create Playable Player
        self.opponent = opponent #Create Computer Opponent
        self.treasure = treasure #Create Treasure Entity
    
    def getRandomPosition(self):
        while True:
            randX = random.randint(0, len(self.maze) - 1)
            randY = random.randint(0, len(self.maze[0]) - 1)

            if self.maze[randY][randX] == 0:
                return randX, randY

    def placeTreasure(self, entity):
        x, y = self.getRandomPosition()
        entity.x = x
        entity.y = y
        height = len(self.maze)
        width = len(self.maze[0])
        x_start = -width // 2 * 22
        y_start = height // 2 * 22
        screenx = x_start + entity.x  * 22
        screeny = y_start - entity.y * 22
        entity.goto(screenx, screeny)
    
    def placeEntity(self, entity):
        x, y = 0, 1
        entity.x = x
        entity.y = y
        height = len(self.maze)
        width = len(self.maze[0])
        x_start = -width // 2 * 22
        y_start = height // 2 * 22
        screenx = x_start + entity.x  * 22
        screeny = y_start - entity.y * 22
        entity.goto(screenx, screeny)
    
    def isOnTreasure(self, entity, treasX, treasY):
        x, y = entity.position()
        if(treasX == x and treasY == y):
            return True
        return False
    
    def runGame(self):
        maze_walls = mgen.get_maze_walls(self.maze) #Get maze walls
        window = mgen.generate_maze(self.maze) #Draw maze

        self.placeEntity(self.player)
        self.placeEntity(self.opponent)
        self.placeTreasure(self.treasure)

        self.opponent.calculateCheatPath(self.maze, (self.opponent.y, self.opponent.x), (self.treasure.y, self.treasure.x), "hard")

        window.listen()
        window.onkey(lambda: (self.player.make_move("up", maze_walls), self.opponent.moveAccordingToPath()), "Up")
        window.onkey(lambda: (self.player.make_move("down", maze_walls), self.opponent.moveAccordingToPath()), "Down")
        window.onkey(lambda: (self.player.make_move("left", maze_walls), self.opponent.moveAccordingToPath()), "Left")
        window.onkey(lambda: (self.player.make_move("right", maze_walls), self.opponent.moveAccordingToPath()), "Right")
        
        while True:
            treasX, treasY = self.treasure.position()

            if(self.isOnTreasure(self.player, treasX, treasY)):
                print("Player Won")
                break
            elif self.isOnTreasure(self.opponent, treasX, treasY):
                print("Opponent Won")
                break
                
            window.update()

        window.update()
        turtle.done()

mazes = imtoar.convert_image_to_array(5)

game = Game(mazes[0])

game.runGame()