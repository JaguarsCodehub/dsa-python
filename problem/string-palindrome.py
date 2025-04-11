def isPalindrome():
    s = input().strip()

    return s == s[::-1]


print(isPalindrome())