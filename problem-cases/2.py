# Alice challenged Bob to write the same word as his on a typewriter. 
# Both are kids and are making some mistakes in typing and are making use of the ‘#’ key on a typewriter 
# to delete the last character printed on it.

# An empty text remains empty even after backspaces. 

# Input Format
# The first line contains a string typed by Bob.
# The second line contains a string typed by Alice.

# Output Format
# The first line contains ‘YES’ if Alice is able to print the exact words as Bob , otherwise ‘NO’.

# Bob and Alice only contain lowercase letters and '#' characters.

# Testcase Input
# ab#c
# ad#c

# Testcase Output
# YES

class Solution: 
    def process_typing(s):
        stack = []

        for char in s:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
    
    # Read Input
    bob = input().strip()
    alice = input().strip()

    final_bob = process_typing(bob)
    final_alice = process_typing(alice)

    print("YES" if final_bob == final_alice else "NO")
    
