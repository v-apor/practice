# Approach 1: make the array lower case, take two pointers at each end and move to middle,
# every character should match till both pointers meet
# Time O(n) | Space O(1)


# for replacing non alphanumeric
# P.S: I could have also used string.isalnum() to check if alphanumeric instead of re
import re

def isPalindrome(s):
    s = s.lower()
    # [a-z] meaning any character from a-z & ^ at front meaning 'not'
    x = re.sub("[^a-z0-9]+", '', s)
    left = 0
    right = len(x) - 1
    while (left <= right):
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))