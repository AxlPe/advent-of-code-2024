# part 2
total = 0

def is_increasing(ls):
    l = 0
    r = 1
    safe = True
    
    while r < len(ls):
        a, b = ls[l], ls[r]
        
        if a < b and (b - a) <= 3:
            l += 1
            r += 1
        else:
            if safe:
                ls.pop(r)
                safe = False
            else: 
                return False
    
    return True


def is_decreasing(ls):
    l = 0
    r = 1
    safe = True
    
    while r < len(ls):
        a, b = ls[l], ls[r]
        
        if a > b and (a - b) <= 3:
            l += 1
            r += 1
        else:
            if safe:
                ls.pop(l)
                safe = False
            else: 
                return False
    
    return True


with open("inputs/input2.txt") as f:
    for line in f.readlines():
        report = [int(i) for i in line.split()]
        
        if is_decreasing(report.copy()):
            total += 1
        elif is_increasing(report.copy()):
            total += 1

print("part 2:", total)
