# def palindrome(n):
#     n = abs(n)
#     return str(n) == str(n)[::-1]

# number = 12321
# print(palindrome(number))

def is_palindrome(n):
    n = abs(n)

    original, reverse = n, 0

    while n > 0:

        reverse = reverse * 10 + n % 10
        n //= 10

    return original == reverse
# def is_plaindrome(n):
#     n = abs(n)

#     original, reverse =  n,0

#     while n > 0:
#         reverse = reverse * 10 + n % 10
#         n //=10

#     return original == reverse

# number  = 12321
# print(is_plaindrome(number))