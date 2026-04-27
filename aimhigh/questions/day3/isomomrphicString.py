def isomorphicStrings(s, t):
    # Two strings are isomorphic if characters in `s` can be replaced to get `t`
    # with a 1-to-1 (bijective) mapping:
    # - each char in `s` maps to exactly one char in `t`
    # - each char in `t` maps back to exactly one char in `s`
    mapS = {}  # maps characters from `s` -> characters in `t`
    mapT = {}  # maps characters from `t` -> characters in `s`

    if len(s) != len(t):
        # Different lengths can never be isomorphic.
        return False
    
    for i in range(len(s)):
        # Compare characters at the same index.
        charS = s[i]
        charT = t[i]

        # If we've seen `charS` before, it must always map to the same `charT`.
        if charS in mapS and mapS[charS] != charT:
            return False
        
        # If we've seen `charT` before, it must always map back to the same `charS`.
        if charT in mapT and mapT[charT] != charS:
            return False
        
        # Record (or re-affirm) the mapping in both directions.
        mapS[charS] = charT
        mapT[charT] = charS

    # If we never found a conflict, the mapping is consistent in both directions.
    return True

# Need to watch Video