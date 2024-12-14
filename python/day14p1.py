import re
# part 1

robots = []
total = 1

with open("inputs/input14.txt") as f:
    for line in f.readlines():
        robot = list(map(int, re.findall(r"-?\d+", line)))
        robots.append(robot)

cols = 101
rows = 103

for _ in range(100):
    for robot in robots:
        px, py, vx, vy = robot
        x = px + vx
        y = py + vy
        
        if x < 0:
            x += cols
        elif x >= cols:
            x = x % cols 
            
        if y < 0:
            y += rows
        elif y >= rows:
            y = y % rows

        robot[0] = x
        robot[1] = y

quadrant_count = [0, 0, 0, 0]

for ri in range(rows):
    for ci in range(cols):
        c = [tuple(x[:2]) for x in robots].count((ci, ri))
        
        col_mid = cols // 2
        row_mid = rows // 2
        
        if ri < row_mid and ci < col_mid:
            quadrant_count[0] += c
        if ri < row_mid and ci > col_mid:
            quadrant_count[1] += c
        if ri > row_mid and ci < col_mid:
            quadrant_count[2] += c
        if ri > row_mid and ci > col_mid:
            quadrant_count[3] += c

for n in quadrant_count:
    total *= n

print("part 1:", total)
