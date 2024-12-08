from PIL import Image as im
import numpy as np

def dfs(maze, s, e, path=[], visited=[]):

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

def bfs(maze, s, e):

    visited = []
    parent = {}
    queue = []

    visited.append(s)
    parent[s] = None
    queue.append(s)

    while queue:
        poppedNode = coordY, coordX = queue.pop(0)

        if poppedNode == e:
            path = []
            while poppedNode is not None:
                path.append(poppedNode)
                poppedNode = parent[poppedNode]
            path.reverse()
            return path

        for node in [(coordY+1, coordX), (coordY-1, coordX), (coordY, coordX+1), (coordY, coordX-1)]:
            y, x = node
            if 0 <= y < len(maze) and 0 <= x < len(maze[0]):
                if node not in visited and maze[y][x] == 0:
                    visited.append(node)
                    queue.append(node)
                    parent[node] = poppedNode

    return None