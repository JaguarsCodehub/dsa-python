def left_rotate(arr, k):

    if k < 0:
        print(f"Array must be atleast {k} elements long.")
        return
    

    k = k % len(arr)    # Handle cases where k > len(arr)


    for _ in range(k):
        first  = arr.pop(0)
        arr.append(first)
    return arr


arr = [1, 2, 3, 4, 5]
k = 2
print(left_rotate(arr, k))