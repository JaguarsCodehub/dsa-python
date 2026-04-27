# Group Anagram:

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# def groupAnagram(strs):
#     cabinetDict = {}

#     for word in strs:
#         signature = "".join(sorted(word))

#         if signature in cabinetDict:
#             cabinetDict[signature].append(word)
#         else:
#             cabinetDict[signature] = [word]
        
#     return list(cabinetDict.values())

def groupAnagrams(strs):
    cabinetDict = {}

    for word in strs:
        signature = "".join(sorted(word))

        if signature in cabinetDict:
            cabinetDict[signature].append(word)
        else:
            cabinetDict[signature] = [word]
    
    return list(cabinetDict.values())



def groupAnagram(strs):

    cabinetDict = {}

    for word in strs:
        signature = "".join(sorted(word))

        if signature in cabinetDict:
            cabinetDict[signature].append(word)
        else:
            cabinetDict[signature] = [word]

        
    return list(cabinetDict.values())