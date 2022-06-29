# Approach 1: Traverse through the array calculate the product counting the number of 0s.
# if there are more than 1 zero then return array with all zeros
# if only 1 zero then return the array with all values 0 except the place of 0 in original array, that will have product
# If no zero then return the array having all position as prod/num in that position
# Time O(n) | space O(n)
def productExceptSelf(nums):
    zero_count = 0
    prod = 1
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            prod *= num

    if zero_count >= 2:
        return [0]*len(nums)
    elif zero_count == 1:
        result = [0]*len(nums)
        result[nums.index(0)] = prod
        return result
    else:
        return [int(prod/i) for i in nums]

nums = [-4,1,0,-3,-3]
print(productExceptSelf(nums))