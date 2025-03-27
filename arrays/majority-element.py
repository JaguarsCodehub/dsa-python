# def majority_element(arr):

#     count = 0
#     candidate = None

#     for num in arr:
#         if count == 0:
#             candidate = num
#         if num == candidate:
#             count += 1
#         else:
#             count -= 1

#     return candidate


# arr = [2, 2, 1, 1, 1, 2, 2]
# print(majority_element(arr))

def majority_element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate