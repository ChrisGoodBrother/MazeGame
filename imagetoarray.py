from PIL import Image as im
import numpy as np

def convert_image_to_array(mazesAmount, mazes=[]):

    for i in range(1, mazesAmount):
        image = im.open(f'mazes/maze{i}.png')
        image = image.convert('L')
        data = np.asarray(image)
        threshold = 128
        maze = (data < threshold).astype(int)
        maze[1][0] = 0
        mazes.append(maze)

    return mazes