# Encode and Decode Strings

def encode(strs):
    result = ""

    for s in strs:
        result += str(len(s)) + '#' + s
    return result

strs = ["neet","code","love","you"]
encoded = print(encode(strs))

def decode(strs):
    result = []
    i = 0

    while i < len(encoded):
        j = i
        while strs[j] != "#":
            j += 1

        length = int(strs[i:j])

        result.append()
