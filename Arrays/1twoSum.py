# https://leetcode.com/problems/two-sum/

# Approach 1: Brute force, try each pair
# Time O(n^2) | space O(1)

# Approach 2: Traverse through the array, store the element in hashmap with element as key and index as value
# When on the next element check if target-element is in hashmap keys, if present return [element_index, key_value]
# Time O(n) | space O(n)
def twoSum(nums, target):
    encountered = {}
    for index, value in enumerate(nums):
        needed = target-value
        if needed in encountered:
            return [encountered[needed], index]
        else:
            encountered[value] = index

nums = [3,3]
target = 6

print(twoSum(nums, target))