#Binary search implementation
#December 11, 2021

def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        #find the middle element in an array, rounded down
        mid = (low + high) // 2
        guess = list[mid]
        #if the value we are looking for is in the middle of the list
        if guess == item:
            return mid

        
        if guess > item:
            #guess was too high
            high = mid - 1
        else:
            #guess was too low
            low = mid + 1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list,3))

        

