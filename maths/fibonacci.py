# def fibonacci(n):

#     n = abs(n)

#     a,b = 0, 1

#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

#     return a

# number = 10
# print(fibonacci(number))

def fibonacci(n):
    n = abs(n)

    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    return a


number = 10
print(fibonacci(number))