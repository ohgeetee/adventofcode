import numpy as np


w = 2500
h = 2500

swatchlist = open("day3input.txt").read().strip().split("\n")
fabric = np.zeros((w, h), dtype=int)

for swatches in swatchlist:
    id_, _, position, dimension = swatches.split(" ") #parses line  ['#1', '@', '1,3:', '4x4'] from '#1 @ 1,3: 4x4'
    #print(swatches)

    id_ = id_[1:] #gets '1' out of '#1'
    x = position.split(',')[0] #gets '1' out of '1,3:'
    y = position.split(',')[1][:-1] #gets '3' out of '1,3:'
    width = dimension.split("x")[0] #gets 1st '4' out of '4x4'
    height = dimension.split("x")[1] #gets 2nd '4' out of '4x4'
    #print(id_, x, y, width, height)

    id_, x, y, width, height = int(id_), int(x), int(y), int(width), int(height) #change str to int

    fabric[y:y + height,x:x + width] += 1 #increment positions from file by 1

overlap = np.count_nonzero(fabric > 1) #get a count of overlapped indices
print(overlap)