# part 1
total = 0
grid = []


def make_word(pos, grid, direction):
    word = ""
    x, y = pos
    
    for i in range(4):
        if direction == "down":
            word += grid[x + i][y]
        if direction == "up":
            word += grid[x - i][y]
        if direction == "down-right":
            word += grid[x + i][y + i]
        if direction == "up-right":
            word += grid[x - i][y + i]
        if direction == "down-left":
            word += grid[x + i][y - i]
        if direction == "up-left":
            word += grid[x - i][y - i]
    
    return word


def word_check(pos, grid):
    x, y = pos
    count = 0
    
    # left
    if y >= 3:
        if grid[x][y - 3:y + 1] == "SAMX":
            count += 1
    # right
    if y <= len(grid[0]) - 4:
        if grid[x][y:y + 4] == "XMAS":
            count += 1
    # down
    if x <= len(grid) - 4:
        if make_word(pos, grid, "down") == "XMAS":
            count += 1
    # up
    if x >= 3:
        if make_word(pos, grid, "up") == "XMAS":
            count += 1
    # down-right
    if x <= len(grid) - 4 and y <= len(grid[0]) - 4:
        if make_word(pos, grid, "down-right") == "XMAS":
            count += 1
    # up-right
    if x >= 3 and y <= len(grid[0]) - 4:
        if make_word(pos, grid, "up-right") == "XMAS":
            count += 1
    # down-left
    if x <= len(grid) - 4 and y >= 3:
        if make_word(pos, grid, "down-left") == "XMAS":
            count += 1
    # up-left
    if x >= 3 and y >= 3:
        if make_word(pos, grid, "up-left") == "XMAS":
            count += 1
            
    return count


with open("inputs/input4.txt") as f:
    for line in f.readlines():
        grid.append(line.strip())

for r_index, row in enumerate(grid):
    for c_index, col in enumerate(row):
        if col == "X":
            total += word_check((r_index, c_index), grid)

print("part 1:", total)