# part 1

guard_map = [list(x) for x in open("inputs/input6.txt").read().split("\n")]

for index, row in enumerate(guard_map):
    if "^" in row:
        x, y = (index, row.index("^"))
        seen = {(x, y)}
        dx, dy = (-1, 0) 
        
        while 0 <= x + dx < len(guard_map) and 0 <= y + dy < len(row):
            if guard_map[x + dx][y + dy] == "#":
                # rotate by 90° 
                dy, dx = (-dx, dy)
            else: 
                x += dx
                y += dy
            
            seen.add((x, y))

print("part 1:", len(seen))
