# part 2
data = [x.split(": ") for x in open("inputs/input7.txt").read().split("\n")]
total = 0


def is_valid(target, n, nums, pos):
    if pos >= len(nums) or n > target:
        if n == target:
            return True
        else:
            return False    

    count = 0
    new_n = int(str(n) + str(nums[pos]))
    
    count += is_valid(target, n * nums[pos], nums, pos + 1)
    count += is_valid(target, n + nums[pos], nums, pos + 1)
    count += is_valid(target, new_n, nums, pos + 1)
    
    return count


for d in data:
    target, nums = d
    array = [int(x) for x in nums.split()]
    if is_valid(int(target), array[0], array, 1):
        total += int(target)

print("part 2:", total)
