# def find(s):

#     charS = set()
#     res = 0
#     l = 0

#     for r in range(len(s)):
#         while s[r] in charS:
#             charS.remove(s[l])
#             l += 1

#         charS.add(s[r])
#         res = max(res, r - l + 1)
#     return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lastSeen = {}
        res = 0

        l = 0

        for r, char in enumerate(s):
            if char in lastSeen and lastSeen[char] >= l:
                l = lastSeen[char] + 1
            res = max(res, r - l + 1)
            lastSeen[char] = r
        
        return res
