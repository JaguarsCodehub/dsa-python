# def reverseString(str):
#     return str[:: -1]

def reverseString(str):

    chars = list(str)

    left, right = 0, len(str) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1
    
    return "".join(chars)

print(reverseString(str='jyotindra'))