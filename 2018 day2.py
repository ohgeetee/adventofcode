import itertools

#part1
#boxlist = open("day2input.txt").read().strip().split("\n")
boxlist = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
c = [0, 0]
for box in boxlist:
    x2 = False
    x3 = False
    for letter in box:
        if box.count(letter) == 2 and not x2:
            c[0] += 1
            x2 = True
        if box.count(letter) == 3 and not x3:
            c[1] += 1
            x3 = True
print(c)
print(c[1]*c[0])

#part2
#boxlist = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
boxlist = open("day2input.txt").read().strip().split("\n")
contenders = []
for a, b in itertools.combinations(boxlist, 2):
    count = sum(1 for x, y in zip(a, b) if x != y)
    if count == 1:
        contenders += a, b
print(contenders)
    