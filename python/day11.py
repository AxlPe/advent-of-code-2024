from functools import cache

stones = [int(x) for x in open("inputs/input11.txt").read().split()]


@cache
def count_stones(stone, blinks):
    if blinks == 0:
        return 1 
    if stone == 0:
        return count_stones(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        l, r = int(str(stone)[:mid]), int(str(stone)[mid:])
        return count_stones(l, blinks - 1) + count_stones(r, blinks - 1)
    else:
        return count_stones(stone * 2024, blinks - 1)


print("part 1:", sum([count_stones(stone, 25) for stone in stones]))
print("part 2:", sum([count_stones(stone, 75) for stone in stones]))
