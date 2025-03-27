# def move_zero_elements(arr):
#     non_zero_index = 0

#     for i in range(len(arr)):

#         if arr[i] != 0:
#             arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
#             non_zero_index += 1
        
#     return arr


# arr = [0, 1, 0, 3, 12]
# print(move_zero_elements(arr))


# Using Extra Lists
# def move_zero_elements(arr):
#     non_zero = [num for num in arr if num != 0]
#     zeroes = [0] * (len(arr) - len(non_zero))

#     list = non_zero + zeroes
#     return list


# arr = [0, 1, 0, 3, 12]
# print(move_zero_elements(arr))

# using Extra lists
def move_zero_elements(arr):

    non_zero = [num for num in arr if num != 0]
    zeroes = [0] * (len(arr) - len(non_zero))

    list = non_zero + zeroes
    return list

arr = [0, 1, 0, 3, 12]
print(move_zero_elements(arr))