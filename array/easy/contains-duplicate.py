def contains_duplicate(arr):
    check = {}
    for i in range(len(arr)):
        if arr[i] in check:
            check[arr[i]] += 1
        else:
            check[arr[i]] = 1
    print(check)
    for value in check.values():
        if value >= 2:
            return True
    return False


print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))