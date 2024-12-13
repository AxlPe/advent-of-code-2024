# part 2
 
grid = open("inputs/input12.txt").read().split("\n")
seen = set()
areas = []
total = 0


def check_neighbors(pos, char):
    x, y = pos
    neighbors = []
    
    for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + r < len(grid) and 0 <= y + c < len(grid[0]):
            new_pos = (x + r, y + c)
            if char == grid[x + r][y + c] and new_pos not in seen:
                neighbors.append(new_pos)
                seen.add(new_pos)
    
    return neighbors


def count_sides(area):
    corners = set()
    for r, c in area:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corners.add((cr, cc))
    
    count = 0
    for cr, cc in corners:
        corner_list = []
        for nr, nc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]:
            corner_list.append((nr, nc) in area)
        if sum(corner_list) == 1:
            count += 1
        elif sum(corner_list) == 2:
            if corner_list == [False, True, False, True] or corner_list == [True, False, True, False]:
                count += 2
        elif sum(corner_list) == 3:
            count += 1
    
    return count


for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        pos = (ri, rc)
        c = grid[ri][rc]
        
        if pos not in seen:
            seen.add(pos)
            queue = [pos]
            visited = set()
               
            while queue:
                curr = queue.pop(0)
                visited.add(curr)
                neighbors = check_neighbors(curr, c)
                queue += neighbors

            areas.append(list(visited))

for area in areas:
    total += len(area) * count_sides(area)

print("part 2:", total)
