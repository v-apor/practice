# https://leetcode.com/problems/valid-anagram/
# Note, assuming the string is of same size
# Approach 1: Sort the string & compare Time O(nlogn) | space O(n)
# Approach 2: Create a frequency array Time O(n) | space O(1)
# Approach 3: Using python counter class

# Approach 2
# def isAnagram(s, t):
#     freqList = [0] * 26
#     s = s.lower()
#     t = t.lower()
#     for ch in s:
#         freqList[ord(ch) - ord('a')] += 1
#     for ch in t:
#         freqList[ord(ch) - ord('a')] -= 1
#     for num in freqList:
#         if num != 0:
#             return False
#     return True

# Approach 3
from collections import Counter
def isAnagram(s, t):
    x = Counter(s)
    y = Counter(t)
    return True if x == y else False 


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))