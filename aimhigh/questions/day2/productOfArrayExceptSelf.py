def productOfArrayExceptSelf(nums):

    n = len(nums)
    leftProduct = 1
    rightProduct = 1

    answer = [1] * n

    for i in range(n):
        answer[i] *= leftProduct
        leftProduct *= nums[i]

    for i in range(n - 1, -1, -1):
        answer[i] *= rightProduct
        rightProduct *= nums[i]
    
    return answer