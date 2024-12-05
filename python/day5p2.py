from collections import defaultdict

# part 2
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


def order_count(page):
    new_page = []
    queue = page.copy()
    
    while queue:
        p = queue.pop(0)
        count = 0
        for i in page:
            if i in page_order[p] and i != p:
                count += 1
        new_page.append((p, count))
    
    return new_page
                
                    
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
    if not valid_order(page):
        new_page = order_count(page)
        new_page = sorted(new_page, key=lambda x: x[1])
        mid = new_page[len(page) // 2][0]
        total += int(mid)

print("part 2:", total)