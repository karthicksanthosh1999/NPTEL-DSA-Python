mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targetValue = 5

# LINEAR SEARCH
def linearSearch(arr,target):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == target:
            is_found = True
            return i
        if is_found:
            break;
    return None

print(linearSearch(mylist, targetValue))
