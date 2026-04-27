def maximumProductSubArray(nums):

    res = max(nums)

    currMin, currMax = 1, 1

    for n in nums:
        if n == 0:
            currMin, currMax = 1, 1
            continue
        temp = currMax * n
        currMax = max(n * currMax, n * currMin, n) # [-1, 8] <- here we will have to entertain self product too
        currMin = min(temp, n * currMin, n) # [-1, 8] <- here we will have to entertain self product too

        res = max(res, currMax)
    
    return res