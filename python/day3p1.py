# part 1
total = 0

with open("inputs/input3.txt") as f:
    l = 0
    for line in f.readlines():
        for index, c in enumerate(line):
            if c == "(":
                l = index
            
            if c == ")" and line[l] == "(":
                mul = line[l + 1:index]
                
                if line[l - 3:l] == "mul":
                    try:
                        a, b = mul.split(",")
                        total += int(a) * int(b)
                    except:
                        pass
                l = index

print("part 1:", total)