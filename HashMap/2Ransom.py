# Approach: Count the frequency of each letters, keep reducing
# Time O(n + m) | space O(1)

def canConstruct(ransomNote, magazine):
    freqInMag = [0]*26
    for letter in magazine:
        freqInMag[ord(letter) - ord('a')] += 1

    for letter in ransomNote:
        if freqInMag[ord(letter) - ord('a')] == 0:
            return False
        else:
            freqInMag[ord(letter) - ord('a')] -= 1
    return True

ransomNote = "aa"
magazine = "ab"

print(canConstruct(ransomNote, magazine))