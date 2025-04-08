# from collections import Counter

# def is_anagram(s1, s2):
#     Counter(s1) == Counter(s2)

#     return True


# s1 = "listen"
# s2 = "silent"
# print(is_anagram(s1, s2))

from collections import Counter

def is_anagram(s1, s2):
    Counter(s1) == Counter(s2)

    return True