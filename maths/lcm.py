# def gcd(a, b):
#     while b:
#         a, b  = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)
    
# print(lcm(12, 15))


def gcd(a, b ):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(12, 15)) 