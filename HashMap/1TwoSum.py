# Approach 1: Try every possible combination | Time O(n^2)
# Approach 2: Keep saving the index of traversed element in dict,
# and lookup for every new element if sum leads to target & return index
def twoSum(nums, target):
    encountered = {}
    for index, ele in enumerate(nums):
        needed = target - ele
        if needed in encountered:
            return [encountered[needed], index]
        else:
            encountered[ele] = index

nums = [3, 3]
target = 6
print(twoSum(nums, target))