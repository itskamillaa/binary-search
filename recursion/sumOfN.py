def findSumOfN(n):
    if n <= 1:
        return n
    return n + findSumOfN(n-1)


print(findSumOfN(10)) 