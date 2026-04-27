def reverseBits(n):
    res = 0

    for i in range(32):
        bit = n & 1
        res = (res << 1) | bit
        n >> 1

    return res