# def find_missing_number(arr):
#     n = len(arr) + 1
#     total_sum = n * (n + 1) // 2
#     return total_sum - sum(arr)

# arr = [1, 2, 3, 5]
# print(find_missing_number(arr))  # 4

# Using XOR when no extra space is allowed
def find_missing_number(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i
    
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

arr = [1, 2, 3, 5]
print(find_missing_number(arr))