# Implement a function to check if two strings are anagrams of each other.
from collections import Counter 
def isAnagram(str1, str2):
    Counter(str1) == Counter(str2)

    return True

str1 = "listen"
str2 = "silent"

print(isAnagram(str1, str2))

class Solution:    
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
