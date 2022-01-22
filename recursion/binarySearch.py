def binarySearch(array, left, right, target):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if target == array[mid]:
        return mid

    if target < array[mid]:
        return binarySearch(array,left, mid-1, target)
    
    return binarySearch(array,mid+1,right,target)

arr = [-1,0,1,2,3,4,7,9,10,20]
print(binarySearch(arr,0,len(arr)-1,10))