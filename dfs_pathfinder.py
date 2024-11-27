from PIL import Image as im
import numpy as np

def dfs(maze, s, e, path=None, visited=None):
    
    if visited is None:
        path = []
        visited = []

    path.append(s)
    visited.append(s)

    if s == e:
        return path
    
    coordY, coordX = s

    for node in [(coordY+1, coordX), (coordY-1, coordX), (coordY, coordX+1), (coordY, coordX-1)]:
        y, x = node
        if 0 <= y < len(maze) and 0 <= x < len(maze[0]):
            if node not in visited and maze[y][x] == 0:
                res = dfs(maze, node, e, path, visited)
                if res:
                    return res
                
    path.pop()
 
    return None
    

image = im.open(f'mazes/maze1.png')
image = image.convert('L')
data = np.asarray(image)
threshold = 128
maze = (data < threshold).astype(int)

print(maze)

mazeStart = (1,0) #maze[1][0]
mazeEnd = (19,20) #maze[19][20]

path = dfs(maze, mazeStart, mazeEnd)
print(path)