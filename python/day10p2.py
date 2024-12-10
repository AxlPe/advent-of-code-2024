# part 2

grid = open("inputs/input10.txt").read().split("\n")
total = 0


def find_trailhead(pos, n):
    x, y = pos
    count = 0
    
    if n == 9:
        return 1
    
    if x - 1 >= 0:
        if int(grid[x - 1][y]) == n + 1:
            count += find_trailhead((x - 1, y), int(grid[x - 1][y]))
            
    if x + 1 < len(grid):
        if int(grid[x + 1][y]) == n + 1:
            count += find_trailhead((x + 1, y), int(grid[x + 1][y]))
    
    if y + 1 < len(grid[0]):
        if int(grid[x][y + 1]) == n + 1:
            count += find_trailhead((x, y + 1), int(grid[x][y + 1]))
   
    if y - 1 >= 0:
        if int(grid[x][y - 1]) == n + 1:
            count += find_trailhead((x, y - 1), int(grid[x][y - 1]))

    
    return count


for ri, row in enumerate(grid):
    for rc, col in enumerate(row):
        char = grid[ri][rc]
        if char == "0":
            total += find_trailhead((ri, rc), int(char))

print("part 2:", total)
