from collections import defaultdict

# part 1
grid = [list(x) for x in open("inputs/input8.txt").read().split("\n")]

antinodes = set()
antennas = defaultdict(list)

for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        c = grid[ri][rc]
        if c != ".":
            antennas[c].append((ri, rc))

for values in antennas.values():
    if len(values) == 1:
        continue
    
    i = 0
    j = 0
    
    while i < len(values):
        if i != j:
            a, b = values[i]
            c, d = values[j]
            diff = (a - c, b - d)
            antinode = (a - diff[0] * 2, b - diff[1] * 2)
            
            if 0 <= antinode[0] < len(grid) and 0 <= antinode[1] < len(grid[0]):
                antinodes.add(antinode)
                    
        j += 1
        
        if j >= len(values):
            i += 1
            j = 0

print("part 1:", len(antinodes))
