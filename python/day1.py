# part 1
total = 0
ls_one = []
ls_two = []

with open("inputs/input1.txt") as f:
    for line in f.readlines():
        a, b = line.strip().split()
        
        ls_one.append(int(a))
        ls_two.append(int(b))
        
ls_one.sort()
ls_two.sort()

for i in range(len(ls_one)):
    total += abs(ls_one[i] - ls_two[i])

print("part 1:", total)


# part 2
total = 0

for i in ls_one:
    total += i * ls_two.count(i)

print("part 2:", total)