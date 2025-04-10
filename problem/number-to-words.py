# Convert number to words

# You are tasked with creating a program that converts a given integer (up to 4 digits) 
# into its corresponding English words.
# Input Format

#     First line of input contains a single integer TT, the number of test cases.
#     Each test case consists of a single line containing a number N.

# Output Format

# For each test case, output the number in words, following the English naming conventions. 
# Each number should be converted to its corresponding words in lowercase, with words separated by a 
# single space.

class Solution:
    def numberToWords(n):

        ones = [
            "zero", 
            "one", 
            "two", 
            "three", 
            "four", 
            "five", 
            "six", 
            "seven", 
            "eight", 
            "nine"
        ]
        teens = [
            "ten", 
            "eleven", 
            "twelve", 
            "thirteen", 
            "fourteen", 
            "fifteen",
            "sixteen", 
            "seventeen", 
            "eighteen", 
            "nineteen"
        ]
        tens = [
            "", 
            "", 
            "twenty", 
            "thirty", 
            "forty", 
            "fifty",
            "sixty", 
            "seventy", 
            "eighty", 
            "ninety"
        ]

        def two_digits(num):
            if num < 10:
                return ones[num]
            elif num < 20:
                return teens[num - 10]
            else:
                return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
            
        def three_digits(num):
            if num < 100:
                return two_digits(num)
            else: 
                return ones[num // 100] + " hundred" + (
                    " " + two_digits(num % 100) if num % 100 != 0 else ""
                )
            
        if n == 0:
            return "zero"
        elif n < 1000:
            return three_digits(n)
        elif n < 10000:
            thousands = n // 1000
            remainder = n % 1000
            result = ones[thousands] + " thousand"
            if remainder:
                result += " " + three_digits(remainder)
            return result
        else:
            return "Number out of supported range"
        


# Read Input
T = int(input())
for _ in range(T):
    N = int(input())
    print(Solution.numberToWords(N))
            