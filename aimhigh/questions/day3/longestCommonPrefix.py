def longestCommonPrefixOptimal(strs):
    if not strs:
        return ""

    # 1. Use the first word as our reference
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # 2. Check this character index in every OTHER word
        for j in range(1, len(strs)):
            # If the current word is too short OR the character doesn't match
            if i == len(strs[j]) or strs[j][i] != char:
                # Return everything we've matched so far
                return strs[0][:i]
                
    return strs[0]


# Need to watch Video