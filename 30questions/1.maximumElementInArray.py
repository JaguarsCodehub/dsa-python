def maximum(arr):
    maxValue = arr[0]

    for num in arr:
        if num > maxValue:
            maxValue = num
    return maxValue


print(maximum(arr=[2,5,7,9,1,12]))