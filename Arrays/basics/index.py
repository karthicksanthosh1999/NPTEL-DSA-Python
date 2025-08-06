array = [3,2,10,1,5,2,1]

# Q1: Find the largest element in array
def largetElementInArray(arr):
    n=len(arr)
    largest = arr[0]
    for i in range(n):
        if arr[i] >= largest:
            largest = arr[i]
    return largest

largetElementInArray(array)
# Output -> 10


# Q2: Find the second largets element in array
def secondLargestElementInArray(arr):
    n=len(arr)
    large = arr[0]
    second_large = arr[0]
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] < large and arr[i] > second_large:
            second_large = arr[i]
    return {large, second_large}

secondLargestElementInArray(array)
# Output -> {10, 5}
        

# Q3: Find the second smallest element in array
def second_smallest_element_in_array(arr):
    n=len(arr)
    smallest = arr[0]
    second_smallest = arr[0]
    for i in range(n):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] > smallest and arr[i] != smallest:
            second_smallest = arr[i]
    return {smallest, second_smallest}

# print(second_smallest_element_in_array(array))

# Q. Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

def search(arr, x):
    n = len(arr)
    is_found= False
    for i in range(0,n):
        if arr[i] == x:
            is_found = True
            return i
        if is_found:
            break
    return -1
    
        
# print(search(array, 100)

# Q. Alternate elements of an array

def getAlternatesRecr(arr,idx,res):
    if idx < len(arr):
        res.append(arr[idx])
        return getAlternatesRecr(arr,idx + 2, res)

def getAlternates(arr):
    res =[]
    getAlternatesRecr(arr,0,res)
    return res

# if __name__ == "__main__":
#     arr = [10, 20, 30, 40, 50]
#     res = getAlternates(arr)
#     print(" ".join(map(str,res)))

# Q.Remove duplicates from Sorted Array

def removeDublicates(arr):
    n=len(arr)
    idx = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx += 1
    return idx 

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDublicates(arr)
    for i in range(newSize):
        print(arr[i], end=" ")