# def right_rotate(arr, k):
#     k = k % len(arr)  # Handle cases where k > len(arr)
#     for _ in range(k):
#         last = arr.pop()  # Remove last element
#         arr.insert(0, last)  # Insert at beginning
#     return arr

# # Example
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(right_rotate(arr, k))  # Output: [4, 5, 1, 2, 3]

def right_rotate(arr, k):
    k = k % len(arr)
    for _ in range(k):
        last = arr.pop()
        arr.insert(0, last)
    return arr

arr = [1, 2, 3, 4, 5]
k = 2
print(right_rotate(arr, k))