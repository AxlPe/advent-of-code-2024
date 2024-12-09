# part 2
data = open("inputs/input9.txt").read()

total = 0
files = {}
free_space = []
file_id = 0
pos = 0

for i, c in enumerate(data):    
    if i % 2 == 0:
        files[file_id] = (pos, int(c))
        file_id += 1
    else:
        if c != "0":
            free_space.append((pos, int(c)))
    
    pos += int(c)

fsize = len(files)
new_pos = {}

while fsize > 0:
    fsize -= 1
    pos, size = files[fsize]
    for i, (p, length) in enumerate(free_space):
        if p >= pos:
            break
        if size <= length:
            new_pos[fsize] = (p, size)
            if size == length:
                free_space.pop(i)
            else:
                free_space[i] = (p + size, length - size)
            break

# merge 2 dicts
files = files | new_pos

for k, (pos, size) in files.items():
    for i in range(size):
        total += (pos + i) * k
        
print("part 2:", total)
