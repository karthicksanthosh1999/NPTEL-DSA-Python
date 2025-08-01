arr = [100,40,20,2,5,8,90]

def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        swaped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j+1] = arr[j+1], arr[j]
                swaped = True
            elif swaped == True:
                break
    return arr

if __name__=="__main__":
    result = bubbleSort(arr)
    print(result)