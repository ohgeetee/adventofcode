import numpy as np
#np.set_printoptions(threshold=np.inf)

w = 1000
h = 1000


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

    swatch = fabric[y:y + height,x:x + width]
    
    swatch += 1 #increment positions from file by 1

    #if np.sum(fabric) == np.prod(fabric.shape):
    #print(np.sum(swatch))
    #print(np.prod(fabric[y:y + height,x:x + width].shape))

overlap = np.count_nonzero(fabric > 1) #get a count of overlapped indices
print(overlap)
#print("Lone ID = ", oid)
#print(fabric)

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

    swatch = fabric[y:y + height,x:x + width]
    if np.sum(swatch) == np.prod(fabric[y:y + height,x:x + width].shape):
        loneid = id_

print("Lone ID = ", loneid)