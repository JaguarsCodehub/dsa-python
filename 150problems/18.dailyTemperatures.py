def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []
    
    for i in range(n):
        print("value of i:", i)
        while stack and temperatures[i] > temperatures[stack[-1]]:
            print("Current temp",temperatures[i])
            print("Current Top of the stack temperature",temperatures[stack[-1]])
            prevIndex = stack.pop()
            print("prevIndex before:", prevIndex)


            result[prevIndex] = i - prevIndex

        stack.append(i)
        print("Current Stack",stack)
    print("Result: ",result)
    return result

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures=temperatures))