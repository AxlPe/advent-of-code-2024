from collections import defaultdict

# part 1
total = 0
pages = []
page_order = defaultdict(list)


def valid_order(page):
        i = 0
        
        while i < len(page):
            for j in range(i + 1, len(page)):
                if page[j] not in page_order[page[i]]:
                    return False
            i += 1
        
        return True
    
    
with open("inputs/input5.txt") as f:
    check = False
    for line in f.readlines():
        if line == "\n":
            check = True
        else:
            if not check:
                x, y = line.strip().split("|")
                page_order[x].append(y)
            else:
                pages.append(line.strip().split(","))
                
for page in pages:
    if valid_order(page):
        mid = page[len(page) // 2]
        total += int(mid)

print("part 1:", total)