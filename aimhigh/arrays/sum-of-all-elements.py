def sumOfAllElements(arr):

    total = 0

    for num in arr:
        total = total + num
    return total

arr = [10, 20, 30, 40]
print(sumOfAllElements(arr))