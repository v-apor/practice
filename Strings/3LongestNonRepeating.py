# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Approach: check longest substring for each character Time | O(n^2)

# Didn't worked
# def lengthOfLongestSubstring(s):
#     seen = {}
#     output = 0

#     currentLen = 0
#     for right, value in enumerate(s):
#         if value not in seen:
#             seen[value] = right
#             currentLen += 1
#         else:
#             currentLen = right - seen[value]
#             seen[value] = right
#         output = max(output, currentLen)
#     return output            

# Sliding Window, moving the window left when repeated entry found
# time O(n) | space O(n)
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    result = 0

    for right, value in enumerate(s):
        while value in seen:
            seen.remove(s[left])
            left += 1
        seen.add(value)
        result = max(result, right-left+1)
    return result

s = "pwwkew"
print(lengthOfLongestSubstring(s))