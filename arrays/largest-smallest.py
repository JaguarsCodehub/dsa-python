# def find_largest_smallest(arr):
#     largest = arr[0]
#     smallest = arr[0]

#     for num in arr:
#         if num > largest:
#             largest = num
#         if num < smallest:
#             smallest = num
#     return largest, smallest

# arr = [-60, 60,]
# largest, smallest = find_largest_smallest(arr)  # (5, 1)
# print(f"Largest: {largest}, Smallest: {smallest}")


def find_largest_smallest(arr):
    largest = arr[0]
    smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest


arr = [1, 2, 3, 4, 5]
largest, smallest = find_largest_smallest(arr)  # (5, 1)
print(f"Largest: {largest}, Smallest: {smallest}")