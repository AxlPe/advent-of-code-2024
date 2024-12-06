# part 2

def find_loops(guard_map, pos):
    x, y = pos        
    dx, dy = (-1, 0) 
    seen = {(x, y, dx, dy)}
    
    while 0 <= x + dx < len(guard_map) and 0 <= y + dy < len(row):
        if guard_map[x + dx][y + dy] == "#":
            dy, dx = (-dx, dy)
        else: 
            x += dx
            y += dy
        
        if (x, y, dx, dy) in seen:
            return True
        else:
            seen.add((x, y, dx, dy))
        
    return False


guard_map = [list(x) for x in open("inputs/input6.txt").read().split("\n")]
total = 0
start = (0, 0)

for index, row in enumerate(guard_map):
    if "^" in row:
        start = (index, row.index("^"))
        x, y = start
        dx, dy = (-1, 0) 
        seen = {(x, y)}
    
        while 0 <= x + dx < len(guard_map) and 0 <= y + dy < len(row):
            if guard_map[x + dx][y + dy] == "#":
                # rotate by 90° 
                dy, dx = (-dx, dy)
            else: 
                x += dx
                y += dy
            
            seen.add((x, y))
        
for ri, row in enumerate(guard_map):
    for ci, col in enumerate(row):
        if (ri, ci) in seen and guard_map[ri][ci] == ".":
            guard_map[ri][ci] = "#"
            total += find_loops(guard_map, start)
            guard_map[ri][ci] = "."
            
print("part 2:", total)
