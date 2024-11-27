from PIL import Image as im
import numpy as np

image1 = im.open('mazes/maze1.png')
image1 = image1.convert('L')

data = np.asarray(image1)

threshold = 128
binary_maze = (data < threshold).astype(int)

print(binary_maze)