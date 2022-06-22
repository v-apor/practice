# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Approach 1: Keep a set, keep inserting till repeats, update max variable & empty set
# At the end return max vs set length
# Time O(n) | Space O(n)
# DOESN'T WORK, COS WE ARE SKIPPING ELEMENTS FROM ONE SEQUENCE
# def lengthOfLongestSubstring(s):
#     max_len = 0
#     len_current = 0
#     char_appeared = set()
#     for ch in s:
#         if ch in char_appeared:
#             max_len = max(max_len, len_current)
#             char_appeared = set(ch)
#             len_current = 1
#         else:
#             char_appeared.add(ch)
#             len_current += 1
#     return max(max_len, len_current)

# Approach 2: Brute, for each element check max sequence length
# Time O(n^2) | Space O(n)
# Got TLE
def lengthOfLongestSubstring(s):
    max_len = 0
    for i in range(len(s)):
        len_current = 0
        char_appeared = set()
        for j in range(i, len(s)):
            if s[j] in char_appeared:
                max_len = max(max_len, len_current)
                char_appeared = set(s[j])
                len_current = 1
            else:
                char_appeared.add(s[j])
                len_current += 1
        max_len = max(max_len, len_current)
    return max_len

print(lengthOfLongestSubstring("pwwkew"))