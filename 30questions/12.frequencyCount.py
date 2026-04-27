def freqCount(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

print(freqCount(arr=[1,2,3,4,5,6,1,4,2]))