# One day, Jack finds a string of characters. He is very keen to arrange them in reverse order, 
# i.e., the first characters become the last characters, the second characters become the 
# second-last characters, and so on.

# Now he wants your help  to find the kth character from the new string 
# formed after reverse the original string.

# Note: String contains only lowercase Latin letters.

# Input Format
# The first line contains two integers n, k — the length of array and the value of k respectively.
# The second line contains a string containing n characters.

# Output Format
# Print a single line containing the kth character of the string.

n, k = map(int, input().split())
s = input()

reversed_string = s[::-1]

print(reversed_string[k-1])