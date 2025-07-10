mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targetValue = 9

# LINEAR SEARCH
def linearSearch(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1
result = linearSearch(mylist, targetValue)

if result != -1:
    print("Found the index:", result)
else:
    print("Not Found")

