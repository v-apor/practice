def twoSum(nums, target):
    encountered = {}
    for index, value in enumerate(nums):
        needed = target-value
        if needed not in encountered:
            encountered[value] = index
        else:
            return [index, encountered[needed]]


nums = [3, 3]
target = 6
print(twoSum(nums, target))