# Factorial without Multiplication & Division

# You are given a positive integer NN. Your task is to compute the factorial of NN without using any multiplication (∗)(∗) or division (/)(/) operators.

# Factorial of a number NN is defined as: N!=N×(N−1)×(N−2)×...×1N!=N×(N−1)×(N−2)×...×1.
# Input Format

#     The first line of input will contain a single integer TT, denoting the number of test cases.
#     Each of the next TT lines will contain a single integer NN, where NN is the number for which you need to calculate the factorial.


def factorial(number):
    # number  = abs(number)
    
    
    upper = 1
    for i in range(number, 1, -1):
        upper = (upper / (1.0 / i))
    return upper


number = 4
print(factorial(number))