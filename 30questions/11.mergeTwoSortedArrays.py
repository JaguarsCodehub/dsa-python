def mergeTwoSortedArrays(a, b):
    i = j = 0
    mergedArray = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            mergedArray.append(a[j])
            i += 1
        else:
            mergedArray.append(b[j])
            j += 1
    
    mergedArray.extend(a[i:])
    mergedArray.extend(b[j:])

    return mergedArray

# In Place Optimized
#  ------------------- To be continued
def mergeTwoSortedArraysOptimized(a, b):
    pass