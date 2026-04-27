def factorial(num):

    if num == 0: return False

    result = 1

    for i in range(2, num + 1):
        result *= i
    return result

print(factorial(num=5))