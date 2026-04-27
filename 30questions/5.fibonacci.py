# def fibonacci(n):

#     a, b = 0, 1

#     for _ in range(n):
#         print(a, end=" ")
#         a, b = a, a + b

# print(fibonacci(n=5))

def fibonacciSpaceOptimized(n):
    if n <= 0 or n == 1: return False

    a, b = 0, 1

    for _ in range(n):
        a, b = b , a + b
    return a

print(fibonacciSpaceOptimized(n=10))

def fibonacci(n):
    if n <= 0 or n == 1: return False

    seq = [0, 1]

    for _ in range(2, n):
        nextValue = seq[-1] + seq[-2]
        seq.append(nextValue)

    return seq

print(fibonacci(n=10))