def contains_duplicate(arr):
    check = {}
    for i in arr:
        if i in check:
            return True
        check[i] = 1
    return False


print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))