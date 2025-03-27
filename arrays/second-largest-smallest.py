# def find_second_largest_smallest(arr):
#     if len(arr) < 2:
#         return print("Array must have at least 2 elements.")
    
#     arr = list(set(arr))
#     arr.sort()

#     return arr[1], arr[-2]


# arr = [10, 5, 20, 8, 25, 3]
# second_largest, second_smallest = find_second_largest_smallest(arr)
# print(f"Second Largest: {second_largest}, Second Smallest: {second_smallest}")

def find_second_largest_smallest(arr):

    if (len(arr) < 2):
        return print("Array must have at least 2 elements.")
    
    arr = list(set(arr))
    arr.sort()

    return arr[1], arr[-2]

arr = [10, 5, 20, 8, 25, 3]
second_largest, second_smallest = find_second_largest_smallest(arr)
print(f"Second Largest: {second_largest}, Second Smallest: {second_smallest}")