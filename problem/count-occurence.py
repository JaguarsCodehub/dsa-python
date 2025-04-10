# Count occurence in Number

# You are given a number N and a digit D. Your task is to count the number of times 
# the digit D occurs in the number N.


# Input Format
# The first line of input will contain a single integer TT, denoting the number of test cases.
# For each test case:
# The first line contains a single integer NN.
# The second line contains a single integer DD.
# Output Format
# For each test case, output the number of times the digit DD occurs in the number NN on a new line.


T = int(input())

for _ in range(T):
    N = int(input())
    D = int(input())

    count = 0

    while N > 0:
        if N % 10 == D:
            count += 1
        N //= 10

    print(count)