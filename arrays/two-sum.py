# def two_sum(nums, target):

#     numMap = {}

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in numMap:
#             return [numMap[complement], i]
        
#         numMap[num] = i

#     return []


# nums = [2, 7, 11, 15]
# target = 17
# print(two_sum(nums, target))

def two_sum(nums, target):
    numMap = {}

    for i, num in enumerate(nums):

        complement = target - num

        if complement in  numMap:
            return [numMap[complement], i]
        
        numMap[num] = i

    return []


nums = [2, 7, 11, 15]
target = 17
print(two_sum(nums, target))