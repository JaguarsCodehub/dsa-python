import math

def isPrime(n):

    n = abs(n)

    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

number = 29
print(isPrime(number))