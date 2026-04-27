def count(arr):
    # [2, 3,6,1,8]

    even, odd = 0, 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

print(count(arr=[1,4,7,2,1,8]))
