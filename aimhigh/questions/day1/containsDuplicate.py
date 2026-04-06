# 217. Contains Duplicate
# Given an integer array nums, return True if any value appears at least twice,
# and return False if every element is distinct.

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return containsDuplicate(nums)


# Example:
# nums = [1, 2, 3, 1]
# print(containsDuplicate(nums))  # True
