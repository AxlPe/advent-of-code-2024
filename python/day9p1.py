# part 1
data = open("inputs/input9.txt").read()

files = []
file_id = 0
total = 0

for i, c in enumerate(data):    
    if i % 2 == 0:
        files += [file_id] * int(c)
        file_id += 1
    else:
        files += ["."] * int(c)

l = 0
r = len(files) - 1

while l < r:
    if files[l] == "." and files[r] != ".":
        files[l], files[r] = files[r], files[l]
        r -= 1
    if files[r] == ".":
        r -= 1
    if files[l] != ".":
        l += 1

for i, c in enumerate(files):
    if c == ".":
        break
    
    total += i * int(c)

print("part 1:", total)
