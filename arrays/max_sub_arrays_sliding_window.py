def max_sub_array(nums, k):

    if (len(nums) < k):
        return "Invalid Input"
    
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum


nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sub_array(nums, k))