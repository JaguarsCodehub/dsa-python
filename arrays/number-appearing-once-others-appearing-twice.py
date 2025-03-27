# def find_unique_number(arr):
#     unique = 0
#     for num in arr:
#         unique = unique ^ num
#     return unique

# arr = [2, 2, 3, 3, 4, 5, 5]
# print(find_unique_number(arr)) # 4


def find_unique_number(arr):

    unique = 0

    for num in arr:
        unique = num ^ unique

    return unique

arr = [2, 2, 3, 3, 4, 5, 5]
print(find_unique_number(arr))