# arr = [1, 4, 9, 7, 4] # Added a duplicate '4' to show the effect
# setarr = set(arr)     # Step 1: Removes duplicates -> {1, 4, 7, 9}
# final_list = list(setarr) # Step 2: Back to list -> [1, 4, 7, 9]

# print(f"Original:", arr)
# print(f"Set (Unique):", setarr)
# print(f"Final List:", final_list)

# Brute Force Appraoch
# def secondLargest(arr):
#     arr = list(set(arr))

#     arr.sort()
#     print(arr)
#     return arr[-1]

# print(secondLargest(arr=[1, 4, 9, 7, 4]))

# def second_largest(arr):
#     first = second = float('-inf')
#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#     return second


def secondLargest(arr):

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second