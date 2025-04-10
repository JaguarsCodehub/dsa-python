# Good Number

# You are given a number NN, and your task is to determine whether it is a "Good Number" or not. 
# A Good Number is defined as a number that is divisible by the sum of its own digits. 
# If the number is divisible by the sum of its digits, it is classified as Good, otherwise, 
# it is classified as Bad.
# Input Format

#     The first line of input will contain a single integer TT, denoting the number of test cases.
#     Each test case contains a single integer NN, the number you need to check.

# Output Format

# For each test case, print "Good Number" if the number is a Good, otherwise print "Bad Number".

def good_number(n):
    digit_sum = sum(int(d) for d in str(n))

    return "Good Number" if n % digit_sum == 0 else "Bad Number"

# Read number of test cases
T = int(input())

for _ in range(T):
    N = int(input())
    print(good_number(N))