## Consecutive zeros
## The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string.##

def sizeof(n):
    count = 0
    if n == 0:
        return 1
    while n//10 != n:
        count += 1
        n //= 10
    return count


def consecutiveZeros(n):
    currentCount = 0
    maxCount = 0
    for i in range(sizeof(n)):
        units = n%10
        if units == 0:
            currentCount += 1
            if currentCount>maxCount:
                maxCount = currentCount
        else:
            currentCount = 0
        n = n//10
    return maxCount




