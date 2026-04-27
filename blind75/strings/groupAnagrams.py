def groupAnagrams(strs):
    dictionary = {}

    for word in strs:
        signature = "".join(sorted(word))

        if signature in dictionary:
            dictionary[signature].append(word)
        else:
            dictionary[signature] = [word]
        
    return list(dictionary.values())
    