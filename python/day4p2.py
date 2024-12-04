# part 2
total = 0
grid = []


def cross_check(pos, grid):
    x, y = pos
    count = 0
    
    word = grid[x - 1][y - 1] + "A" + grid[x + 1][y + 1]
    if word == "SAM" or word == "MAS":
        count += 1
    word = grid[x + 1][y - 1] + "A" + grid[x - 1][y + 1]
    if word == "SAM" or word == "MAS":
        count += 1
    
    return True if count == 2 else False


with open("inputs/test.txt") as f:
    for line in f.readlines():
        grid.append(line.strip())

for r_index, row in enumerate(grid[1:len(grid) - 1]):
    for c_index, col in enumerate(row[1:len(row) - 1]):
        if col == "A":
            if cross_check((r_index + 1, c_index + 1), grid):
                total += 1

print("part 2:", total)
