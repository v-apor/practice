# https://leetcode.com/problems/maximum-subarray/

# Approach 1: Try out every single sequence 
# Approach 2: Note that the value of each element is not it's actual value, but max(actual value, sum so far)
# Traverse through the array keeping track of max_global and max_ongoing_chain
# Time O(n) | space O(1)

def maxSubArray(nums):
    max_global = max_current = nums[0]
    for ele in nums[1:]:
        max_current = max(max_current+ele, ele)
        max_global = max(max_current, max_global)

    return max_global

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))