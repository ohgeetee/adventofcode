
#part1
boxlist = open("day2input.txt").read().strip().split("\n")
c = [0, 0]
for box in boxlist:
    x2 = False
    x3 = False
    for letter in box:
        if box.count(letter) == 2 and not x2:
            c[0] += 1
            x2 = True
    for letter in box:
        if box.count(letter) == 3 and not x3:
            c[1] += 1
            x3 = True
print(c)
print(c[1]*c[0])