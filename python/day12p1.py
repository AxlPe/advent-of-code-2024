# part 1
 
grid = open("inputs/input12.txt").read().split("\n")
seen = set()
areas = []
total = 0


def check_neighbors(pos, char):
    x, y = pos
    neighbors = []
    fences = 0
    
    for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + r < len(grid) and 0 <= y + c < len(grid[0]):
            new_pos = (x + r, y + c)
            if char == grid[x + r][y + c] and new_pos not in seen:
                neighbors.append(new_pos)
                seen.add(new_pos)
            elif char != grid[x + r][y + c]:
                fences += 1
        else:
            fences += 1
    
    return neighbors, fences


for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        pos = (ri, rc)
        c = grid[ri][rc]
        
        if pos not in seen:
            seen.add(pos)
            queue = [pos]
            visited = set()
            fences_count = 0
            
            while queue:
                curr = queue.pop(0)
                visited.add(curr)
                neighbors, fences = check_neighbors(curr, c)
                queue += neighbors
                fences_count += fences
                 
            areas.append((len(visited), fences_count))

for area, perimeter in areas:
    total += area * perimeter

print("part 1:", total)