import re

data = []
total = 0

with open("inputs/input13.txt") as f:
    temp = []
    for line in f.readlines():
        if line == "\n":
            data.append(temp)
            temp = []
        else:
            line = line.split()
            x, y = re.sub("\D", "", line[-2]), re.sub("\D", "", line[-1])
            temp.append((int(x), int(y)))
    
    data.append(temp)

for (ax, ay), (bx, by), (px, py) in data:
    # ax * A + bx * B = px
    # ay * A + by * B = py
    px += 10000000000000
    py += 10000000000000
    
    # Cramer's rule
    A = (px * by - py * bx) / (ax * by - ay * bx)
    B = (ax * py - ay * px) / (ax * by - ay * bx)
    
    if A % 1 == 0 and B % 1 == 0:
        total += int(A * 3 + B)

print(total)
