def searchAnElementInArray(arr, target):

    indices = []

    for i in range(len(arr)):

        if arr[i] == target:
            indices.append(i)

        
    if not indices:
        return "Element not found or Incorrect Array"
    else:
        return indices    
        

arr = [20,40,10,60,20]
target = 20
print(searchAnElementInArray(arr, target))