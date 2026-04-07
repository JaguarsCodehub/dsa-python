# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

def validAnagram(s, t):

    if len(s) != len(t):
        return 0
    count = {}

    for i in range(len(s)):
        charS = s[i]
        count[charS] = count.get(charS, 0) + 1

        charT = t[i]
        count[charT] = count.get(charT, 0) - 1
 
    for val in count.values():
        if val != 0:
            return False
    
    return True