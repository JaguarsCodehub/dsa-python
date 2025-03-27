# def binary_decimal(binary_str):
#     return int(binary_str, 2)

# print(binary_decimal('1010'))  # 10

def binary_decimal(binary_str):
    decimal = 0

    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

print(binary_decimal('1010'))  # 10

def binary_to_decimal(binary_str):
    decimal = 0

    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
        
    return decimal
