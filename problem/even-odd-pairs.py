# Count Pairs divisible by 2

# You're given a list of numbers. Your task is to find how many pairs of numbers in that 
# list add up to an even number. A pair consists of two different numbers from the list. 
# For example, in the list [1, 2, 3, 4], the pairs that sum to an even number are (1, 3) and (2, 4).

def count_even_odd_pairs(nums):

    even = sum(1 for num in nums if num % 2 == 0)
    odd  = len(nums) - even

    even_pairs = even * (even - 1) // 2
    odd_pairs = odd * (odd - 1) // 2

    return even_pairs + odd_pairs


nums = [1, 2, 3, 4, 67, 12, 43, 78, 90, 45]
print(count_even_odd_pairs(nums))