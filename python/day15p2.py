# part 2

def can_move(direction, start):
    queue = start
    visited = set()
    dx, dy = direction
    
    while queue:
        x, y = queue.pop()
        visited.add((x, y))
        nx, ny = x + dx, y + dy
        
        if grid[nx][ny] == "#":
            return None, False
        
        elif grid[nx][ny] in "[]":
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                side = (nx, ny - 1) if grid[nx][ny] == "]" else (nx, ny + 1)
                if side not in visited:
                    queue.append(side)

    return visited, True    


data = open("inputs/input15.txt").read().split("\n\n")

grid = [list(row) for row in data[0].split("\n")]
commands = data[1].replace("\n", "")

directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
pos = None
total = 0
new_grid = []

for ri, row in enumerate(grid):
    temp_row = []
    for rc, col in enumerate(row):
        if grid[ri][rc] == "@": temp_row += ["@", "."]
        elif grid[ri][rc] == "#": temp_row += ["#", "#"]
        elif grid[ri][rc] == "O": temp_row += ["[", "]"]
        else: temp_row += [".", "."]
    new_grid.append(temp_row)
    
grid = new_grid

for ri, row in enumerate(grid):
    temp_row = []
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
    
    elif grid[nx][ny] in "[]":
        side = (nx, ny - 1) if grid[nx][ny] == "]" else (nx, ny + 1)
        
        new_pos, move = can_move(directions[command], [side, (nx, ny)])
            
        if move:
            temp_grid = [list(row) for row in grid]
            
            for px, py in new_pos:
                temp_grid[px][py] = "."
            for px, py in new_pos:
                mx, my = px + dx, py + dy
                temp_grid[mx][my] = grid[px][py]
                        
            temp_grid[nx][ny], temp_grid[x][y] = "@", "."
            pos = (nx, ny)
            grid = temp_grid
        
for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        if grid[ri][rc] == "[":
            total += 100 * ri + rc

print("part 2:", total)
