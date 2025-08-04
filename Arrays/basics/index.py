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

# Q.
arr = [-5, 1, 4, 2, 12]

def alternate_elements(arr):
    n =len(arr)
    elements =[]
    for i in range(0,n):
        if i%2 == 0:
            elements.append(arr[i])

    return elements
print(alternate_elements(arr))

