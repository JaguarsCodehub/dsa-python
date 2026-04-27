# def productOfArrayExceptSelf(nums):

#     n = len(nums)
#     leftProduct = 1
#     rightProduct = 1

#     answer = [1] * n

#     for i in range(n):
#         answer[i] *= leftProduct
#         leftProduct *= nums[i]

#     for i in range(n - 1, -1, -1):
#         answer[i] *= rightProduct
#         rightProduct *= nums[i]
    
#     return answer

def productsExceptSelf(nums):

    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res