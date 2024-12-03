# part 2
total = 0

with open("inputs/input3.txt") as f:
    l = 0
    d = 0
    do = True
    
    for line in f.readlines():
        for index, c in enumerate(line):
            # check instruction
            if c == "d":
                d = index
            
            if c == ")" and line[d] == "d":
                if line[d:index + 1] == "don't()":
                    do = False
                if line[d:index + 1] == "do()":
                    do = True
                d = index
            
            # check operation
            if c == "(":
                l = index
            
            if c == ")" and line[l] == "(":
                mul = line[l + 1:index]
                
                if line[l - 3:l] == "mul" and do:
                    try:
                        a, b = mul.split(",")
                        total += int(a) * int(b)
                    except:
                        pass
                l = index

print("part 2:", total)