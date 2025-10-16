# def productOfArrayExceptSelf(arr):
#     n = len(arr)

#     left = [1] * n
#     right = [1] * n
#     answer = [0] * n

#     for i in range(1, n):
#         left[i] = left[i - 1] * arr[i - 1]
    
#     for i in range(n - 2, -1, -1):
#         right[i] = right[i + 1] * arr[i + 1]

#     for i in range(n):
#         answer[i] = left[i] * right[i]



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