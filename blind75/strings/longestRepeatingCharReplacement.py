# def longestRepeatingCharReplacement(s, k):
    
#     count =  {}
#     res = 0
#     l = 0

#     for r in range(len(s)):
#         count[s[r]] = 1 + count.get(s[r], 0)

#         while (r - l + 1) - max(count.values())> k:
#             count[s[l]] -= 1
#             l += 1
#         res = max(res, r - l + 1)
#     return res

# def longestRepeatingCharReplacement(s, k):
    
#     res = 0
#     l = 0
#     count = {}

#     for r in range(len(s)):
#         count[s[r]] = 1 + count.get(s[r], 0)

#         while (r - l + 1) - max(count.values()) > k:
#             count[s[l]] -= 1
#             l += 1
        
#         res = max(res, (r - l + 1))
#     return res


def find(s, k):
    left = 0
    res = 0
    maxCount = 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = 1 + freq.get(s[right], 0)
        maxCount = max(maxCount, freq[s[right]])

        if right - left + 1 - maxCount > k:
            freq[s[left]] -= 1
            left += 1
    return len(s) - left