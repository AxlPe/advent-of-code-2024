# part 1

def can_move(direction, start):
    x, y = start
    dx, dy = direction
    
    while grid[x][y] == "O":
        nx, ny = x + dx, y + dy
        
        if grid[nx][ny] == "#":
            return (nx, ny), False
        elif grid[nx][ny] == ".":
            return (nx, ny), True
        
        x, y = nx, ny


data = open("inputs/input15.txt").read().split("\n\n")

grid = [list(row) for row in data[0].split("\n")]
commands = data[1].replace("\n", "")

directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
pos = None
total = 0

for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        if grid[ri][rc] == "@":
            pos = (ri, rc)

for command in commands:
    x, y = pos
    dx, dy = directions[command]
    nx, ny = (x + dx, y + dy)
    
    if grid[nx][ny] == ".":
        grid[nx][ny], grid[x][y] = "@", "."
        pos = (nx, ny)   
    elif grid[nx][ny] == "O":
        new_pos, move = can_move(directions[command], (nx, ny))
        if move:
            grid[nx][ny], grid[x][y] = "@", "."
            grid[new_pos[0]][new_pos[1]] = "O"
            pos = (nx, ny)

for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        if grid[ri][rc] == "O":
            total += 100 * ri + rc

print("part 1:", total)
