import re
# part 2

robots = []
total = 1

with open("inputs/input14.txt") as f:
    for line in f.readlines():
        robot = list(map(int, re.findall(r"-?\d+", line)))
        robots.append(robot)

cols = 101
rows = 103

def move():
    unique_pos = set()
    
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
        unique_pos.add((x, y))
    
    return unique_pos


i = 0

while True:
    unique_pos = move()
    
    if len(robots) == len(unique_pos):
        grid = [list( "." * cols) for _ in range(rows)]
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                if (ci, ri) in [tuple(x[:2]) for x in robots]: 
                    grid[ri][ci] = "X"

        for g in grid:
            print("".join((list(map(str, g)))))
        print("part 2:", i + 1)
        break
    
    i += 1
