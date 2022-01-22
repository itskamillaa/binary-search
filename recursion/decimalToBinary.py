def findBinary(n,result = ""):
  if n == 0:
    return result
  
  result = str(n%2) + result
  return findBinary(int(n/2),result)

print(findBinary(17))