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

print(second_smallest_element_in_array(array))

