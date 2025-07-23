arr = [100,40,20,2,5,8,90]
def insertionSort(arr):
    n =len(arr)    
    for i in range(1,n):
        currentVal = arr[i]
        j=i-1
        while j>=0 and currentVal<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = currentVal
    return arr

if __name__ == "__main__":
    result = insertionSort(arr)
    print(result)
            
            